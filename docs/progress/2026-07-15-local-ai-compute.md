# Progress 001: The First Real Local Execution Loop

**2026-07-15 · Workbench alpha**

Jinstone has reset its product around one concrete goal:

> Make enterprise-owned AI compute as easy to use as cloud.

An AI team should submit a workload and its latency, privacy, cost,
availability, and failure constraints. Jinstone should choose an eligible
device, local-node, or cloud path, execute it, fail over visibly when required,
and return the result with a verifiable execution record.

## What changed

Jinstone no longer treats a chip as the starting product.

The first product form is **Local AI Computer**: a local compute node and
runtime for robotics, automotive, intelligent hardware, edge-AI, and private-AI
teams.

```text
AI task + constraints
  → placement
  → real execution and visible fallback
  → result + execution record
  → repeated bottleneck
  → software / existing hardware / custom compute / stop
```

Silicon remains a long-term capability. It becomes a product decision only
after the same high-value bottleneck survives software and existing hardware,
and an external team wants the next version.

## What exists today

- a Workbench alpha for workload constraints and path selection;
- a real offline inference adapter for the local node;
- a versioned execution record that binds the request, chosen path, runtime,
  result identity, and failure state;
- one internal local path that completes the full technical loop;
- an intake contract for the first external workload.

The current loop is:

```text
task constraints → path selection → real offline inference → execution record
```

This is a meaningful engineering milestone because the product surface now
reaches real execution. It is not merely an architecture diagram or benchmark.

## What it does not prove

The current alpha does not yet establish:

- customer demand or customer acceptance;
- a production deployment;
- a completed device/local/cloud product;
- a real cross-path fallback in an external workflow;
- semantic quality, an SLA, or performance leadership;
- a repeatable public installation outside the prepared internal environment.

The company is therefore at **technical alpha / product discovery**, not
commercial validation.

## Next 90 days

The next hard milestone is the first design-partner deployment:

1. obtain one external workload with a non-sensitive fixture and acceptance owner;
2. run it on the local node and at least one real device or cloud path;
3. make a controlled failure and fallback visible;
4. deliver a before/after and Go/No-Go decision;
5. earn a dated continuation resource: engineering time, an interface, a
   device, or pilot budget.

## Design-partner request

Jinstone is looking for teams in robotics, automotive, intelligent hardware,
edge AI, and private AI with a workload that must stay local because of
privacy, latency, or continuous operation.

For a two-week pilot, the partner provides:

- one non-sensitive workload fixture;
- at least two candidate execution paths;
- one workflow owner who can accept or reject the result.

Jinstone targets a concrete delivery: real execution, an explicit
failure/fallback test, and a before/after decision.

## Twelve-month target

- Local Compute Runtime v1.0 and adapter SDK;
- three classes of execution path;
- at least two external workloads;
- at least two design partners;
- one paid pilot, NRE, or equivalent engineering commitment;
- one whole-system optimization derived from a repeated external bottleneck;
- a Silicon Go/No-Go decision.

The decision rule remains simple:

> Prove that local compute changes one real workload. Then prove that a repeated
> bottleneck deserves custom compute.
