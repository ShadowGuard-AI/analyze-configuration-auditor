#!/usr/bin/env python3
"""Auditor logo: the gouge roll from above, five blades up, one cut strip below. Name in Atomic Age."""
import os
from PIL import Image, ImageDraw, ImageFont
V = os.environ.get("VARIANT", "")
HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 960, 640
CHAR = (38, 36, 34); GREY = (198, 196, 190); ROSE = (216, 160, 158); PAPER = (210, 208, 202)
img = Image.new("RGB", (W, H), PAPER); d = ImageDraw.Draw(img)
# canvas roll laid open, stitched pockets in a row
rx, ry, rw, rh = 90, 70, 780, 300
d.rectangle([rx, ry, rx + rw, ry + rh], fill=GREY, outline=CHAR, width=6)
for i in range(6):
    x = rx + i * (rw // 5)
    d.line([(x, ry + 10), (x, ry + rh - 10)], fill=CHAR, width=3)
    for yy in range(ry + 18, ry + rh - 8, 14):
        d.line([(x - 5, yy), (x + 5, yy)], fill=(110, 108, 102), width=2)
def blade(cx, top, kind):
    if kind == "V":
        d.polygon([(cx - 20, top + 44), (cx + 20, top + 44), (cx, top)], fill=(224, 224, 218), outline=CHAR, width=3)
    elif kind == "U":
        d.pieslice([cx - 21, top, cx + 21, top + 52], 180, 360, fill=(224, 224, 218), outline=CHAR, width=3)
        d.rectangle([cx - 21, top + 24, cx + 21, top + 46], fill=(224, 224, 218), outline=CHAR, width=3)
    elif kind == "flat":
        d.rectangle([cx - 22, top + 4, cx + 22, top + 44], fill=(224, 224, 218), outline=CHAR, width=3)
    elif kind == "scoop":
        d.ellipse([cx - 17, top + 2, cx + 17, top + 44], fill=(224, 224, 218), outline=CHAR, width=3)
        d.ellipse([cx - 8, top + 10, cx + 8, top + 34], outline=CHAR, width=2)
    else:
        d.polygon([(cx - 18, top + 44), (cx + 18, top + 44), (cx + 4, top)], fill=(224, 224, 218), outline=CHAR, width=3)
kinds = ["V", "U", "flat", "scoop", "knife"]
for i, kind in enumerate(kinds):
    cx = rx + i * 156 + 78
    blade(cx, ry + 26, kind)
    d.rectangle([cx - 21, ry + 84, cx + 21, ry + 236], fill=ROSE, outline=CHAR, width=3)
    d.ellipse([cx - 12, ry + 120, cx + 4, ry + 190], fill=(228, 182, 178))  # worn lighter where thumbs rest
# one finished cut strip of lino apart from the set
sy = 404 if V != "1" else 388
d.rectangle([150, sy, 810, sy + 52], fill=CHAR)
for i in range(4):
    yy = sy + 10 + i * 9
    d.line([(170, yy), (790 - i * 30, yy)], fill=GREY, width=3)
d.arc([700, sy + 6, 780, sy + 40], 30, 300, fill=GREY, width=3)
# ruled line above the name, none below it
d.line([(90, 492), (870, 492)], fill=CHAR, width=3)
font = ImageFont.truetype(os.path.join(HERE, "fonts", "AtomicAge.ttf"), 37)
d.text((480, 512), "analyze-configuration-auditor", font=font, fill=CHAR, anchor="ma")
out = os.path.join(HERE, "scratch", f"logo-v{V}.png") if V else os.path.join(HERE, "logo.png")
os.makedirs(os.path.dirname(out), exist_ok=True); img.save(out); print("saved", out)
if not V:
    img.resize((96, 64)).save(os.path.join(HERE, "scratch", "logo64-ship.png"))
