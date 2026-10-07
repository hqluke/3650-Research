## Nielsen's 10 Usability Heuristics - Audit Reference

### What a Heuristic Evaluation Is

A heuristic evaluation is an expert review. I go through the interface myself and check each screen against a short list of rules of thumb (the heuristics), and every problem I find gets logged with the heuristic it breaks and how bad it is. Jakob Nielsen and Rolf Molich came up with the original heuristics in 1990, and Nielsen refined them into the 10 we use now in 1994.

It's called a "discount" method because you don't need any users to do it, but that's also its weakness. It finds what the evaluator thinks is a problem, not what actually trips real people up. Nielsen found that one evaluator only catches about 35% of the problems in an interface, and five evaluators together catch about 75% (Nielsen, 1994b). I'm one evaluator, so that's probably why Phase 1 has us observe real users too.

A heuristic is a judgment call, while a WCAG success criterion is pass/fail. The same problem can be both though, see `wcag-2.1-aa.md`.

### Audit Process

The course framework is three steps:

1. **Individual Evaluation.** Go through the core task at least twice. The first time is just to learn the flow, and the second time is slow, screen by screen and element by element. Screenshot each flaw right when I see it and name the file with its finding ID (`H-03-date-picker.png`) so the log and the screenshots match up.
2. **Heuristic Mapping.** Every problem gets at least one heuristic. A lot of problems break two, like a broken link with no feedback (H1 and H9).
3. **Severity Rating.** Rate each problem 0-4 after everything is logged, not while I'm still looking. Nielsen (1994c) says it's hard to rate well when you're focused on finding new problems, and rating at the end means I can compare each problem against all the others.

### Severity Scale

| Rating | Meaning | Rule of thumb |
| --- | --- | --- |
| 0 | Not a usability problem | After thinking about it, it isn't actually a problem |
| 1 | Cosmetic problem only | You notice it but it doesn't slow anyone down. Fix if there's time |
| 2 | Minor usability problem | Slows people down or annoys them, but they still finish. Low priority |
| 3 | Major usability problem | Causes errors, big delays, or wrong results, and some people give up. Important to fix |
| 4 | Usability catastrophe | People can't finish the task, or they finish it wrong without knowing. Has to be fixed before launch |

Nielsen (1994c) bases a rating on three things together:

| Factor | Question to ask |
| --- | --- |
| Frequency | Does it happen to a lot of users or just a few? |
| Impact | Is it easy to get past, or hard? |
| Persistence | Is it a one time thing users learn to get around, or does it get them every time? |

He also considers market impact, since some problems hurt a product's reputation even when they're easy to get past.

I'm going to write the three factors next to each rating in my log. That way the rating is about the problem and not about how annoyed it made me.

### The 10 Heuristics

Each one has a short definition and then a list of what to look for.

#### H1. Visibility of System Status

The system should keep users updated on what's going on, with feedback that shows up in a reasonable amount of time.

- Loading or searching with no spinner or progress bar
- An action (submit, book, add to cart, save) with no confirmation that it worked
- Not showing the current state, IE which filter, date, or option is selected, or what step of a multi-step flow you're on
- Content that shows up and then disappears or changes without any explanation
- Hidden timers, like a reservation hold that quietly expires
- Data that could be out of date with no "last updated" time

#### H2. Match Between System and the Real World

Use words and concepts the user already knows, in an order that makes sense to them, instead of the system's internal terms.

- Database or business jargon in the UI (internal category names, codes, IDs)
- Steps in the order the system stores the data instead of how people think about the task
- Icons, date or time formats, or units people don't recognize
- Labels that mean one thing to a normal person and something else to the company

#### H3. User Control and Freedom

People make mistakes and need an obvious way out that doesn't take a bunch of steps.

- Browser Back breaks the page or loses everything you entered
- No Cancel or close button on popups and multi-step flows
- Changing one choice makes you start over
- No way to edit or cancel something after it's done, or the policy for doing it is hidden
- No undo for destructive actions

#### H4. Consistency and Standards

Users shouldn't have to wonder if different words, situations, or actions mean the same thing. This covers internal consistency, where the same thing looks and works the same across the whole product, and external consistency, where it follows the conventions of other sites. Jakob's law says users spend most of their time on other sites, so they expect yours to work like those.

- The same action called different things on different screens (Book, Reserve, Continue)
- Buttons that move around between steps
- Links that don't look like links, or text that looks like a link but isn't
- Breaking conventions people bring from other sites (logo doesn't go home, cart isn't in the corner)
- Negative transfer, where a familiar pattern does something unexpected here

#### H5. Error Prevention

Preventing the problem is better than having a good error message. Either get rid of the conditions that cause errors, or check for them and have the user confirm before they commit.

There are two kinds of errors. A slip is when someone meant to do the right thing and the action went wrong, like a mis-tap. A mistake is when the plan itself was wrong because the interface gave them the wrong mental model. She et al. (2025) is the human error chapter in the textbook to cite for this, and it covers mode errors too.

- Options that can't work are still selectable (sold out, in the past, out of range)
- Rules users only find out about after they fail, IE limits, eligibility, booking windows
- Free text fields where a picker or restricted input would stop bad input
- No confirmation before expensive or permanent actions (payment, cancellation, deletion)
- Defaults that give the wrong result if the user doesn't notice them
- Modes, where the same action does different things based on a state you can't see

#### H6. Recognition Rather Than Recall

Keep memory load low. Objects, actions, and options should be visible, and whatever the user needs to make a decision should be on the same screen as the decision. Working memory only holds about 7 +/- 2 items (MacKenzie, 2024, Ch. 2), so anything the user has to carry from one screen to the next uses some of that up.

- Having to remember something from a previous screen or a separate policy page
- Codes or IDs the user has to type from memory
- Important rules (limits, hours, prices, fees) shown somewhere other than where the choice gets made
- No recent history, saved info, or previous selections
- Icon-only buttons with no labels

#### H7. Flexibility and Efficiency of Use

Shortcuts that new users might not even notice can speed up experienced users. The system should work for both and let people customize the things they do a lot.

- Tasks people repeat that take the full path every time (no favorites, rebook, saved party or payment)
- No way to compare options side by side, so users have to check them one at a time
- No filters, sorting, or search on long lists
- URLs you can't bookmark or share to get back to the same view
- No keyboard shortcuts, or forms where Enter doesn't submit
- Lots of steps or clicks for the core task. A Keystroke-Level Model estimate (MacKenzie, 2024, Ch. 7) can turn that into a number

#### H8. Aesthetic and Minimalist Design

Every extra bit of information competes with the stuff that matters and makes it harder to see. This one is more about signal-to-noise and what stands out on the screen than about how pretty it looks. The Hick-Hyman law backs it up: decision time goes up with the log of the number of choices (Stephanidis & Salvendy, 2025, Ch. 3).

- Ads, upsells, or promos competing with the task
- Info people rarely need taking up prime screen space
- The most important thing on the screen isn't the most noticeable
- Walls of text, especially policy text, that you have to get through to continue
- Too many choices shown at once

#### H9. Help Users Recognize, Diagnose, and Recover From Errors

Error messages should be in plain language with no codes, say exactly what went wrong, and suggest how to fix it.

- Error codes or technical messages ("Error 500," "invalid request")
- Messages that say something failed but not what or why
- No suggested fix or next step
- Errors shown far away from the field that caused them, or only shown with color
- Empty states that don't tell the difference between "nothing matches," "something broke," and "you aren't allowed to see this"
- Input that gets wiped after an error so the user has to type it all again

#### H10. Help and Documentation

Ideally the system doesn't need documentation, but when people do need help it should be easy to find, about the task they're doing, and give actual steps.

- No help or FAQ, or help that's hard to get to from where the problem happens
- Help that explains features instead of how to get things done
- Important policies (cancellations, fees, eligibility) buried or missing
- No contact info when the only fix is talking to a person
- No tooltips or hints on confusing fields

### Common Heuristic Pairings

Some kinds of problems break the same heuristics pretty much every time:

| Problem | Heuristics |
| --- | --- |
| Something fails with no message | H1, H9 |
| Jargon in an error message | H2, H9 |
| A rule you only learn about after failing | H5, H6 (H10 too if it's only written down somewhere else) |
| Changing one setting resets everything | H3, H5 |
| The same control works differently on two screens | H4, H5 |
| Status shown only by color | H1, H4 (also fails WCAG SC 1.4.1) |

### Course Connections

| Source | Concept | Heuristic |
| --- | --- | --- |
| MacKenzie Ch. 2 | Working memory (7 +/- 2) and chunking | H6 |
| MacKenzie Ch. 2 | Human variability: design for the edges, not the average user | H7, accessibility |
| MacKenzie Ch. 7 | Keystroke-Level Model for counting how much a task costs | H7 |
| Stephanidis & Salvendy Ch. 3 | Hick-Hyman law | H8 |
| Stephanidis & Salvendy Ch. 3 | Task switch costs (bouncing between tabs or sites) | H6, H7 |
| She et al. (2025) | Slips, mistakes, mode errors | H5, H9 |
| Course page on prior experience | Jakob's law, positive and negative transfer | H4 |
| Course page on prior experience | Users with low self-efficacy are scared they'll break something | H3, H9 |

### Findings Log Template

| ID | Screen / Step | What happened | Heuristic(s) | Freq / Impact / Persist | Severity | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| H-01 | | | | | | `screenshots/H-01-*.png` |

### GenAI Documentation

I used Claude to help me put this reference sheet together from the course's heuristics page and Nielsen's articles so I'd know what to look for. All the findings in my audit come from me going through the system myself.

### References

MacKenzie, I. S. (2024). *Human-computer interaction: An empirical research perspective* (2nd ed.). Morgan Kaufmann. https://doi.org/10.1016/C2022-0-02755-0

Nielsen, J. (1994a). Enhancing the explanatory power of usability heuristics. *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*, 152-158. https://doi.org/10.1145/191666.191729

Nielsen, J. (1994b). *How to conduct a heuristic evaluation*. Nielsen Norman Group. https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/

Nielsen, J. (1994c). *Severity ratings for usability problems*. Nielsen Norman Group. https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/

Nielsen, J. (2024). *10 usability heuristics for user interface design*. Nielsen Norman Group. https://www.nngroup.com/articles/ten-usability-heuristics/

Nielsen, J., & Molich, R. (1990). Heuristic evaluation of user interfaces. *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*, 249-256. https://doi.org/10.1145/97243.97281

She, M., Yin, Z., & Li, Z. (2025). Human error. In C. Stephanidis & G. Salvendy (Eds.), *Foundations and fundamentals in human-computer interaction*. CRC Press. https://doi.org/10.1201/9781003495109-6

Stephanidis, C., & Salvendy, G. (Eds.). (2025). *Foundations and fundamentals in human-computer interaction*. CRC Press. https://doi.org/10.1201/9781003495109
