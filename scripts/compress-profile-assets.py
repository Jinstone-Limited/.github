from pathlib import Path
from PIL import Image

assets = Path(__file__).resolve().parents[1] / "profile" / "assets"


def resize_keep_aspect(img: Image.Image, *, height: int | None = None, width: int | None = None) -> Image.Image:
    w, h = img.size
    if height is not None:
        return img.resize((int(w * height / h), height), Image.LANCZOS)
    if width is not None:
        return img.resize((width, int(h * width / w)), Image.LANCZOS)
    raise ValueError("pass height or width")


banner_src = assets / "jinstone-banner.jpg"
if not (assets / "_orig-banner.png").exists():
    # one-time: recover from git if needed; skip if jpg already ok
    pass

# Rebuild banner from png if present in vault attachments - use existing jpg if banner png gone
png = list(assets.glob("jinstone-banner.png"))
if png:
    img = resize_keep_aspect(Image.open(png[0]).convert("RGB"), width=680)
    img.save(assets / "jinstone-banner.jpg", format="JPEG", quality=80, optimize=True, progressive=True)

orig_mark = assets / "_orig-mark.png"
if orig_mark.exists():
    mark = resize_keep_aspect(Image.open(orig_mark).convert("RGBA"), height=112)
    mark.save(assets / "jinstone-mark.png", format="PNG", optimize=True)
    print("jinstone-mark.png", mark.size, (assets / "jinstone-mark.png").stat().st_size)

if (assets / "jinstone-banner.jpg").exists():
    im = Image.open(assets / "jinstone-banner.jpg")
    print("jinstone-banner.jpg", im.size, (assets / "jinstone-banner.jpg").stat().st_size)
