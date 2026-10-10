## Post-Mortem Reflection

### 1. How did combining qualitative user observations with an expert heuristic evaluation reveal usability flaws that a developer testing their own code would likely overlook?

I'm basically the developer testing their own code here. I built a site on ForeUp's data, so I always pick the right booking class and never see the empty list, and on my own I would have rated H-01 a 2 or 3. Watching P1 is what made it a 4. They clicked "18 Holes" on both courses, saw nothing, and decided the courses were full, with 5 out of 5 confidence. MacKenzie (2024, Ch. 3) says "programmers' discretion rules the day." The booking class makes sense if you built the system, and it only falls apart for people who didn't.

It worked the other way too. Neither participant used a keyboard or noticed the cancellation rules were different, so the expert review is what caught those. Looking back, my biggest mistake would have been testing with only P2. P2 passed four of five tasks, so I'd have said the site works, but P2 hit the same problem as P1 and just pushed through it. That's what a developer testing with people like themselves would miss.

### 2. Identify one heuristic violation that directly creates a legal or ethical accessibility barrier under WCAG 2.1 AA, and explain how resolving that violation improves the user experience for both disabled users and the general public.

I'd pick H-02, the empty results message. The page shows the same message whether the times are sold out, not open yet, or hidden by the booking class. It doesn't tell you what's going on (H1) or how to fix it (H9). Screen reader users have it worse. The page has no `aria-live` region, so they aren't told anything when the list changes (A-07 in `accessibility-audit.md`). That fails **SC 4.1.3 Status Messages**, and since Davis County has to meet WCAG 2.1 AA under Title II (U.S. Department of Justice, 2024), it's a legal problem too.

The fix is a status message that says why the list is empty, like "No 18 hole times because you're booking as 9 Hole Groups." A screen reader would read it out and everyone else would see it, so P1 would have found the 18 hole times and P2 wouldn't have refreshed the page. Becker (2020, Ch. 2) says "A product, service, or interface that is not accessible is not usable," and here fixing one fixes the other. The keyboard failure (SC 2.1.1, A-01) is the bigger legal problem and I'd fix it first, but it mostly helps people who can't use a mouse, while fixing the empty message helps every golfer who sees it.

### References

Becker, C. R. (2020). *Learn human-computer interaction: Solve human problems and focus on rapid prototyping and validating solutions through user testing*. Packt Publishing.

MacKenzie, I. S. (2024). *Human-computer interaction: An empirical research perspective* (2nd ed.). Morgan Kaufmann. https://doi.org/10.1016/C2022-0-02755-0

U.S. Department of Justice. (2024). *Nondiscrimination on the basis of disability; Accessibility of web information and services of state and local government entities* (89 Fed. Reg. 31320). https://www.federalregister.gov/d/2024-07758
