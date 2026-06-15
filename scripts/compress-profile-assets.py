from pathlib import Path
from PIL import Image

assets = Path(__file__).resolve().parents[1] / "profile" / "assets"

banner_src = assets / "jinstone-banner.png"
img = Image.open(banner_src).convert("RGB")
w = 680
h = int(img.height * w / img.width)
img = img.resize((w, h), Image.LANCZOS)
banner = assets / "jinstone-banner.jpg"
img.save(banner, format="JPEG", quality=80, optimize=True, progressive=True)

mark = Image.open(assets / "jinstone-mark.png").convert("RGBA")
mark = mark.resize((128, 128), Image.LANCZOS)
mark.save(assets / "jinstone-mark.png", format="PNG", optimize=True)

for p in (banner, assets / "jinstone-mark.png"):
    print(p.name, p.stat().st_size)
