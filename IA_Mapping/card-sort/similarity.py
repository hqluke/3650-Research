"""Builds the card sort similarity matrix from raw/card_sort_raw.csv.

Run from this folder: python3 similarity.py
Each cell is how many participants put both cards in the same group (0 to n).
The diagonal (a card with itself) is left blank.
Cards are ordered by average-linkage clustering so cards people grouped
together sit next to each other. Every cell prints its number, so nothing
relies on color. Writes similarity_matrix.svg and similarity_matrix.csv.
"""
import csv
from html import escape
from itertools import combinations

rows = list(csv.DictReader(open("raw/card_sort_raw.csv")))
cards = {int(r["Card_ID"]): r["Card"] for r in rows}
people = sorted({r["Participant_ID"] for r in rows})
group = {(r["Participant_ID"], int(r["Card_ID"])): r["Group_Label"].strip() for r in rows}

ids = sorted(cards)
n_people = len(people)
sim = {(a, b): sum(group[p, a] == group[p, b] for p in people) for a in ids for b in ids}

# Average-linkage clustering, only used to pick the card order.
clusters = [[i] for i in ids]
while len(clusters) > 1:
    def link(pair):
        x, y = pair
        return sum(sim[a, b] for a in x for b in y) / (len(x) * len(y))
    x, y = max(combinations(clusters, 2), key=link)
    clusters.remove(x)
    clusters.remove(y)
    clusters.append(sorted(x + y) if link((x, y)) == n_people else x + y)
order = clusters[0]

with open("similarity_matrix.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Card"] + [f"{i}" for i in order])
    for a in order:
        w.writerow([f"{a}. {cards[a]}"] + [sim[a, b] for b in order])

# Light sequential blue ramp; black text on the light steps, white on the dark one.
# ponytail: ramp has 4 steps, so this only draws up to 3 participants. Add steps if n grows.
FILL = ["#ffffff", "#b7d3f6", "#5598e7", "#1c5cab"]
INK = ["#1a1a1a", "#1a1a1a", "#1a1a1a", "#ffffff"]
C, LEFT, TOP = 34, 300, 60
n = len(order)
W, H = LEFT + n * C + 20, TOP + n * C + 90
out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
       f'font-family="Noto Sans, sans-serif" font-size="13" role="img" '
       f'aria-label="Card sort similarity matrix, {len(people)} participants">',
       f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
for i, a in enumerate(order):
    y = TOP + i * C
    out.append(f'<text x="{LEFT - 8}" y="{y + C / 2 + 4}" text-anchor="end" fill="#1a1a1a">'
               f'{escape(cards[a])} ({a})</text>')
    out.append(f'<text x="{LEFT + i * C + C / 2}" y="{TOP - 10}" text-anchor="middle" '
               f'fill="#555555">{a}</text>')
    for j, b in enumerate(order):
        x = LEFT + j * C
        if a == b:
            continue
        v = sim[a, b]
        out.append(f'<rect x="{x + 1}" y="{y + 1}" width="{C - 2}" height="{C - 2}" rx="3" '
                   f'fill="{FILL[v]}" stroke="#d0d0d0" stroke-width="{1 if v == 0 else 0}"/>')
        out.append(f'<text x="{x + C / 2}" y="{y + C / 2 + 4}" text-anchor="middle" '
                   f'font-size="12" fill="{INK[v]}">{v}</text>')
ly = TOP + n * C + 30
out.append(f'<text x="{LEFT}" y="{ly}" fill="#555555">How many of the {n_people} participants '
           f'put both cards in the same group:</text>')
for v in range(n_people + 1):
    x = LEFT + v * 70
    out.append(f'<rect x="{x}" y="{ly + 10}" width="20" height="20" rx="3" fill="{FILL[v]}" '
               f'stroke="#d0d0d0"/><text x="{x + 26}" y="{ly + 25}" fill="#1a1a1a">{v}</text>')
out.append("</svg>")
open("similarity_matrix.svg", "w").write("\n".join(out))

if __name__ == "__main__":
    assert all(sim[i, i] == n_people for i in ids)
    assert all(sim[a, b] == sim[b, a] for a in ids for b in ids)
    assert sorted(order) == ids
    print("order:", order)
