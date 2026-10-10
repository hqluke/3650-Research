## Heuristic Evaluation: Nielsen's 10 Usability Heuristics

### How I Did It

I went through the core booking flow on both courses' ForeUp pages twice on October 9, 2026, following the process in `../reference/nielsen-heuristics.md`. The first time was just to learn it. The second time I went screen by screen, at full desktop width and at the narrow width that switches to the phone layout, and checked each screen against Nielsen's (2024) 10 heuristics.

I logged every problem before rating any of them, so I could compare the ratings against each other. Each rating uses Nielsen's (1994) three factors: how many people run into it (frequency), how hard it is to get past (impact), and whether people learn their way around it (persistence). When P1 or P2 ran into a problem, I based the rating on what happened to them (`synthesis.md`) instead of my own guess.

| Rating | Meaning |
| --- | --- |
| 0 | Not a usability problem |
| 1 | Cosmetic only |
| 2 | Minor. Slows people down, but they finish |
| 3 | Major. Causes errors, big delays, or wrong results, and some people give up |
| 4 | Catastrophe. People can't finish, or finish wrong without knowing |

### The Flow I Evaluated

1. Get to the booking page (a search, or a course link)
2. Pick a booking class (18 Hole Groups, 9 Hole Groups, Single Golfers, Season Pass)
3. Pick a date, time of day, number of players, and holes
4. Pick a tee time and go to checkout (I stopped before paying)
5. Do it again on the other course to compare
6. Find the booking rules and cancellation policy

### Summary

| ID | Finding | Heuristics | Severity |
| --- | --- | --- | --- |
| H-01 | The holes buttons and the booking class don't match, and the wrong combo shows no times | H1, H4, H5 | **4** |
| H-02 | Same empty message for sold out, not open yet, or wrong class, and it suggests fixing the wrong thing | H1, H9 | **3** |
| H-03 | Both county courses have separate sites, accounts, and apps, so you compare them yourself | H4, H6, H7 | **3** |
| H-04 | The calendar doesn't show the booking window | H1, H6, H10 | **3** |
| H-05 | The cancellation policy is hard to find and different at each course | H4, H6, H10 | **3** |
| H-06 | All caps warnings instead of preventing the mistakes | H3, H5 | **3** |
| H-07 | The sunset cutoff isn't written anywhere, and a glitch lets you book past it | H1, H5, H10 | **3** |
| H-08 | The first choice is ForeUp's pricing categories, with no explanation | H2, H10 | 2 |
| H-09 | Change sends you back to the class picker instead of switching in place | H3, H7 | 2 |
| H-10 | It doesn't remember your search and you can't share it | H7 | 2 |
| H-11 | The plain booking link opens a Log In popup on a passes page | H2, H3 | 2 |
| H-12 | The course dropdown only has one course in it | H4 | 1 |
| H-13 | The welcome text has typos, fake looking links, and a lot of yelling | H4, H8 | 1 |
| H-14 | "Both" only shows 9 hole times | H2, H4 | 2 |

Keyboard and screen reader problems are in `accessibility-audit.md`. A couple of them, like the tee times not being reachable by keyboard at all, would be a 4 here too.

### H-01: The Holes Buttons and the Booking Class Don't Match

Severity 4. Breaks H1 Visibility of System Status, H4 Consistency and Standards, and H5 Error Prevention.

The page has two controls that look like they pick how many holes you're playing. One is the booking class at the top ("Booking as 9 Hole Groups" with a Change button), and the other is the 9 Holes / 18 Holes / Both buttons on the left. Only the booking class decides which tee times load. If the buttons disagree with it, the list comes up empty, even when the course has plenty of times open.

| Booking as | Holes button | Result | Evidence |
| --- | --- | --- | --- |
| 18 Hole Groups | 18 Holes | Tee times | `screenshots/class-switch-1-18-groups-18-holes.png` |
| 18 Hole Groups | 9 Holes | Empty | `screenshots/class-switch-2-18-groups-9-holes-empty.png` |
| 9 Hole Groups | Both | Only 9 hole times | `screenshots/class-switch-3-9-groups-both.png` |
| 9 Hole Groups | 18 Holes | Empty | `screenshots/class-switch-4-9-groups-18-holes-empty.png` |

The booking class works like a mode, and MacKenzie (2024, Ch. 3) says feedback about which mode you're in is the main problem with modes. Here the only feedback is a small badge above the results, away from the buttons people are actually clicking.

| Factor | Rating |
| --- | --- |
| Frequency | High. Both participants hit it, and anyone who changes their mind about 9 vs 18 will |
| Impact | High. P1 never got past it and concluded "These courses are very full." P2 refreshed the page thinking it was broken |
| Persistence | P2 learned the workaround after one try. P1 never did |

I rated it a 4 because P1 walked away with the wrong answer and rated their confidence 5 out of 5.

### H-02: Same Empty Message No Matter What Went Wrong

Severity 3. Breaks H1 Visibility of System Status and H9 Help Users Recognize, Diagnose, and Recover From Errors.

The page says "There are no tee times available with your current search criteria. To see more times, try adjusting filters (date, holes, players or time of day)" in three different situations:

- the time is actually sold out
- the date isn't open yet for that booking class
- you're in the wrong booking class for the holes button you picked (H-01)

The site has to know which one it is, since it knows every class's booking window and limits, but it never says. The suggestion also lists "holes," and in the H-01 case that filter is what emptied the list in the first place. It never mentions the booking class, which is the actual fix. Evidence: `screenshots/empty-state-18-groups-both.jpg`.

| Factor | Rating |
| --- | --- |
| Frequency | High. Both participants saw it and both read it as sold out |
| Impact | High. It points people at the wrong control, or sends them to another course |
| Persistence | Every time, since the message never changes |

### H-03: Both Courses Have Separate Sites, Accounts, and Apps

Severity 3. Breaks H4 Consistency and Standards, H6 Recognition Rather Than Recall, and H7 Flexibility and Efficiency of Use.

Davis Park and Valley View are run by the same county on the same software, with the same booking classes and almost the same policy text. But a golfer gets two URLs, two accounts (ForeUp makes you sign up at every course), two iPhone apps, and no way to see both tee sheets at once. To compare them, you open two tabs, set the class, date, and players on each one, and remember the first course's times while you look at the second.

P2 switched tabs constantly in T2 and named "having to keep track of the times" as the hardest part. P1 searched for the second course from scratch and repeated every step.

I used the Keystroke-Level Model (KLM) to estimate how long the comparison takes. The KLM breaks a task into small actions and adds up a set time for each one, assuming an expert who doesn't make mistakes (MacKenzie, 2024, Ch. 7). The actions here are deciding what to do next (M, 1.35 s), moving the mouse to something (P, 1.1 s), clicking (K, 0.2 s), and waiting for the page to load (R, which I guessed at 1 s). The task I modeled is T2, finding the earliest 9 hole time for 2 players, with both sites already open.

| Step | Operators | Time |
| --- | --- | --- |
| Pick the class | M P K | 2.65 s |
| Wait for the tee sheet | R | 1.00 s |
| Pick the date | M P K | 2.65 s |
| Wait | R | 1.00 s |
| Pick 2 players | M P K | 2.65 s |
| Scan for the earliest time | M | 1.35 s |
| **One course** | | **11.30 s** |
| Switch tabs | P K M | 2.65 s |
| Second course, same steps | | 11.30 s |
| Remember the first course's time and compare | M | 1.35 s |
| **Two separate sites** | | **26.60 s** |
| **Both courses on one page** (pick the date, pick 2 players, scan once) | M P K, R, M P K, M | **7.65 s** |

Two sites take 26.6 seconds and one combined page would take 7.65, so comparing the courses takes about 3.5 times as long as it needs to. That's for an expert who never makes a mistake. On this same task, P2 hit a dead end and had to refresh, and P1 took about a minute.

| Factor | Rating |
| --- | --- |
| Frequency | Anyone who plays both courses or wants the earliest time anywhere |
| Impact | Medium. People finish, but slower and with more chance of misremembering |
| Persistence | Every time. There's no way around it |

### H-04: The Calendar Doesn't Show the Booking Window

Severity 3. Breaks H1 Visibility of System Status, H6 Recognition Rather Than Recall, and H10 Help and Documentation.

You can only book a few days out, and how many depends on your class. 18 Hole Groups get 4 days counting today, 9 Hole Groups and Single Golfers get 3, and the next day opens every night at 9:00 PM. The only hint on the calendar is that the days you can't book are a slightly lighter gray (`#6f777e` instead of `#333333`), and the narrow layout's date dropdown just leaves them out. Nothing says why you can't book a day or when it'll open. That's only in the welcome text ("3 days in advance for 18 holes and 2 day in advance for 9 holes. Stating at 9:00 pm"), and you'd still have to count the days yourself.

P1 never found it. In T4 they clicked next Friday, got an empty list, and decided the courses were full.

| Factor | Rating |
| --- | --- |
| Frequency | Anyone planning more than 2-3 days out |
| Impact | High for new users (P1 failed), low for regulars who already know |
| Persistence | Goes away once you learn the rule, but nothing on the page teaches it |

### H-05: The Cancellation Policy Is Hard to Find and Different at Each Course

Severity 3. Breaks H4 Consistency and Standards, H6 Recognition Rather Than Recall, and H10 Help and Documentation.

The only mention of cancelling in the welcome message is "Cancellation (see email confirmation)," so you're pointed to the rules after you've already paid. The actual policy is further down in "FOREUP TERMS & CONDITIONS." The two courses' terms are copied from the same template, but the last line is different:

| | Davis Park | Valley View |
| --- | --- | --- |
| 12+ hours out | Full refund | Full refund |
| Under 12 hours | Rain check for the full amount | Rain check for the full amount |
| Last stretch | Within 1 hour: 50% rain check | Under 2 hours or no-show: nothing |

So cancelling 90 minutes out gets you a full rain check at one county course and nothing at the other. Neither participant noticed the difference. P1 only found Valley View's rule after a hint, and then said "This doesn't make sense."

| Factor | Rating |
| --- | --- |
| Frequency | Anyone whose plans change on the day |
| Impact | High. It's the whole group's prepaid money |
| Persistence | Every time, since the policy is never shown during booking |

### H-06: All Caps Warnings Instead of Preventing the Mistakes

Severity 3. Breaks H3 User Control and Freedom and H5 Error Prevention.

Instead of preventing mistakes, the courses warn about them in the welcome text:

- "(Double Check your DATE!!)"
- "Please select the correct number of players" and "Please be accurate in your bookings"
- At Valley View, "Do not hit the back button or refresh during payment process. Double charge could happen."

If a course has to say it in all caps, I'd guess people make that mistake a lot. She et al. (2025) rank warnings second to last in their list of ways to control errors, just above tolerating the error. Showing the date, day of the week, and party size on the pay button, and making sure a refresh can't charge you twice, would stop these mistakes instead of warning about them. I stopped before paying, so I didn't test the double charge myself. This rating is based on the courses' own warnings.

| Factor | Rating |
| --- | --- |
| Frequency | Unknown, but the all caps warnings suggest it's common |
| Impact | High. A double charge or a wrong date costs real money |
| Persistence | Every time |

### H-07: The Sunset Cutoff Isn't Written Anywhere, and a Glitch Lets You Book Past It

Severity 3. Breaks H1 Visibility of System Status, H5 Error Prevention, and H10 Help and Documentation.

The tee time list stops 100 minutes before sunset so groups can finish before dark. Booking itself stays open all day. Only the list gets cut off, and the rule isn't in the welcome message, the booking rules, or the terms, so the list just ends in the late afternoon with no explanation. The bigger problem is that the site sometimes glitches and shows every time, and booking one past the cutoff goes through like normal. That happened to me. I prepaid for a late tee time on ForeUp's own page, and at check-in the course told me it shouldn't have been bookable.

| Factor | Rating |
| --- | --- |
| Frequency | Anyone looking for an evening time |
| Impact | High when the glitch lets a bad booking through, since you find out at the course |
| Persistence | Every evening, and the cutoff moves as sunset changes through the season |

### H-08: The First Choice Is ForeUp's Pricing Categories

Severity 2. Breaks H2 Match Between System and the Real World and H10 Help and Documentation.

The first screen asks you to pick "18 Hole Groups," "9 Hole Groups," "Single Golfers," or "Season Pass" before you see any tee times (`screenshots/class-picker.jpg`). These are how ForeUp handles pricing and permissions. A golfer is thinking "tomorrow afternoon, me and two friends." Nothing explains the classes or what each one hides, like that the group classes never show a tee time with only one spot left. Season Pass shows up for everyone even though it needs a pass login.

P1 said "I didn't really pay attention to them too much," which is how they ended up stuck later (H-01).

| Factor | Rating |
| --- | --- |
| Frequency | Every booking |
| Impact | Low on its own. It turns into a problem through H-01 |
| Persistence | Regulars learn it |

### H-09: Change Sends You Back to the Class Picker

Severity 2. Breaks H3 User Control and Freedom and H7 Flexibility and Efficiency of Use.

Clicking Change next to "Booking as" doesn't switch the class on the same page. It takes you back to the full class picker screen, welcome text and all, and you pick again (`screenshots/change-returns-to-class-picker.jpg`). Your date and filters carry over, but every switch between 9 and 18 holes is a trip to another screen, and keyboard focus gets dropped back to the top of the page (see `accessibility-audit.md`).

### H-10: It Doesn't Remember Your Search

Severity 2. Breaks H7 Flexibility and Efficiency of Use.

The address stays `#/teetimes` no matter what class, date, or filters you pick, so you can't bookmark or share a search like "Valley View, 9 Hole Groups, Saturday." P2 books once or twice a month and has to set up the same search from the class picker every time.

### H-11: The Plain Booking Link Opens a Log In Popup

Severity 2. Breaks H2 Match Between System and the Real World and H3 User Control and Freedom.

If you go to Valley View's booking address without `#teetimes` on the end (`foreupsoftware.com/index.php/booking/19501/1759`), you land on a "passes" page with a Log In/Register popup over an empty screen (`screenshots/login-modal-on-landing.jpg`). Someone who just wants a tee time has to know to close the popup and click Reservations. Neither participant came in this way, so I rated it a 2.

### H-12: The Course Dropdown Only Has One Course

Severity 1. Breaks H4 Consistency and Standards.

The top of the tee time page has a course dropdown that looks like it should switch courses, but the only option is the course you're already on.

### H-13: The Welcome Text

Severity 1. Breaks H4 Consistency and Standards and H8 Aesthetic and Minimalist Design.

The welcome message is centered, bold, and mostly in caps ("In UTAH!!!", "Double Check your DATE!!", "PLEASE NOTE"), with the bullets floating off to the left of the centered text. It has typos ("Stating at 9:00 pm," "2 day in advance"), and the "Starting at 9:00 pm" parts are underlined and italic, so they look like links but aren't. Valley View's version also repeats almost the same rules in the "Booking Rules" sidebar. When everything is bold and loud, nothing stands out, which might be part of why P1 never read the rules (H-04).

### H-14: "Both" Only Shows 9 Hole Times

Severity 2. Breaks H2 Match Between System and the Real World and H4 Consistency and Standards.

Under 9 Hole Groups, "Both" is selected by default but only shows 9 hole times (`screenshots/class-switch-3-9-groups-both.png`). It's a smaller version of H-01, and since it's the default, everyone sees it first.

### Heuristic Coverage

| Heuristic | Findings | Worst |
| --- | --- | --- |
| H1 Visibility of system status | H-01, H-02, H-04, H-07 | 4 |
| H2 Match between system and the real world | H-08, H-11, H-14 | 2 |
| H3 User control and freedom | H-06, H-09, H-11 | 3 |
| H4 Consistency and standards | H-01, H-03, H-05, H-12, H-13, H-14 | 4 |
| H5 Error prevention | H-01, H-06, H-07 | 4 |
| H6 Recognition rather than recall | H-03, H-04, H-05 | 3 |
| H7 Flexibility and efficiency of use | H-03, H-09, H-10 | 3 |
| H8 Aesthetic and minimalist design | H-13 | 1 |
| H9 Help users recognize, diagnose, and recover from errors | H-02 | 3 |
| H10 Help and documentation | H-04, H-05, H-07, H-08 | 3 |

### Limitations

I was the only evaluator, and I'm not a neutral one. I've used these pages a lot and built my own tee time site on ForeUp's data, so I already know the workarounds, which is why the user sessions matter so much. I didn't go through payment, so anything past checkout (H-06's double charge) is based on the courses' own warnings, not my testing.

### References

MacKenzie, I. S. (2024). *Human-computer interaction: An empirical research perspective* (2nd ed.). Morgan Kaufmann. https://doi.org/10.1016/C2022-0-02755-0

Nielsen, J. (1994). *Severity ratings for usability problems*. Nielsen Norman Group. https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/

Nielsen, J. (2024). *10 usability heuristics for user interface design*. Nielsen Norman Group. https://www.nngroup.com/articles/ten-usability-heuristics/

She, M., Yin, Z., & Li, Z. (2025). Human error. In C. Stephanidis & G. Salvendy (Eds.), *Foundations and fundamentals in human-computer interaction*. CRC Press. https://doi.org/10.1201/9781003495109-6
