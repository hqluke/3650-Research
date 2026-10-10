"""Draws numbered callout boxes on the Phase 1 screenshots.

Run from this folder: python3 annotate.py
Boxes are pink with a white edge so they show on light and dark pages, and
each image gets a light margin so badges can sit outside the content.
Every number is explained in the report text, so nothing relies on color.
"""
from PIL import Image, ImageDraw, ImageFont

BOLD = "/usr/share/fonts/noto/NotoSans-Bold.ttf"
FONT = ImageFont.truetype(BOLD, 22)
SMALL = ImageFont.truetype(BOLD, 20)
PINK = (230, 0, 115)  # white text on this is 4.55:1
WHITE = (255, 255, 255)
MARGIN_BG = (233, 233, 236)
M = 40  # margin added on every side
PAD = 6  # space between the content and the box


def with_margin(src):
    im = Image.open(src).convert("RGB")
    out = Image.new("RGB", (im.width + 2 * M, im.height + 2 * M), MARGIN_BG)
    out.paste(im, (M, M))
    return out


def box(d, x0, y0, x1, y1):
    d.rectangle([x0 - 2, y0 - 2, x1 + 2, y1 + 2], outline=WHITE, width=8)
    d.rectangle([x0, y0, x1, y1], outline=PINK, width=4)


def badge(d, x, y, n):
    r = 17
    d.ellipse([x - r - 3, y - r - 3, x + r + 3, y + r + 3], fill=WHITE)
    d.ellipse([x - r, y - r, x + r, y + r], fill=PINK)
    d.text((x, y), str(n), font=FONT, fill=WHITE, anchor="mm")


def label(d, x, y, text):
    w = d.textlength(text, font=SMALL)
    d.rectangle([x - 3, y - 3, x + w + 15, y + 31], fill=WHITE)
    d.rectangle([x, y, x + w + 12, y + 28], fill=PINK)
    d.text((x + 6, y + 14), text, font=SMALL, fill=WHITE, anchor="lm")


def annotate(src, dst, marks):
    """marks: (x0, y0, x1, y1) in original image pixels, optionally with a
    5th item (bx, by) to place the badge somewhere other than the top-left."""
    im = with_margin(src)
    d = ImageDraw.Draw(im)
    placed = []
    for mark in marks:
        x0, y0, x1, y1 = (v + M for v in mark[:4])
        x0, y0, x1, y1 = x0 - PAD, y0 - PAD, x1 + PAD, y1 + PAD
        box(d, x0, y0, x1, y1)
        if len(mark) > 4:
            placed.append((mark[4][0] + M, mark[4][1] + M))
        else:
            placed.append((x0 - 24, (y0 + y1) // 2))
    for n, (bx, by) in enumerate(placed, start=1):
        badge(d, bx, by, n)
    im.save(dst)
    print("wrote", dst)


FIGURES = {
    # 1 booking class, 2 holes button, 3 empty message
    "class-switch-2-18-groups-9-holes-empty.png": ("annotated/fig-class-trap.png", [
        (272, 16, 512, 50),
        (10, 434, 90, 468),
        (340, 160, 970, 290),
    ]),
    # 1 one-option course dropdown, 2 calendar, 3 filters, 4 booking class,
    # 5 hole badge, 6 rules text
    "teesheet-desktop-9-groups.jpg": ("annotated/fig-teesheet.png", [
        (296, 52, 502, 79),
        (296, 88, 502, 274),
        (296, 282, 502, 442),
        (522, 54, 722, 80, (752, 67)),
        (523, 92, 553, 170, (585, 131)),
        (296, 452, 502, 805),
    ]),
    # 1 welcome text, 2 underlined text that isn't a link, 3 class buttons
    "class-picker.jpg": ("annotated/fig-class-picker.png", [
        (318, 80, 1082, 316),
        (964, 176, 1076, 197, (1110, 186)),
        (594, 350, 886, 532),
    ]),
}


def keyboard_figure():
    """Tab order: badges 1-9 on each Tab stop, boxes on what Tab skips."""
    im = with_margin("kb-03-mobile-tab-skips-filters.jpg")
    d = ImageDraw.Draw(im)
    for x0, y0, x1, y1 in [(106, 148, 834, 362), (106, 500, 834, 870)]:
        box(d, x0 + M - PAD, y0 + M - PAD, x1 + M + PAD, y1 + M + PAD)
    label(d, 600 + M, 236 + M, "Skipped by Tab")
    label(d, 560 + M, 600 + M, "Never reached by Tab")
    stops = [(752, 25), (86, 25), (86, 84), (150, 127), (262, 121),
             (852, 127), (86, 385), (86, 418), (386, 470)]
    for n, (x, y) in enumerate(stops, start=1):
        badge(d, x + M, y + M, n)
    im.save("annotated/fig-keyboard.png")
    print("wrote annotated/fig-keyboard.png")


if __name__ == "__main__":
    for src, (dst, marks) in FIGURES.items():
        annotate(src, dst, marks)
    keyboard_figure()
