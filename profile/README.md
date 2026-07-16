<div align="center">

<img src="https://raw.githubusercontent.com/Jinstone-Limited/.github/main/profile/assets/jinstone-mark.png" alt="Jinstone" height="96" />

<h1>JINSTONE · 径石</h1>

**Make enterprise-owned AI compute as easy to use as cloud.**

径石让企业像用云一样，使用自己的 AI 算力。

提交一个 AI 任务和约束，Jinstone Runtime 决定它在设备、本地节点还是云端运行，
失败时如何回退，并返回结果与可核验的执行记录。

[Product](#product) · [Progress](#progress) · [Design partners](#design-partners) · [Progress 001](../docs/progress/2026-07-15-local-ai-compute.md)

</div>

## Why now

AI is moving from chat windows into robots, vehicles, intelligent devices, and
private workflows. These systems cannot assume that every request can wait for
the cloud:

- networks disconnect;
- private data cannot always leave the site;
- actions have latency and availability requirements;
- complex work may still need a local node or cloud capacity.

Teams currently stitch these paths together one integration at a time.
Jinstone is building the local compute layer that makes execution location,
failure, and evidence explicit.

## Product

The first product form is **Jinstone Local AI Computer**: a local compute node
and runtime for robotics, automotive, intelligent-device, edge-AI, and private-AI
teams.

```text
AI task + constraints
  → choose device / local node / cloud
  → execute and fail over visibly
  → result + verifiable execution record
```

The user works through one workload interface. The runtime handles placement,
execution, fallback, and the record of what actually happened.

<img src="https://raw.githubusercontent.com/Jinstone-Limited/.github/main/profile/assets/jinstone-workbench-alpha-v2.png" alt="Jinstone Workbench alpha after a read-only local-path evaluation" width="100%" />

## Progress

Jinstone has built a Workbench alpha and closed its first real technical loop
on one internal local path:

```text
task constraints → path selection → real offline inference → execution record
```

This establishes that the product contract can reach real execution. It does
not yet establish customer demand, a production deployment, performance
leadership, an SLA, or a completed device/local/cloud product.

The next product milestone is an external workload running on the local node
and at least one real device or cloud path, with an explicit failure test and a
continue/stop decision from the workflow owner.

## Why Jinstone

Jinstone starts from the workload, not from a predetermined chip.

Repeated bottlenecks decide what to build next:

1. use software and existing hardware first;
2. measure the complete workload, not an isolated benchmark;
3. enter custom runtime, FPGA, IP, or silicon only when the same high-value
   bottleneck survives and an external team wants the next version.

> **Run AI where it belongs. Build silicon when the workload demands it.**

## Founder

**Fanrui Kong · 孔繁睿**, 19, studies Microelectronics Science and Technology at
Xi'an Jiaotong-Liverpool University.

He has built across workload interfaces, runtime systems, RISC-V, FPGA, and
chip design. That range lets Jinstone follow one real AI task from the product
surface down to the hardware bottleneck, while keeping silicon as an earned
decision rather than a starting story.

## Design partners

Jinstone is looking for its first design partners in robotics, automotive,
intelligent hardware, edge AI, and private AI.

The strongest starting workload has:

- a real reason to stay local, such as privacy, latency, or continuous operation;
- a non-sensitive test fixture;
- at least two candidate execution paths;
- one workflow owner who can accept or reject the result.

Jinstone's two-week pilot target is to deliver real execution, an explicit
failure/fallback test, and a before/after decision. A successful test should
lead to a dated next commitment: engineering time, an interface, a device, or
pilot budget.

## Twelve-month target

- Local Compute Runtime v1.0 and adapter SDK;
- three classes of execution path;
- at least two external workloads;
- at least two design partners;
- one paid pilot, NRE, or equivalent engineering commitment;
- one whole-system optimization derived from a repeated external workload
  bottleneck;
- a Silicon Go/No-Go decision, not a promised tapeout.

---

<div align="center">

**JINSTONE · 径石**

*Run AI where it belongs.*

</div>
