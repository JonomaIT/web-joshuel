#!/usr/bin/env python3
"""Clean draw.io SVG exports for the site: drop the PNG fallbacks of the HTML labels, the external
"Text is not SVG" link, and the light-dark() colours (always the light value), then report sizes.

    python3 -I svg_clean.py <src-dir> <dst-dir>
"""
import re
import sys
from pathlib import Path

src, dst = Path(sys.argv[1]), Path(sys.argv[2])
dst.mkdir(parents=True, exist_ok=True)
for old in dst.glob("*"):
    old.unlink()
for f in sorted(src.glob("*.svg")):
    t = f.read_text(encoding="utf-8")
    before = len(t)
    t = re.sub(r'<image[^>]*xlink:href="data:image/png;base64,[^"]*"[^>]*/>', "", t)
    t = re.sub(r'<switch><g requiredFeatures="[^"]*"/><a [^>]*>.*?</a></switch>', "", t, flags=re.S)
    t = re.sub(r"light-dark\(\s*([^,()]+(?:\([^()]*\))?)\s*,\s*[^()]+?(?:\([^()]*\))?\s*\)", r"\1", t)
    t = t.replace("color-scheme: light dark;", "")
    t = re.sub(r"<!DOCTYPE[^>]*>", "", t)
    assert "<script" not in t.lower() and "javascript:" not in t.lower(), f.name
    ext = re.findall(r'(?:href|src)="(https?:[^"]+)"', t)
    assert not ext, (f.name, ext[:3])
    (dst / f.name).write_text(t, encoding="utf-8")
    w, h = re.search(r'<svg[^>]*\bwidth="([\d.]+)px"[^>]*\bheight="([\d.]+)px"', t).groups()
    print(f"{f.name}: {before // 1024} KB -> {len(t) // 1024} KB, {w}x{h}, light-dark left: {t.count('light-dark')}")
