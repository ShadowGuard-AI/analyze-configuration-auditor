#!/usr/bin/env python3
"""Auditor banner: the bench at session start, inventory card pinned above it."""
import os, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
random.seed(53)
V = os.environ.get("VARIANT", "")
HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1200, 520
CHAR = (38, 36, 34); GREY = (198, 196, 190); ROSE = (216, 160, 158)
img = Image.new("RGB", (W, H), (208, 206, 200)); d = ImageDraw.Draw(img, "RGBA")
# window at the left, hard light falling from it
d.rectangle([26, 26, 300, 250], fill=(234, 234, 226), outline=CHAR, width=6)
d.line([(163, 26), (163, 250)], fill=CHAR, width=5); d.line([(26, 138), (300, 138)], fill=CHAR, width=5)
for i in range(3):
    d.polygon([(300 + i * 30, 60 + i * 60), (1200, 130 + i * 60), (1200, 190 + i * 60), (300, 130 + i * 60)], fill=(255, 252, 230, 26))
# shelf with turned away jars, wall hook with the older tied roll
d.rectangle([760, 96, 1170, 108], fill=(120, 96, 66))
for jx in (800, 890, 990, 1080):
    d.rounded_rectangle([jx, 38, jx + 52, 96], 8, fill=(170, 168, 160), outline=CHAR, width=2)
d.polygon([(620, 130), (724, 138), (718, 182), (626, 174)], fill=(152, 150, 144), outline=CHAR, width=3)
d.line([(650, 134), (646, 178)], fill=CHAR, width=4)
# inventory card pinned above the bench, the only lettering in the scene
font = ImageFont.truetype(os.path.join(HERE, "fonts", "AtomicAge.ttf"), 25 if V == "1" else 23)
cw = 620 if V == "1" else 580
d.rectangle([600 - cw // 2, 34, 600 + cw // 2, 108], fill=(216, 214, 208), outline=CHAR, width=3)
for yy in (58, 78, 96):
    d.line([(600 - cw // 2 + 14, yy), (600 + cw // 2 - 14, yy)], fill=(160, 158, 152), width=1)
d.text((600, 44), "analyze-configuration-auditor", font=font, fill=CHAR, anchor="ma")
d.ellipse([592, 26, 608, 42], fill=(150, 60, 54), outline=CHAR, width=2)
# bench
d.rectangle([0, 268, W, H], fill=(152, 120, 86))
for _ in range(56):
    y = random.uniform(276, 512); d.line([(0, y), (W, y + random.uniform(-4, 4))], fill=(138, 106, 74), width=2)
# lino block at the left with a transferred drawing, lines only
d.rectangle([52, 300, 330, 440], fill=(174, 172, 166), outline=CHAR, width=3)
for i in range(5):
    d.arc([70 + i * 10, 316 + i * 5, 170 + i * 20, 396 + i * 5], 20, 300, fill=CHAR, width=2)
d.line([(84, 424), (300, 330)], fill=CHAR, width=2)
# gouge roll open across the centre, handles catching the window light
rx, ry, rw, rh = 386, 292, 470, 148
d.rectangle([rx, ry, rx + rw, ry + rh], fill=(180, 178, 172), outline=CHAR, width=4)
for i in range(6):
    x = rx + i * (rw // 5)
    d.line([(x, ry + 8), (x, ry + rh - 8)], fill=CHAR, width=2)
for i in range(5):
    cx = rx + i * 94 + 47
    d.polygon([(cx + 16, ry + 118), (cx + 52, ry + 132), (cx + 18, ry + 130)], fill=(70, 62, 52, 130))  # short shadow toward the block side
    d.rectangle([cx - 12, ry + 34, cx + 12, ry + 104], fill=ROSE, outline=CHAR, width=2)
    d.polygon([(cx - 10, ry + 34), (cx + 10, ry + 34), (cx + 5, ry + 10), (cx - 5, ry + 10)], fill=(216, 216, 210), outline=CHAR, width=2)
# proof sheets stacked at the right, top sheet carrying a fresh print
for k in range(3):
    d.rectangle([906 + k * 7, 306 + k * 7, 1158 + k * 7, 446 + k * 7], fill=(206, 204, 198), outline=(130, 128, 122), width=2)
d.rectangle([920, 320, 1172, 460], fill=(212, 210, 204), outline=CHAR, width=2)
d.ellipse([960, 344, 1060, 424], fill=CHAR)
d.polygon([(1060, 440), (1130, 356), (1160, 440)], fill=CHAR)
for i in range(5):
    d.line([(976 + i * 14, 360 + i * 8), (976 + i * 14, 408 - i * 4)], fill=(212, 210, 204), width=4)
img = img.filter(ImageFilter.GaussianBlur(0.5))
out = os.path.join(HERE, "scratch", f"banner-v{V}.png") if V else os.path.join(HERE, "banner.png")
os.makedirs(os.path.dirname(out), exist_ok=True); img.save(out); print("saved", out)
