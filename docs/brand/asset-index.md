# Asset Index

## Canonical identity

| Asset | Use |
|---|---|
| [`jinstone-mark.png`](../../profile/assets/jinstone-mark.png) | Exact organization mark; do not redraw |
| [`jinstone-banner.jpg`](../../profile/assets/jinstone-banner.jpg) | Exact raster lockup reference; do not redraw |

## Generated campaign masters

| Asset | Role | Evidence status |
|---|---|---|
| [`jinstone-hero-generated-v1.png`](../../profile/assets/jinstone-hero-generated-v1.png) | Dark GitHub hero and campaign key art | Concept only |
| [`jinstone-campaign-light-v1.png`](./assets/jinstone-campaign-light-v1.png) | Light editorial field | Concept only |
| [`jinstone-proof-frame-v1.png`](./assets/jinstone-proof-frame-v1.png) | Release-film proof beat | Concept only |
| [`jinstone-social-preview-v1.png`](./assets/jinstone-social-preview-v1.png) | Source master for the `.github` social preview | Concept only |
| [`social-preview.png`](../../social-preview.png) | Published copy of the social master | Publication asset |

Generated masters are versioned, not overwritten. Their prompts and source
roles are recorded in [generation-prompts.md](./generation-prompts.md).

## System graphics

| Asset | Role |
|---|---|
| [`jinstone-system-path-v1.png`](../../profile/assets/jinstone-system-path-v1.png) | Organization-profile view of the four-stage system |
| [`jinstone-system-path-v1.svg`](../../profile/assets/jinstone-system-path-v1.svg) | Editable source for the system path |
| [`jinstone-evidence-ladder-v1.png`](../../profile/assets/jinstone-evidence-ladder-v1.png) | Organization-profile view of evidence levels |
| [`jinstone-evidence-ladder-v1.svg`](../../profile/assets/jinstone-evidence-ladder-v1.svg) | Editable source for the evidence ladder |

System graphics are deterministic vector artwork built from the visual tokens.
They are distinct from conceptual campaign masters and product evidence.

## Design data

| Asset | Use |
|---|---|
| [`tokens.json`](../../brand/tokens.json) | Color, type, spacing, evidence, and motion tokens |

## GitHub publishing surfaces

| Surface | Source | Activation |
|---|---|---|
| Organization homepage | [`profile/README.md`](../../profile/README.md) | Automatic after merge to the default branch |
| Organization avatar | [`jinstone-mark.png`](../../profile/assets/jinstone-mark.png) | Upload in organization profile settings |
| `.github` social preview | [`social-preview.png`](../../social-preview.png) | Upload in repository settings |

The avatar and social preview are settings-controlled GitHub assets. Updating
their tracked source files does not upload them automatically.
