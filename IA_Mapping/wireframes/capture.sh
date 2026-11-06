#!/usr/bin/env bash
# Regenerates every wireframe export. Needs chrome-devtools-axi and the folder served:
#   python3 -m http.server 8790 --directory IA_Mapping/wireframes
set -euo pipefail
cd "$(dirname "$0")"
B=http://localhost:8790
OUT=$PWD/exports
mkdir -p "$OUT/desktop" "$OUT/phone" "$OUT/annotated"
PAGES=(01-find-a-time 02-no-tee-times 03-sign-in 04-review-and-pay 05-confirmed 06-my-tee-times 07-cancel 08-cancelled 09-rules-and-policies)

open() { chrome-devtools-axi open "$1" >/dev/null; sleep 1; }
shot() { chrome-devtools-axi screenshot "$1" --full-page >/dev/null; }

chrome-devtools-axi resize 1280 900 >/dev/null
for p in "${PAGES[@]}"; do
  open "$B/$p.html"; shot "$OUT/desktop/$p.png"
  open "$B/$p.html?annotate"; shot "$OUT/annotated/$p.png"
done

chrome-devtools-axi resize 390 844 >/dev/null
for p in "${PAGES[@]}"; do
  open "$B/$p.html"; shot "$OUT/phone/$p.png"
done
open "$B/01-find-a-time.html"
chrome-devtools-axi eval "() => { document.querySelector('.menu-toggle').click(); document.querySelector('.filters-toggle').click(); return 1 }" >/dev/null
shot "$OUT/phone/01-find-a-time-menu-and-filters-open.png"

# Full-page shots pad the bottom with blank viewport, so trim it.
python3 - "$OUT" <<'EOF'
import sys
from pathlib import Path
from PIL import Image, ImageChops
for f in Path(sys.argv[1]).rglob("*.png"):
    im = Image.open(f).convert("RGB")
    box = ImageChops.difference(im, Image.new("RGB", im.size, "white")).getbbox()
    if box:
        im.crop((0, 0, im.width, min(im.height, box[3] + 24))).save(f)
EOF
echo "Exports written to $OUT"
