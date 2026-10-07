## WCAG 2.1 AA - Accessibility Audit Reference

### What WCAG 2.1 AA Means

WCAG (Web Content Accessibility Guidelines) is the W3C's standard for making web content usable for people with disabilities, IE blind and low vision, deaf and hard of hearing, motor, and cognitive. 2.1 is the version, and it came out in June 2018. It kept everything from WCAG 2.0 (2008) and added 17 new criteria, mostly for mobile, low vision, and cognitive disabilities. WCAG 2.2 came out in October 2023 and is backward compatible, but this assignment audits against 2.1.

It's split into layers:

| Layer | Count in 2.1 | Example |
| --- | --- | --- |
| Principles | 4 | 1 Perceivable |
| Guidelines | 13 | 1.4 Distinguishable |
| Success criteria (SC) | 78 | 1.4.3 Contrast (Minimum) |

The four principles spell POUR: Perceivable (users can sense it), Operable (they can work it), Understandable (they can make sense of it), and Robust (it works with assistive technology).

#### Reading an SC Number

`SC 1.4.3` means Principle 1 (Perceivable), Guideline 4 (Distinguishable), criterion 3 (Contrast Minimum). Every SC is a pass/fail statement you can test, which is the big difference from Nielsen's heuristics.

#### Conformance Levels

| Level | Criteria in 2.1 | What it means |
| --- | --- | --- |
| A | 30 | The bare minimum. Failing one usually blocks some users completely |
| AA | 20 more | The usual target. "AA conformance" means passing all 50 A and AA criteria |
| AAA | 28 more | The highest level. The W3C doesn't recommend requiring it for whole sites since some content can't meet all of it |

#### Why AA Matters

AA is the level the law points to.

- ADA Title II covers state and local governments. The DOJ's 2024 rule made WCAG 2.1 AA the required standard for their websites and mobile apps, and that includes content they provide "through contractual, licensing, or other arrangements" (U.S. Department of Justice, 2024). So a city or county service still counts even if a private vendor built it. In April 2026 an interim final rule pushed the deadlines back a year, to April 26, 2027 for entities serving 50,000+ people and April 26, 2028 for smaller ones and special districts. The standard itself didn't change (Rivenburgh, 2026).
- ADA Title III covers private businesses that are open to the public. There's no written technical standard for it, but courts and DOJ settlements commonly use WCAG AA as the benchmark.
- Section 508 (federal agencies) uses WCAG 2.0 AA, and the EU's EN 301 549 uses WCAG 2.1 AA.

### SC 1.4.3 Contrast (Minimum) - Level AA

Text and images of text need a contrast ratio of at least 4.5:1 against the background. Large text only needs 3:1, and large means at least 18pt (24px) regular or 14pt (about 18.66px) bold.

Contrast ratio compares the relative luminance (how bright it looks) of the lighter color, L1, to the darker color, L2:

```
contrast ratio = (L1 + 0.05) / (L2 + 0.05)
```

It goes from 1:1 (same color) to 21:1 (black on white). Hue doesn't matter, only luminance, which lines up with MacKenzie's (2024, Ch. 2) section on luminance and vision.

#### Exceptions

These don't have to pass:

- Text in disabled controls
- Pure decoration, or text nobody can see
- Text that's part of a photo with other important visual content
- Logos and brand names

#### What to Look For

- Light gray placeholder text in inputs, this one fails a lot
- Gray secondary text like timestamps, fine print, prices, and footnotes
- Text over images, gradients, or video. Measure the worst spot
- Every state on its own: hover, focus, selected, visited. A selected button with white text on light green is its own color pair
- Error and warning text. Pure red `#FF0000` on white is 4.0:1 and fails
- Stuff that looks disabled but still works. If you can click it, it isn't exempt

#### Related Criteria

I should check these in the same pass:

| SC | Level | Rule |
| --- | --- | --- |
| 1.4.11 Non-text Contrast | AA, new in 2.1 | Input borders, icons, focus rings, and other UI parts need 3:1 against whatever's next to them |
| 1.4.1 Use of Color | A | Color can't be the only way information is shown. "Green means open, gray means booked" with no text or icon fails |

#### How to Measure

1. Chrome DevTools: inspect the text and click the color swatch next to `color` in the Styles pane. The picker shows the ratio with AA and AAA checkmarks. This is the most accurate way since it uses the actual CSS colors.
2. axe DevTools and WAVE flag contrast automatically, but they mark text over images and gradients as "needs review," and they only check whatever state the page is in when you scan.
3. WebAIM Contrast Checker for hex pairs I sample myself. Sampling from a screenshot isn't as exact because the anti-aliased edges of letters blend into the background, so sample the middle of a thick stroke.

#### Log Table

| Element | Screen | Colors (text on background) | Ratio | Required | Result |
| --- | --- | --- | --- | --- | --- |
| | | | | 4.5:1 | |

### SC 2.4.7 Focus Visible - Level AA

Anything you can use with a keyboard has to have a visible keyboard focus indicator.

Focus is whichever element is getting keyboard input right now. Keyboard users move it around with the keys below, and that includes screen reader users, people with motor disabilities who can't use a mouse, and power users.

| Key | What it does |
| --- | --- |
| Tab / Shift+Tab | Next / previous interactive element |
| Enter | Activates a link or button, submits a form |
| Space | Activates a button, toggles a checkbox |
| Arrow keys | Move within radio groups, selects, menus, tabs, sliders |
| Esc | Closes a dialog or menu |

The focus indicator is the visual marker on the focused element, usually an outline or ring. Without one, a sighted keyboard user has no idea where they are on the page.

#### What to Look For

- No indicator at all. Usually it's `outline: none` or `outline: 0` in the CSS with nothing replacing it
- An indicator that's technically there but so faint you can't see it (1px light gray on white). I'd log it even if it squeaks by 2.4.7
- Some components show focus and others don't (custom dropdowns, date pickers, clickable cards)
- Focus hidden behind a sticky header or under a popup. WCAG 2.2 made this its own criterion (2.4.11), but under 2.1 it's still worth noting as a usability issue

#### Keyboard Criteria

These get tested in the same pass. They're all Level A, so they're even more basic than 2.4.7:

| SC | Name | Fails when |
| --- | --- | --- |
| 2.1.1 | Keyboard | Something you can do with a mouse can't be done with a keyboard. A `<div>` with only a click handler can't be reached with Tab |
| 2.1.2 | No Keyboard Trap | Focus gets stuck and Tab can't get out (popups, embedded maps, payment iframes) |
| 2.4.3 | Focus Order | Focus jumps around in an order that doesn't make sense, or doesn't move into a dialog when it opens and back out when it closes |
| 2.4.1 | Bypass Blocks | There's no "Skip to main content" link or landmarks, so every page starts with tabbing through the whole navigation |

#### Manual Test

1. Click the address bar and put the mouse away.
2. Do the whole core task with just the keyboard.
3. At every stop: Can I see where focus is? Does the order make sense? Can I activate it? Am I stuck? After doing something like changing a filter or loading results, where did focus go?
4. Count how many Tab presses it takes to finish the task. That's an actual number for the report, and it works as an efficiency measure for H7 too.
5. Firefox's Accessibility Inspector has a Show Tabbing Order option that puts numbered focus stops over the page. A screenshot of that would make a good annotated figure.

#### Log Table

| Step | Element | Reachable? | Focus visible? | Order makes sense? | Notes |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

### Semantic Structure, ARIA, and Screen Reader Support

#### How a Screen Reader Reads a Page

A screen reader doesn't see the page. It reads the accessibility tree, which the browser builds from the HTML plus any ARIA. Every element in the tree has:

| Property | Meaning | Examples |
| --- | --- | --- |
| Role | What it is | button, link, heading level 2, checkbox, dialog |
| Name | What it's called | Button text, `alt` text, a `<label>`, `aria-label` |
| State or value | What it's doing | checked, expanded, selected, current, invalid |

If the HTML is semantic (`<button>`, `<nav>`, `<h2>`, `<label>`), the tree comes out right on its own. If everything is a `<div>`, the tree is just a bunch of unlabeled generic nodes and the user hears "clickable" or nothing.

Screen reader users don't usually listen to a page from top to bottom. They jump around by headings, landmarks (`<header>`, `<nav>`, `<main>`, `<footer>`), links, and form fields. WebAIM's screen reader surveys keep finding that headings are the most common way people find information on a long page, so a page without real headings is a lot harder to get around.

#### What Screen Reader Readability Means in WCAG

| SC | Level | Name | What to check |
| --- | --- | --- | --- |
| 1.1.1 | A | Non-text Content | Images and icons have useful `alt` text, and decorative ones have `alt=""` |
| 1.3.1 | A | Info and Relationships | The structure you can see is in the markup too: real headings, real lists, `<th>` table headers, labels tied to inputs |
| 2.4.2 | A | Page Titled | `<title>` describes the page and changes between steps |
| 2.4.6 | AA | Headings and Labels | Headings and labels describe the content or what it's for |
| 3.1.1 | A | Language of Page | `<html lang="en">` is set |
| 3.3.1 | A | Error Identification | Errors are described in text, not just a red border |
| 3.3.2 | A | Labels or Instructions | Inputs have visible labels and any instructions they need (format, limits) |
| 4.1.2 | A | Name, Role, Value | Every control has a name, role, and state, custom widgets included |
| 4.1.3 | AA | Status Messages | Updated results, "added," "nothing available," and errors get announced without stealing focus. New in 2.1 |

#### ARIA

ARIA (Accessible Rich Internet Applications) is a set of HTML attributes that add or override roles, names, and states in the accessibility tree. It doesn't change anything visually and doesn't add any behavior. Putting `role="button"` on a `<div>` doesn't make it focusable or make Enter work, the developer still has to build that.

The first rule of ARIA is that if there's a native HTML element that does the job, use that instead (World Wide Web Consortium, n.d.-c). So `<button>` over `<div role="button" tabindex="0">`. WebAIM's yearly Million report keeps finding that home pages with ARIA average more detected errors than pages without it. Basically, no ARIA is better than bad ARIA.

| Attribute | What it does | Typical use |
| --- | --- | --- |
| `role` | Says what an element is | `dialog`, `tab`, `alert`, `status` |
| `aria-label` | Gives it a name when there's no visible text | Icon-only buttons (`aria-label="Close"`) |
| `aria-labelledby` | Names it using another element's text | A dialog named by its heading |
| `aria-describedby` | Adds a description | Hints and error messages tied to a field |
| `aria-expanded` | Open or closed | Dropdowns, accordions, menus |
| `aria-selected` / `aria-pressed` / `aria-checked` | Selection state | Tabs, toggle buttons, custom checkboxes |
| `aria-current` | The current item in a set | Current page, current step, selected date |
| `aria-live` (`polite` / `assertive`) | Announces content when it changes | Result counts, status, errors (SC 4.1.3) |
| `aria-invalid` | The field has an error | Form validation |
| `aria-hidden="true"` | Removes it from the tree | Decorative icons. Never on something focusable |

#### Common Failures

- Clickable `<div>`s and `<span>`s with no role and no keyboard support
- Icon-only buttons with no name, so the screen reader just says "button"
- Inputs only labeled by placeholder text, which goes away once you start typing
- Bold text pretending to be a heading, or heading levels that skip (h1 straight to h4)
- Results, prices, or errors that change on screen without being announced
- Popups without `role="dialog"` that don't move focus inside or keep it there
- `aria-hidden="true"` on something you can Tab to
- Vague link or button text ("Click here," "Select") repeated over and over with no context

#### How to Test

1. Automated scan. Run axe DevTools ("Scan all of my page") and WAVE on every screen of the core task, not just the home page. Re-run them after each state change (results loaded, popup open, error showing) because scanners only see what's on the page when they run. Lighthouse (DevTools > Lighthouse > Accessibility) gives a third opinion and a score.
2. Accessibility tree. In Chrome DevTools, the Accessibility pane under Elements shows the role and name the browser came up with for any element. Firefox's Accessibility Inspector has "Check for issues" built in. WAVE's Structure tab outlines the headings and landmarks.
3. A real screen reader. Do the core task with one running and write down what I hear next to what's on screen.
   - Linux: Orca (launch with `orca`), works best with Firefox
   - Windows: NVDA (free)
   - Mac: VoiceOver (Cmd+F5)
   - iPhone: VoiceOver (Settings > Accessibility > VoiceOver). Worth doing if most people use the system on their phone
   - Android: TalkBack

#### Log Table

| Check | Tool | Finding | SC | Level | Result | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| A-01 | | | | | | `screenshots/A-01-*.png` |

### Other Quick Checks

These only take a minute each and catch some of the less obvious stuff:

| SC | Name | Test |
| --- | --- | --- |
| 1.4.4 | Resize Text (AA) | Zoom to 200%. Nothing should get cut off or overlap |
| 1.4.10 | Reflow (AA, new in 2.1) | Zoom to 400% on a 1280px wide window. Everything should fit in one column without scrolling sideways |
| 1.3.4 | Orientation (AA, new in 2.1) | On a phone, it works in both portrait and landscape |
| 2.5.3 | Label in Name (A, new in 2.1) | A button's accessible name has its visible text in it, so voice control users can say what they see |

### Automated vs. Manual Testing

Scanners only catch what a machine can check. They can tell an image has no alt text but not whether the alt text is accurate, and they can tell a button has a name but not whether the name makes sense. They can't judge focus order, whether a change gets announced, or whether the page even works with a keyboard. Deque, the company that makes axe, says automated testing covers about 57% of issues by volume (Deque Systems, 2021), so the rest has to be checked by a person. That's probably why the top tier of the rubric asks for violations found with keyboard and screen reader testing.

### Where WCAG and Nielsen Overlap

A WCAG failure is usually a heuristic violation too, and fixing it helps more people than just disabled users. That's called the curb-cut effect.

| WCAG failure | Heuristic | Who else it helps |
| --- | --- | --- |
| No focus indicator (2.4.7) | H1 Visibility of system status | Power users, anyone tabbing through a form |
| Results update silently (4.1.3) | H1 Visibility of system status | Anyone who looked away and missed the change |
| Status shown only by color (1.4.1) | H1, H4 | Colorblind users (about 1 in 12 men), anyone on a phone in sunlight |
| Low contrast text (1.4.3) | H8 Aesthetic and minimalist design | Older eyes, phones outdoors, cheap monitors |
| Error only shown in red (3.3.1) | H9 Recognize and recover from errors | Everyone who doesn't know what went wrong |
| Placeholder-only labels (3.3.2) | H6 Recognition rather than recall | Anyone who forgets what a field was for after typing |

### Course Connections

| Source | Concept | How it connects |
| --- | --- | --- |
| MacKenzie Ch. 2 | Human variability: design for the edges (about +/-3 SD), not the average user | WCAG is pretty much that idea written down as rules you can test |
| MacKenzie Ch. 2 | Alternative responders (keyboard, voice, switches) | They stand in for the mouse when someone can't use their hands the usual way, which is why keyboard support matters |
| Stephanidis & Salvendy Ch. 3 | Attention and visual search, look-but-fail-to-see | A change outside where the user is focused can go unnoticed. SC 2.4.7 and 4.1.3 fix that same problem for keyboard and screen reader users |

### GenAI Documentation

I used Claude to help me put this reference sheet together from the W3C's WCAG 2.1 docs so I'd know what to look for. All the findings in my audit come from me testing the system myself.

### References

Deque Systems. (2021). *The automated accessibility coverage report*. https://www.deque.com/automated-accessibility-coverage-report/

Kirkpatrick, A., O Connor, J., Campbell, A., & Cooper, M. (Eds.). (2018). *Web content accessibility guidelines (WCAG) 2.1*. World Wide Web Consortium. https://www.w3.org/TR/WCAG21/

MacKenzie, I. S. (2024). *Human-computer interaction: An empirical research perspective* (2nd ed.). Morgan Kaufmann. https://doi.org/10.1016/C2022-0-02755-0

Rivenburgh, K. (2026, April 17). *DOJ extends ADA Title II web compliance deadline 1 year*. Accessible.org. https://accessible.org/news/doj-extends-ada-title-ii-web-compliance-deadline/

Stephanidis, C., & Salvendy, G. (Eds.). (2025). *Foundations and fundamentals in human-computer interaction*. CRC Press. https://doi.org/10.1201/9781003495109

U.S. Department of Justice. (2024). *Nondiscrimination on the basis of disability; Accessibility of web information and services of state and local government entities* (89 Fed. Reg. 31320). https://www.federalregister.gov/d/2024-07758

WebAIM. (n.d.). *The WebAIM Million*. https://webaim.org/projects/million/

World Wide Web Consortium. (n.d.-a). *Understanding success criterion 1.4.3: Contrast (minimum)*. https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html

World Wide Web Consortium. (n.d.-b). *Understanding success criterion 2.4.7: Focus visible*. https://www.w3.org/WAI/WCAG21/Understanding/focus-visible.html

World Wide Web Consortium. (n.d.-c). *Using ARIA*. https://www.w3.org/TR/using-aria/
