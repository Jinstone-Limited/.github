<div align="center">

<img src="https://raw.githubusercontent.com/Jinstone-Limited/.github/main/profile/assets/jinstone-banner.jpg" alt="Jinstone" width="680" />

### Routing is the new bottleneck.

**Custom paths for inference on silicon** · RISC-V

<sub>径石 — 为 MoE 路由与矩阵乘热点，在开放 ISA 上刻出可集成的推理路径</sub>

<br/>

[![MoE](https://img.shields.io/badge/Wedge-MoE_routing-1A1F26?style=for-the-badge&logo=gitbranch&logoColor=white)](https://github.com/Jinstone-Limited)
[![ISA](https://img.shields.io/badge/ISA-RISC--V-1A1F26?style=for-the-badge&logo=openjdk&logoColor=white)](https://riscv.org)
[![Hotspot](https://img.shields.io/badge/Hotspot-matmul-1A1F26?style=for-the-badge&logo=matrix&logoColor=white)](https://github.com/Jinstone-Limited)
[![Labs](https://img.shields.io/badge/Labs-FranklinNexus-F4F5F7?style=for-the-badge&logo=github&logoColor=1A1F26)](https://github.com/FranklinNexus)

</div>

---

## Thesis

Dense GPUs trained the models. **Sparse, routed inference** is still running on the wrong silicon.

Every generation pushes more decisions into **expert selection, gating, and irregular memory** — while accelerators keep optimizing for one thing: big, uniform matmul blocks.

**Jinstone lives in that gap.** Not broadly at "edge AI." Narrowly at **routing × matmul × integration** — the two kernels and one control plane that decide whether inference ships on-device or dies in the cloud bill.

> The next moat is not a bigger API. It is **a path through the ISA you own.**

---

## What we build

**Jinstone（径石）** — edge inference infrastructure carved into **RISC-V**.

| | |
|---|---|
| **径** | The path — expert routing, gating, ISA-level control |
| **石** | The silicon — custom ops, coprocessors, blocks you can integrate |

```text
profile → extend → prove → integrate
   │         │        │          │
software   custom   FPGA /     reference
baseline   ISA      sim        design
```

```text
Profile (MoE · matmul) → Extend (RISC-V ISA) → Prove (sim · FPGA) → Integrate (edge PoC)
```

We do **one vertical** exceptionally well:

- **MoE routing** — selection, gating, memory-bound control flow  
- **Matmul hotspots** — accelerate what the profile actually hits  
- **Open ISA surface** — inspectable, extensible, partner-ready  

No general-purpose GPU. No application wrapper. No benchmark theater.

---

## Why now

| Everyone optimizes for | Models actually need |
|----------------------|----------------------|
| Dense tensor cores | **Sparse activation & expert routing** |
| Closed black boxes | **An ISA you can extend and audit** |
| Cloud-scale power budgets | **Watts per useful token at the edge** |
| Slide-deck "AI chips" | **Reproducible profile → silicon artifact** |

Model structure moved. **Silicon didn't keep up.** Jinstone is the correction — quiet, measured, and built to tape out thinking.

---

## How we work

Cold engineering. Hot problem.

1. **Profile before you pipeline** — real workloads, real numbers  
2. **Extend only where the profile screams** — no vanity instructions  
3. **Prove in sim and FPGA** — same benchmarks, every iteration  
4. **Ship artifacts others can run** — not narratives they can't verify  

We are a **silicon infrastructure** team in temperament: restraint in scope, obsession in the wedge.

**Brand & assets →** [docs/brand](https://github.com/Jinstone-Limited/.github/tree/main/docs/brand)

---

## Status

**In the lab.** Baselines running. Extensions under validation. Public experiments at **[FranklinNexus](https://github.com/FranklinNexus)**; core reference designs maturing here.

Follow **[@Jinstone-Limited](https://github.com/Jinstone-Limited)** for releases. Design-partner conversations welcome — bring a workload, not a deck.

---

<div align="center">

<img src="https://raw.githubusercontent.com/Jinstone-Limited/.github/main/profile/assets/jinstone-mark.png" alt="Jinstone" height="56" />

<br/>

**JINSTONE**

*Custom paths for inference on silicon.*

<br/>

<sub>Hong Kong · 径石</sub>

</div>
