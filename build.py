"""Wrap src/page.html into a complete document at public/index.html for GitHub Pages."""
import shutil
from pathlib import Path

src = Path(__file__).parent / "src" / "page.html"
head, body = src.read_text(encoding="utf-8").split("<!--HEAD-END-->", 1)

doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta property="og:title" content="Cibin Mathew Simon, technical architect">
<meta property="og:type" content="website">
{head.strip()}
</head>
<body>
{body.strip()}
</body>
</html>
"""
out = Path(__file__).parent / "public" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(doc, encoding="utf-8")
shutil.copy(src.parent / "photo.jpg", out.parent / "photo.jpg")
print(f"wrote {out}")
