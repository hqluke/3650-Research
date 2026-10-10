## WCAG 2.1 AA Accessibility Audit

### What I Tested and How

I tested Valley View's ForeUp booking pages (`foreupsoftware.com/index.php/booking/19501/1759`) against WCAG 2.1 Level AA (Kirkpatrick et al., 2018) on October 9, 2026, in Chrome on Linux. Davis Park uses the same ForeUp template, so the results should be the same there, but I only measured Valley View. I tested at full desktop width (1492 px) and at a narrow width (954 px) that switches to the phone layout.

| Method | Tool | What it covers |
| --- | --- | --- |
| Automated scan | `axe-core` 4.10.2 (the engine behind axe DevTools), run on the tee time list (Booking as 9 Hole Groups, Saturday Oct 10) | Everything a machine can check, tagged by WCAG criterion |
| Keyboard only | Tab, Shift+Tab, and Enter, no mouse, at both widths | SC 2.1.1, 2.4.3, 2.4.7 |
| Structure and names | DevTools console scripts and Chrome's accessibility tree | SC 1.3.1, 2.4.6, 4.1.2, 4.1.3, landmarks and headings |
| Contrast | Text and background colors from the computed CSS, run through the WCAG formula | SC 1.4.3 |

The axe scan didn't catch the worst problem on the site. Not being able to pick a tee time with a keyboard only showed up when I tabbed through the page.

### Results by Success Criterion

| SC | Level | Name | Result | Finding |
| --- | --- | --- | --- | --- |
| 2.1.1 | A | Keyboard | **Fail** | A-01, A-02, A-03 |
| 4.1.2 | A | Name, Role, Value | **Fail** | A-02, A-04, A-09 |
| 2.4.3 | A | Focus Order | **Fail** | A-05, A-09 |
| 1.3.1 | A | Info and Relationships | **Fail** | A-08 |
| 2.4.1 | A | Bypass Blocks | **Fail** (low impact) | A-08 |
| 1.4.4 | AA | Resize Text | **Fail** | A-06 |
| 4.1.3 | AA | Status Messages | **Fail** | A-07 |
| 1.4.3 | AA | Contrast (Minimum) | **Fail** | A-10 |
| 1.3.5 | AA | Identify Input Purpose | **Fail** | A-09 |
| 2.4.6 | AA | Headings and Labels | **Fail** | A-11 |
| 2.4.7 | AA | Focus Visible | Pass, on everything that can actually get focus | A-12 |
| 3.1.1 | A | Language of Page | Pass (`<html lang="en">`) | |
| 2.4.2 | A | Page Titled | Pass, but the title never changes between steps | |
| 3.3.2 | A | Labels or Instructions | Pass for the login form, which has real `<label>`s | |

### Automated Scan (axe-core)

| Rule | Impact | WCAG | What it found |
| --- | --- | --- | --- |
| `meta-viewport` | Critical | 1.4.4 (AA) | `<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">` turns off pinch-to-zoom |
| `select-name` | Critical | 4.1.2 (A) | The course dropdown (`#schedule_select`) and the date dropdown (`#date-menu`) have no accessible name |
| `landmark-one-main` | Moderate | Best practice | No `<main>` landmark |
| `page-has-heading-one` | Moderate | Best practice | No `<h1>` anywhere |
| `region` | Moderate | Best practice | 7 blocks of content outside any landmark |
| `color-contrast` | Needs review | 1.4.3 | 93 elements axe couldn't decide on because they sit on gradient backgrounds. I measured the important ones by hand (A-10) |

axe also passed 23 rules. I didn't run WAVE.

### A-01: You Can't Pick a Tee Time With a Keyboard

SC 2.1.1 Keyboard, Level A. Fails, and it blocks the whole task.

Each tee time is a `<div class="time time-tile-ob-no-details">` with a pointer cursor but no `tabindex` and no role, so it only works with a mouse or a tap. Tab never lands on one. These are all the Tab stops on the tee time page at the narrow width, in order:

| Tab | Lands on |
| --- | --- |
| 1 | Menu button ("Toggle navigation") |
| 2 | "Valley View Golf Course" home link |
| 3 | Course dropdown |
| 4 | "<" (previous day) |
| 5 | Date dropdown |
| 6 | ">" (next day) |
| 7 | "FOREUP TERMS & CONDITIONS" |
| 8 | "View Booking Rules" |
| 9 | "Change" |
| 10 | Leaves the page and starts over at the top |

None of the nine stops is a tee time. Chrome's accessibility tree doesn't list the tee times as interactive either, so a screen reader user would hear the text but have nothing to activate. Anyone who uses a keyboard, a switch, or a screen reader can't book online at either county course. Evidence: `screenshots/kb-03-mobile-tab-skips-filters.jpg`.

The fix is to make each tee time a real `<button>` (or `<a href>`) with a name that covers the whole card, like `aria-label="2:10 PM, Back 10, 9 holes, up to 2 players, $18"`.

### A-02: The Filter Buttons Can't Be Reached or Read

SC 2.1.1 Keyboard and 4.1.2 Name, Role, Value, both Level A. Fails.

Morning, Midday, Evening, Anytime, players 1-4 and Any, and 9 Holes / 18 Holes / Both are all `<a class="ob-filters-btn">` with no `href`. An `<a>` without an `href` can't get focus, so Tab skips all 12 of them. The selected one is only shown by a dark blue fill and an `active` CSS class. There's no `aria-pressed` or `aria-checked`, so a screen reader can't tell which filter is on.

The fix is `<button type="button" aria-pressed="true|false">` for each one, with each set wrapped in a `role="group"` labeled like `aria-label="Number of players"`.

### A-03: The Desktop Calendar Isn't Keyboard Accessible

SC 2.1.1 Keyboard, Level A. Fails at desktop width.

At desktop width, the date is picked from a calendar made of plain `<td class="day">` cells with no `tabindex`. The whole tee time page at that width has only 7 Tab stops (4 header links, the course dropdown, the terms link, and Change), and none of them picks a date. The narrow layout swaps in a real date `<select>` with "<" and ">" buttons that work with a keyboard. So a keyboard user can change the date in a phone-sized window but not on a laptop.

The fix is to use the same `<select>` (or a proper date grid with arrow key support) at every width.

### A-04: The Dropdowns Have No Names

SC 4.1.2 Name, Role, Value, Level A. Fails (axe `select-name`, critical).

The course dropdown and the date dropdown have no `<label>`, `aria-label`, or `aria-labelledby`. A screen reader announces them as "combo box, Valley View Golf Course" and "combo box, Saturday, Oct 10th" without saying what they're for.

The fix is `<label for="date-menu">Date</label>`, or `aria-label="Date"` and `aria-label="Course"`.

### A-05: Focus Gets Dropped After Every Choice

SC 2.4.3 Focus Order, Level A. Fails.

Pressing Enter on "9 Hole Groups" loads the tee times and sends focus back to `<body>`, the very top of the page (`screenshots/teesheet-desktop-9-groups.jpg`). Pressing Enter on "Change" goes back to the class picker and does the same thing (`screenshots/change-returns-to-class-picker.jpg`). A keyboard user has to tab back through the header after every choice, and a screen reader user isn't told anything happened.

The fix is to move focus to a heading at the top of the results after they load, like `<h2 tabindex="-1">Tee times for Saturday, Oct 10</h2>`.

### A-06: Pinch-to-Zoom Is Turned Off

SC 1.4.4 Resize Text, Level AA. Fails (axe `meta-viewport`, critical).

The viewport tag has `maximum-scale=1, user-scalable=no`, so on a phone you can't pinch to zoom in on the tee times. The prices and side names on each card are 12.5 px. P1 did the whole session on a phone, and I'd guess older golfers are the ones most likely to want to zoom.

The fix is to remove `maximum-scale=1, user-scalable=no`.

### A-07: Result Changes Are Never Announced

SC 4.1.3 Status Messages, Level AA. Fails.

There's no `aria-live` region or `role="status"` anywhere on the page. When you change a filter or a date, the list updates, or turns into "There are no tee times available with your current search criteria," and a screen reader says nothing (`screenshots/empty-state-18-groups-both.jpg`). That's the same message both participants misread (H-02 in `heuristic-evaluation.md`), and a blind user wouldn't even know it appeared.

The fix is a short summary in a `role="status"` region, like "12 tee times found" or "No 18 hole times, because you're booking as 9 Hole Groups."

### A-08: No Headings or Landmarks

SC 1.3.1 Info and Relationships and 2.4.1 Bypass Blocks, both Level A. Fails.

There's no `<h1>` and no `<main>`. On the class picker, the only heading is an `<h3>` that wraps the entire welcome message, bullets and all. On the tee time page, the only heading is an `<h4>` reading "Booking Rules," and the tee time list, which is the main content, has no heading at all. There's no skip link either. The header is short, so that part is low impact, but with no headings or `<main>`, a screen reader user has no shortcut to the results.

The fix is one `<h1>` with the course name, a `<main>` around the booking area, and `<h2>`s for "Tee times" and "Booking rules."

### A-09: The Log In Popup

SC 4.1.2 and 2.4.3 (Level A), and 1.3.5 Identify Input Purpose (Level AA). Fails.

Going to the plain booking address opens a Log In/Register popup (`screenshots/login-modal-on-landing.jpg`). It has `role="dialog"` but no `aria-labelledby` or `aria-modal`, so it has no name and a screen reader can still wander behind it. Focus stays on `<body>` instead of moving into the popup. The email and password fields have proper `<label>`s but no `autocomplete="email"` or `autocomplete="current-password"`, which matters more than usual here, since ForeUp makes you create a separate account at every course.

### A-10: Contrast

SC 1.4.3 Contrast (Minimum), Level AA. Fails on two elements.

Normal text needs 4.5:1. Large text (24 px, or about 18.66 px bold) needs 3:1.

| Element | Colors | Size | Ratio | Result |
| --- | --- | --- | --- | --- |
| Hole count badge on every tee time ("9" or "18") | `#f0f0f1` on `#7a7575` | 15 px regular | **3.98:1** | **Fail** |
| Site title in the header | `#777777` on a `#ffffff` to `#f8f8f8` gradient | 18 px regular | **4.48 to 4.22:1** | **Fail** |
| Terms and Booking Rules links | `#3174ad` on `#ffffff` | 18 px bold | 4.96:1 | Pass |
| Filter button text | `#434d56` on `#ffffff` | 12 px | 8.63:1 | Pass |
| Selected filter | `#ffffff` on `#16487c` | 12 px | 9.32:1 | Pass |
| "9 Hole Groups" badge | `#ffffff` on `#01548a` | 12.6 px bold | 7.97:1 | Pass |
| Class buttons (lightest point of the gradient) | `#ffffff` on `#2d6ca2` | 14 px | 5.56:1 | Pass |
| Tee time, side, and price text | `#1f2b36` / `#333333` on `#f9f9f9` | 12.5 px and up | 12.0 to 13.7:1 | Pass |
| Highlighted booking rules | `#000000` on `#ffff00` | 12 px bold | 19.56:1 | Pass |

The hole count badge is the one that matters, since it's the only thing on a tee time that says whether it's 9 or 18 holes, and that's exactly what both participants got confused about. Darkening its background to `#5f5a5a` would raise it to 5.95:1.

### A-11: Buttons Named "<" and ">"

SC 2.4.6 Headings and Labels, Level AA. Fails.

The previous and next day buttons in the narrow layout are named "<" and ">", which a screen reader reads as "less than, button" and "greater than, button." The names don't say what the buttons do.

The fix is `aria-label="Previous day"` and `aria-label="Next day"`.

### A-12: Focus Visible Mostly Passes

SC 2.4.7 Focus Visible, Level AA. Passes.

Everything that can get keyboard focus shows it. The header links get a dark box (`screenshots/kb-01-focus-nav-link.jpg`), the class buttons get the browser's default ring (`screenshots/kb-02-focus-class-button.png`), and the dropdowns and Change button get a ring too. The class buttons only pass because of the white inner line in Chrome's default ring, since the dark outer line is just 2.04:1 against the blue button. It doesn't count for much, though, when the tee times, filters, and calendar days can't get focus in the first place (A-01 to A-03).

### Where the Accessibility and Heuristic Findings Overlap

| Accessibility failure | Heuristic finding | Who else it affects |
| --- | --- | --- |
| A-07 Results update silently | H-02 Same empty message for three problems | Everyone who misreads the empty list, which was both participants |
| A-01 to A-03 Keyboard can't reach the controls | H-03 and H-10 Efficiency | People who'd rather tab and type |
| A-06 Zoom turned off | H-13 Small, crowded text | Anyone on a phone outdoors, and older eyes |
| A-10 Hole badge contrast | H-01 Holes buttons vs booking class | Everyone trying to tell 9 hole times from 18 |
| A-05 Focus dropped | H-09 Change sends you back to the class picker | Anyone who loses their place |

### Why This Matters Here

Davis County is a local government, so ADA Title II applies. The DOJ's 2024 rule requires WCAG 2.1 AA for web content a government provides, including through "contractual, licensing, or other arrangements," which covers a vendor like ForeUp (U.S. Department of Justice, 2024). The county's deadline is April 26, 2027 (Rivenburgh, 2026), and every Level A failure above would need to be fixed by then.

### Limitations

- I didn't test the site with a real screen reader. I used Chrome's accessibility tree instead, which shows what a screen reader gets but not how it sounds.
- I didn't run WAVE, only `axe-core`.
- I only measured Valley View. Davis Park uses the same template, but I didn't check it separately.
- I didn't go past checkout, so the payment form isn't covered.

### References

Kirkpatrick, A., O Connor, J., Campbell, A., & Cooper, M. (Eds.). (2018). *Web content accessibility guidelines (WCAG) 2.1*. World Wide Web Consortium. https://www.w3.org/TR/WCAG21/

Rivenburgh, K. (2026, April 17). *DOJ extends ADA Title II web compliance deadline 1 year*. Accessible.org. https://accessible.org/news/doj-extends-ada-title-ii-web-compliance-deadline/

U.S. Department of Justice. (2024). *Nondiscrimination on the basis of disability; Accessibility of web information and services of state and local government entities* (89 Fed. Reg. 31320). https://www.federalregister.gov/d/2024-07758
