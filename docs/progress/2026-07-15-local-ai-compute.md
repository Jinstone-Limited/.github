# Progress 001: One Real Local Path, Not Customer Validation

**2026-07-15 · Internal HOST evidence**

径石的产品边界已经从“先做芯片 / 先建验证实验室”重置为 **Local AI
Compute Node + Runtime**：让一个 AI workload 根据时延、隐私、质量、成本和
失败约束，在设备、本地节点或云端选择并真实执行路径，再由反复出现的瓶颈决定
是否进入 runtime、FPGA 或芯片。

## What changed

The product contract is now explicit:

```text
workload constraints
  → placement decision
  → execution + visible fallback
  → evidence-bound receipt
  → software / existing hardware / custom compute / stop
```

A chip is no longer the assumed answer. It has to be earned by repeated
external workload evidence. Today, only the internal local-node slice has a
real execution record; device and cloud paths remain unmeasured.

## Internal evidence today

Internal records for one frozen Qwen2.5 x86 local-node configuration show five
completed fresh offline runs:

| Result | Value |
|---|---:|
| Successful runs | `5 / 5` |
| p50 end-to-end latency | `7.544 s` |
| p95 end-to-end latency | `8.471 s` |
| `30 s` request budget | eligible |
| `3 s` request budget | blocked |

The path binds input, model, runtime, target, adapter, route, output, and receipt
identities. Persisted records remove prompt and completion plaintext, local
paths, full argv, hostname, and raw stream text.

## Claim boundary

This is locally identity-pinned internal `HOST` evidence. It does **not** prove:

- customer demand or semantic acceptance;
- performance leadership or an SLA;
- an edge/cloud comparison;
- availability, memory, power, or cost qualification;
- clean-clone reproduction outside the prepared host.

The builder image, model distribution path, runtime artifact, and supporting
run-set report are not public today. The numbers above are therefore not
independently reproducible public evidence. The private monorepo also contains
hardware inventory and must not be made public by changing repository
visibility.

## The next hard gate

Jinstone will implement an external pilot only when one workflow owner provides:

1. acceptance authority and an evaluator owner;
2. an approved non-sensitive fixture manifest;
3. executable acceptance and critical-fail rules;
4. at least two real candidate paths;
5. a dated continuation resource if the test passes.

Current count: **0 approved external packets, 0 design partners, 0 paid or dated
engineering commitments, and 0 second real execution paths.** That is the
product bottleneck.

## 2026-08-09 target

Run one approved external workload on the local node and at least one real edge
or cloud path, demonstrate visible failure and fallback, return an auditable
receipt, and obtain one external continue / stop decision backed by resources.
