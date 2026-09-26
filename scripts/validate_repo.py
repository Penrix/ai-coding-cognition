#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []
warnings: list[str] = []

REQUIRED = [
    "README.md",
    "START-HERE.md",
    "AGENTS.md",
    "cognition/00-owner-and-agent.md",
    "cognition/02-evidence-and-completion.md",
    ".agents/plugins/marketplace.json",
    "plugins/penrix-coding-core/.codex-plugin/plugin.json",
]

for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required file: {rel}")

def load_json(rel: str):
    try:
        return json.loads((ROOT / rel).read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid JSON {rel}: {exc}")
        return {}

market = load_json(".agents/plugins/marketplace.json")
manifest = load_json("plugins/penrix-coding-core/.codex-plugin/plugin.json")

if market:
    if not isinstance(market.get("name"), str) or not market["name"]:
        errors.append("marketplace.name must be a non-empty string")
    entries = market.get("plugins")
    if not isinstance(entries, list):
        errors.append("marketplace.plugins must be an array")
        entries = []

    seen = set()
    for i, entry in enumerate(entries):
        name = entry.get("name")
        if not isinstance(name, str) or not name:
            errors.append(f"marketplace plugin[{i}] missing name")
            continue
        if name in seen:
            errors.append(f"duplicate marketplace plugin name: {name}")
        seen.add(name)

        source = entry.get("source")
        if not isinstance(source, dict):
            errors.append(f"{name}: source must be an object")
            continue
        stype = source.get("source")
        if stype == "local":
            path = source.get("path")
            if not isinstance(path, str) or not path.startswith("./"):
                errors.append(f"{name}: local source path must begin with ./")
            else:
                plugin_root = ROOT / path[2:]
                pmanifest = plugin_root / ".codex-plugin" / "plugin.json"
                if not pmanifest.is_file():
                    errors.append(f"{name}: local plugin manifest missing at {pmanifest.relative_to(ROOT)}")
                else:
                    try:
                        data = json.loads(pmanifest.read_text(encoding="utf-8"))
                        if data.get("name") != name:
                            errors.append(f"{name}: marketplace name does not match manifest name {data.get('name')!r}")
                    except Exception as exc:
                        errors.append(f"{name}: invalid local plugin manifest: {exc}")
        elif stype == "git-subdir":
            if not source.get("url") or not source.get("path"):
                errors.append(f"{name}: git-subdir requires url and path")
        elif stype == "url":
            if not source.get("url"):
                errors.append(f"{name}: url source requires url")
        else:
            errors.append(f"{name}: unsupported source type in this repository validator: {stype!r}")

        policy = entry.get("policy")
        if not isinstance(policy, dict):
            errors.append(f"{name}: policy must be an object")
        else:
            if policy.get("installation") not in {"NOT_AVAILABLE", "AVAILABLE", "INSTALLED_BY_DEFAULT"}:
                errors.append(f"{name}: invalid policy.installation")
            if policy.get("authentication") not in {"ON_INSTALL", "ON_USE"}:
                errors.append(f"{name}: invalid policy.authentication")
        if not entry.get("category"):
            errors.append(f"{name}: category is required")

if manifest:
    if manifest.get("name") != "penrix-coding-core":
        errors.append("Penrix Core manifest name mismatch")
    skills_path = manifest.get("skills")
    if not isinstance(skills_path, str) or not skills_path.startswith("./"):
        errors.append("Penrix Core manifest skills path must be relative and begin with ./")

skill_root = ROOT / "plugins/penrix-coding-core/skills"
skill_names = set()
if skill_root.is_dir():
    for skill_file in sorted(skill_root.glob("*/SKILL.md")):
        text = skill_file.read_text(encoding="utf-8")
        front = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        rel = skill_file.relative_to(ROOT)
        if not front:
            errors.append(f"{rel}: missing YAML front matter")
            continue
        block = front.group(1)
        name_match = re.search(r"^name:\s*(\S+)\s*$", block, re.M)
        desc_match = re.search(r"^description:\s*(.+)$", block, re.M)
        if not name_match:
            errors.append(f"{rel}: missing skill name")
        else:
            name = name_match.group(1)
            if name in skill_names:
                errors.append(f"duplicate skill name: {name}")
            skill_names.add(name)
            if skill_file.parent.name != name:
                errors.append(f"{rel}: folder name and skill name differ")
        if not desc_match or not desc_match.group(1).strip():
            errors.append(f"{rel}: missing description")

expected_skills = {
    "using-penrix-coding-core",
    "intent-contract",
    "contract-reality-check",
    "reality-verification",
    "owner-handoff",
}
missing_skills = expected_skills - skill_names
if missing_skills:
    errors.append("missing Penrix Core skills: " + ", ".join(sorted(missing_skills)))

# Validate local Markdown links in README and START-HERE where the target is a repo path.
for rel in ["README.md", "START-HERE.md"]:
    p = ROOT / rel
    if not p.is_file():
        continue
    content = p.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
        if "://" in target or target.startswith("#"):
            continue
        clean = target.split("#", 1)[0]
        if clean and not (ROOT / clean).exists():
            errors.append(f"{rel}: broken local link -> {target}")

if errors:
    print("REPOSITORY VALIDATION: FAIL")
    for error in errors:
        print(f"ERROR: {error}")
    for warning in warnings:
        print(f"WARN: {warning}")
    sys.exit(1)

print("REPOSITORY VALIDATION: PASS")
print(f"Marketplace plugins: {len(market.get('plugins', []))}")
print(f"Penrix Core skills: {len(skill_names)}")
for warning in warnings:
    print(f"WARN: {warning}")
