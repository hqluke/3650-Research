## Card Sort Protocol

### Goal

Find out how golfers group the things they do when booking at Davis Park and Valley View. ForeUp puts the booking class first, before you see any times (H-08), and that's what tripped up both Phase 1 participants. I want to know where golfers would put each piece before I lock in a sitemap.

### Method

This is an open card sort. Participants make their own groups and name them, so the group names are their words, not mine or ForeUp's. The cards are things golfers do or need to know, written in plain words. They don't use ForeUp's labels, because a card that says "18 Hole Groups" would just teach them ForeUp's model.

Each session is about 15 minutes, one person at a time.

### Participants

Participants are called C1, C2, and C3 so they don't get mixed up with P1 and P2 from Phase 1 or P01-P12 from Lab 04. If someone from Phase 1 does the sort too, I'll note it next to their C number, since I explained the booking classes to them afterward.

| ID | Has booked a tee time online | Has booked on ForeUp at Davis Park or Valley View | Date | Time (MST) |
| --- | --- | --- | --- | --- |
| C1 | Yes | No | 2026-11-05 | 9:55-10:05 AM (10 min) |
| C2 | No | No | 2026-11-05 | 10:12-10:24 AM (12 min) |
| C3 | No | No | 2026-11-05 | 10:47-11:05 AM (18 min) |

### The Deck

| # | Card |
| --- | --- |
| 1 | Pick a date |
| 2 | Choose 9 or 18 holes |
| 3 | Choose how many players |
| 4 | Choose morning, afternoon, or evening |
| 5 | Pick Davis Park or Valley View |
| 6 | See open tee times at both courses |
| 7 | Book as a single golfer |
| 8 | Choose a cart or walking |
| 9 | Pay for your group |
| 10 | Log in or create an account |
| 11 | Use a season pass |
| 12 | See your upcoming tee times |
| 13 | Cancel a tee time |
| 14 | Read the cancellation policy |
| 15 | See when new days open for booking |
| 16 | See why there are no tee times |
| 17 | Find the last tee time before sunset |
| 18 | Get your confirmation email |

### Setup

The sort runs in Trello. Each person gets a fresh copy of a board with a list called "C1 Cards" (or C2, C3) holding all 18, plus five empty lists named "List item 1 (click to rename)" through "List item 5." They drag cards into the empty lists and rename them, and they can add more lists if they need them. `raw/before.webp` shows the board at the start. When they're done I take a screenshot of the board.

I planned to export each board as JSON too, but I couldn't get the export to work, so the screenshots are the raw data. I typed each one into the CSV by hand and checked it against the screenshot. The board is named "4850 Phase 2" in the screenshots. That's a typo, I mixed up my class numbers, and it's the same board for this class.

### Script

> Thanks for helping. This is for my HCI class. I'm going to give you 18 cards on a Trello board, and each one is something you might do or want to know when you book a tee time. Put them into groups that make sense to you, and give each group a name. There's no right answer, and you can make as many or as few groups as you want. If a card doesn't fit anywhere, or you don't know what it means, put it in its own list and tell me. Please think out loud while you go. You can stop at any time, and your name won't be in anything I turn in.

After they're done:

1. "Walk me through your groups. Why do these go together?"
2. "Which card was the hardest to place? Why?"
3. "If this was a website, which group would you look at first?"

### What I Record

- A screenshot of the finished board, saved in `raw/` as `c1.webp`, `c2.webp`, and `c3.webp`.
- One row per card in `raw/card_sort_raw.csv`, with the group name in their words. I capitalized the names so they're consistent (C2 wrote "Rules and confirmation"), but didn't change any wording. Empty lists aren't in the CSV, like the "booking" list C2 made and never used.
- Screening answers, quotes word for word (especially for cards they moved more than once or couldn't place), and follow-up answers in `raw/session_notes.md`.
