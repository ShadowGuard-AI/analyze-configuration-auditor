#!/usr/bin/env python3
"""Auditor intro: the bench before work, one pocket empty. Scenery only, no text."""
import os, random
from PIL import Image, ImageDraw, ImageFilter
random.seed(41)
V = os.environ.get("VARIANT", "")
HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1200, 520
CHAR = (38, 36, 34); GREY = (198, 196, 190); ROSE = (216, 160, 158)
img = Image.new("RGB", (W, H), (206, 204, 198)); d = ImageDraw.Draw(img, "RGBA")
# studio window, pale wash, window frame shadows in charcoal bands on the wall
d.rectangle([60, 30, 460, 240], fill=(232, 232, 224))
d.rectangle([60, 30, 460, 240], outline=CHAR, width=6)
d.line([(260, 30), (260, 240)], fill=CHAR, width=5); d.line([(60, 135), (460, 135)], fill=CHAR, width=5)
for i in range(3):
    d.polygon([(520 + i * 190, 0), (640 + i * 190, 0), (430 + i * 190, 250), (330 + i * 190, 250)], fill=(58, 56, 54, 44))
# shelf with jars, labels turned away; older tied roll on its wall hook
d.rectangle([640, 120, 1150, 132], fill=(120, 96, 66))
for jx in (690, 790, 900, 1010):
    d.rounded_rectangle([jx, 58, jx + 56, 120], 8, fill=(168, 166, 158), outline=CHAR, width=2)
    d.rectangle([jx + 14, 44, jx + 42, 60], fill=(140, 138, 130), outline=CHAR, width=2)
d.polygon([(1010, 168), (1130, 178), (1124, 226), (1016, 216)], fill=(150, 148, 142), outline=CHAR, width=3)
d.line([(1040, 172), (1036, 220)], fill=CHAR, width=4); d.line([(1070, 152), (1070, 168)], fill=CHAR, width=3)
# bench surface with wood grain and old cut scars
d.rectangle([0, 250, W, H], fill=(152, 120, 86))
for _ in range(70):
    y = random.uniform(258, 512); d.line([(0, y), (W, y + random.uniform(-4, 4))], fill=(138, 106, 74), width=2)
for _ in range(26):
    x, y = random.uniform(0, W), random.uniform(280, 500)
    d.line([(x, y), (x + random.uniform(14, 44), y + random.uniform(-3, 3))], fill=(104, 80, 54), width=2)
# open gouge roll across the middle: five pockets, four tools standing, one pocket empty
rx, ry, rw, rh = 300, 268, 620, 128
d.rectangle([rx, ry, rx + rw, ry + rh], fill=(178, 176, 170), outline=CHAR, width=4)
for i in range(6):
    x = rx + i * (rw // 5)
    d.line([(x, ry + 8), (x, ry + rh - 8)], fill=CHAR, width=2)
    for yy in range(ry + 14, ry + rh - 6, 12):
        d.line([(x - 4, yy), (x + 4, yy)], fill=(110, 108, 102), width=1)
empty = 2
for i in range(5):
    if i == empty:
        d.rectangle([rx + i * 124 + 18, ry + 26, rx + i * 124 + 106, ry + rh - 14], outline=(120, 118, 112), width=2)
        continue
    cx = rx + i * 124 + 62
    d.rectangle([cx - 13, ry + 30, cx + 13, ry + 96], fill=ROSE, outline=CHAR, width=2)
    d.polygon([(cx - 11, ry + 30), (cx + 11, ry + 30), (cx + 6, ry + 6), (cx - 6, ry + 6)], fill=(214, 214, 208), outline=CHAR, width=2)
# lino block beyond the roll, transferred drawing as abstract lines only
d.rectangle([950, 276, 1164, 388], fill=(172, 170, 164), outline=CHAR, width=3)
for i in range(5):
    d.arc([966 + i * 8, 292 + i * 4, 1050 + i * 16, 360 + i * 4], 20, 300, fill=CHAR, width=2)
d.line([(980, 372), (1140, 300)], fill=CHAR, width=2)
# the one tool out at work, on its side in the lower right, plus curled shavings
gx, gy = (880, 452) if V != "1" else (880, 428)
d.rounded_rectangle([gx, gy, gx + 190, gy + 34], 15, fill=ROSE, outline=CHAR, width=3)
d.polygon([(gx + 190, gy + 4), (gx + 252, gy + 12), (gx + 190, gy + 30)], fill=(222, 222, 216), outline=CHAR, width=2)
d.line([(gx + 194, gy + 8), (gx + 244, gy + 13)], fill=(255, 255, 250), width=3)
for i in range(7):
    sx, sy = 700 + i * 22, 470 + (i % 3) * 12
    d.arc([sx, sy, sx + 26, sy + 16], 40, 320, fill=(120, 118, 112), width=3)
img = img.filter(ImageFilter.GaussianBlur(0.5))
out = os.path.join(HERE, "scratch", f"intro-v{V}.png") if V else os.path.join(HERE, "intro-banner.png")
os.makedirs(os.path.dirname(out), exist_ok=True); img.save(out); print("saved", out)
