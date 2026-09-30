# Default Workflow

This is a routing map, not a demand for bulky artifacts on every edit.

~~~text
Owner natural language
        |
        v
Intent contract
        |
        +--> existing LLM task contract? --> Contract reality check
        |
        v
Reality Reconnaissance — PRE
(current project + official/upstream + field reality as relevant)
        |
        v
Engineering execution
(Superpowers when useful)
        |
        v
Reality Reconnaissance — POST
(re-check the actual diff's external/operational assumptions)
        |
        v
Fresh code verification
        |
        +--> meaningful diff? --> Independent review
        |
        +--> security surface? --> Codex Security
        |
        v
Reality verification
(browser / Windows / Android / target system)
        |
        v
Owner handoff
(plain-language status + evidence + residual risk)
~~~

The invariant is not use every external source for every typo.

The invariants are:

> no material assumption may silently become implementation truth from model prior alone;

> when code depends on current external or operational reality, that reality is checked before implementation and attacked again after the diff exists;

> no lower-grade evidence may be reported as higher-grade evidence.
