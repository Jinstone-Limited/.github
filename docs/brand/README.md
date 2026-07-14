# Jinstone Visual System 1.0

![Jinstone dark-field campaign master](../../profile/assets/jinstone-hero-generated-v1.png)

This is the public source of truth for Jinstone（径石）identity, campaign
imagery, evidence labels, release graphics, and motion direction. The system is
meant to survive changes in models, boards, foundries, and product form.

## Core idea

**Measure the path. Build the silicon.**

The visual sequence is physical rather than diagrammatic:

```text
unresolved field → selected route → measurement gate → visible result
```

The route is not decoration. It represents a workload path selected by
evidence. The coral gate is a proof boundary. The terminal object must show a
real or explicitly conceptual result, never imply hardware that does not
exist.

## Canonical identity

The existing logo is immutable. AI and drawing scripts must not reconstruct,
clean up, rotate, or reinterpret it.

| Source | Status | Use |
|---|---|---|
| [`jinstone-mark.png`](../../profile/assets/jinstone-mark.png) | Canonical raster mark | Organization avatar and light fields |
| [`jinstone-banner.jpg`](../../profile/assets/jinstone-banner.jpg) | Canonical raster lockup | Reference for the exact mark and wordmark |

Until the original vector artwork is supplied, do not publish a new SVG mark
or reverse lockup. Generated campaign images contain no logo; the exact source
logo is placed separately at publication time.

## Campaign world

![Jinstone light-field campaign master](./assets/jinstone-campaign-light-v1.png)

![Jinstone proof frame](./assets/jinstone-proof-frame-v1.png)

The image world is tactile and industrial: engineered mineral, ceramic,
calibrated metal, physical channels, a selected teal path, and one restrained
coral proof point. It is concept art, not product evidence.

Avoid generic circuit boards, fake die photography, holograms, neural-network
meshes, code screens, server racks, glowing particles, and abstract gradients.

## Color system

| Token | Hex | Function |
|---|---|---|
| Carbon | `#14181C` | Primary technical field |
| Graphite | `#272E34` | Secondary dark surface |
| Paper | `#F3F4F0` | Editorial and ceramic field |
| Route | `#20B8A6` | Selected, measured path |
| Compute | `#4F6FF2` | Secondary software or host path |
| Proof | `#E4614D` | Measurement gate and physical proof |
| Fixture | `#D8A93D` | Simulated or contract-only evidence |

Functional colors identify meaning. They are never atmospheric glow.

## Typography

- Display: **IBM Plex Sans**; system fallback **Bahnschrift / Segoe UI**.
- Body: **IBM Plex Sans**; system fallback **Segoe UI**.
- Technical metadata: **IBM Plex Mono**; system fallback **Consolas**.
- Chinese: **Noto Sans SC**; system fallback **Microsoft YaHei**.

Typography is applied outside generated imagery. Never ask an image model to
render the Jinstone name, logo, metrics, or evidence labels.

## Evidence as identity

Every result is labeled `FIXTURE`, `HOST`, `BOARD`, `FPGA`, or `SILICON`. The
level controls both color and permissible language. Conceptual campaign art is
never evidence.

## Library

- [Asset index](./asset-index.md)
- [Generation prompts and provenance](./generation-prompts.md)
- [Release system](./release-system.md)
- [Motion system](./motion.md)
- [Voice and claims](./voice-and-claims.md)
- [Machine-readable tokens](../../brand/tokens.json)
