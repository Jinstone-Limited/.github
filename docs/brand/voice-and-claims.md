# Voice and Claims

Jinstone should sound like an engineering organization that expects its work
to be rerun by someone skeptical.

## Voice

| Attribute | Write this way | Avoid |
|---|---|---|
| Literal | Name the workload, target, and result | “Revolutionary acceleration” |
| Calm | State the consequence once | Repeating the thesis as hype |
| Bounded | Say exactly what the evidence establishes | Turning one kernel into a product claim |
| Technical | Prefer units, identities, and mechanisms | Dense jargon used as status signaling |
| Long-term | Explain the system that compounds | Chasing every model or board release |

## Claim grammar

Every result follows this order:

```text
[workload] on [identified target] changed [literal metric]
from [baseline] to [result] under [conditions].
Evidence: [level]. Boundary: [what remains unproven].
```

Example:

> The visual inspection loop on DEVICE-001 reduced p95 sensor-to-action
> latency from 184 ms to 121 ms at the same test set and action interface.
> Evidence: BOARD. This does not establish production reliability or another
> device/runtime path.

## Evidence language

| Level | Allowed verbs | Prohibited implication |
|---|---|---|
| `FIXTURE` | exercises, validates the contract, detects | measured hardware performance |
| `HOST` | establishes a host baseline, reproduces | edge-device efficiency |
| `BOARD` | measures, qualifies one path, compares | general platform superiority |
| `FPGA` | demonstrates the architecture, changes the path | tapeout readiness or ASIC power |
| `SILICON` | implements, measures physical silicon | production readiness without qualification |

## Naming releases

Prefer a literal outcome:

- `Qualification Cell 0.2 — collector identity is now fail-closed`
- `Q4 dot primitive — 1.8× on the bound FPGA workload`
- `Board Agent 0.3 — offline status joins evidence and inventory`

Avoid names that imply maturity the artifact has not earned: “platform,”
“production,” “industry-leading,” “world’s first,” and “autonomous lab” all
require unusually strong evidence.
