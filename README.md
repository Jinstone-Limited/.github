# Jinstone organization profile

Source for the public [Jinstone-Limited](https://github.com/Jinstone-Limited)
organization page and Jinstone Visual System 1.0.

## Structure

- `profile/README.md` — rendered organization homepage.
- `profile/assets/` — canonical identity sources and public homepage graphics.
- `docs/brand/assets/` — generated campaign masters, kept as versioned art.
- `docs/brand/` — identity, release, claim, motion, and generation standards.
- `docs/progress/` — public, evidence-bounded project updates.
- `brand/tokens.json` — machine-readable color, type, and evidence tokens.

The organization page should change only when the long-term thesis changes.
Individual product results belong in release assets and repositories, not in a
new homepage identity every month.

## Publish

Merging `profile/README.md` and its assets into the default branch updates the
public organization profile. Two GitHub surfaces remain settings-controlled:

- Upload `profile/assets/jinstone-mark.png` as the organization avatar.
- Upload `social-preview.png` as the `.github` repository social preview.

Keeping those source files in the repository makes every manual update
reproducible without pretending repository code can change organization
settings.

Generated campaign artwork is never a logo master or product-evidence image.
The existing mark and lockup remain immutable until their original vector
sources are added.
