# Voice and Claims

Jinstone should sound like an engineering organization that expects its work
to be challenged by someone skeptical. When a result cannot yet be rerun from
public artifacts, say so directly.

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

Current example:

> One frozen Qwen2.5 x86 local-node configuration completed 5/5 internal runs
> with p50 7543.840 ms and p95 8471.469 ms. Evidence: HOST. Boundary: the
> supporting artifacts remain private, so this does not establish external
> reproduction, semantic acceptance, an edge/cloud comparison, performance
> leadership, or an SLA.

## Evidence language

| Level | Allowed verbs | Prohibited implication |
|---|---|---|
| `FIXTURE` | exercises, validates the contract, detects | measured hardware performance |
| `HOST` | records, establishes a host baseline, repeats internally | edge-device efficiency or external reproduction |
| `BOARD` | measures, qualifies one path, compares | general platform superiority |
| `FPGA` | demonstrates the architecture, changes the path | tapeout readiness or ASIC power |
| `SILICON` | implements, measures physical silicon | production readiness without qualification |

## Naming releases

Prefer a literal outcome:

- `Progress 001 — one internal local-node path`
- `Execution Receipt 0.2 — route and fallback identity are explicit`
- `Qualification Cell 0.2 — collector identity is now fail-closed`

Avoid names that imply maturity the artifact has not earned: “platform,”
“production,” “industry-leading,” “world’s first,” and “autonomous lab” all
require unusually strong evidence.

## Endorsements and traction

Programs, mentors, investors, event selection, and introductions are context,
not product evidence. Do not describe them as backing, investment, customer
validation, or market traction without an explicit public commitment from the
relevant party. A design-partner conversation is not a design partner, and a
private internal run is not an externally reproduced result.
