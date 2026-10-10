## Synthesis: What P1 and P2 Showed Me

This is the synthesis of my two sessions from October 9, 2026 (`field-notes/P1.md` and `field-notes/P2.md`). Both participants did the same five tasks from `research-protocol.md` on the Davis Park and Valley View ForeUp booking pages, with one change to T1 for each (noted below).

### The Two Participants

| | P1 | P2 |
| --- | --- | --- |
| Generation | Older | Younger |
| How often they golf | Every few weeks now, a few times a year before that | Once or twice a month |
| Booked a tee time online before? | Never. Someone else has always booked for them | Yes, once or twice a month, "a few days out" |
| Device | Samsung phone, Firefox | Windows PC, Chrome |
| Whole session | 8:04-8:17 PM, 13 minutes | 8:20-8:26 PM, 6 minutes |

P1 is close to a first-time user and P2 is close to an active user, which is the spread I wanted.

### Task Results

| Task | P1 | P2 |
| --- | --- | --- |
| T1. Book for a group | Success (switched to 9 holes, since there were no 18 hole times tomorrow) | Success (switched to the day after tomorrow, same reason) |
| T2. Compare the courses | Success | Success, after a dead end and a page refresh |
| T3. Go as a single | Marked success, but never left 9 Hole Groups, so never saw Single Golfers or any 18 hole time | Success |
| T4. Booking window | **Failed.** Decided there were no 18 hole times at all | Success |
| T5. Cancellation | **Failed.** Needed a hint, didn't notice the courses differ | **Failed.** Didn't notice the courses differ |

On T4, P1 rated the task 3 out of 7 for ease and 5 out of 5 for confidence, and their answer was wrong. If you're sure nothing is open, you don't keep looking, you just go somewhere else.

P2 finished all five tasks in 6 minutes, less than half of P1's 13. P2 moved too fast for me to time each task (see the note in `field-notes/P2.md`), but going by my estimates from right after the session, T2 took the longest because of the refresh and the tab switching, and T4 the shortest because P2 went straight to the booking class.

### Theme 1: The Holes Buttons Don't Do What They Say

This was the biggest thing I found, and both participants ran into it. Both used the 9 Holes / 18 Holes buttons on the left to pick how many holes they were playing, which makes sense since that's what they're labeled. But the booking class at the top ("Booking as 9 Hole Groups" with a Change button) decides what loads, and when the two disagree the list is empty.

P1 never figured it out. In T3 and T4 they clicked "18 Holes" while booking as 9 Hole Groups, saw nothing, switched courses, and saw nothing again. They concluded "These courses are very full. I can't find an 18 hole time," and said in the debrief, "There's no 18 hole times available anytime at either of the courses." There were 18 hole times. P1 just couldn't get to them.

P2 got through by trial and error. In T2 they clicked "9 Holes" while booking as 18 Hole Groups, saw nothing, and refreshed because they thought the page was broken. Then they tried Change, picked 9 Hole Groups, and the times showed up ("Why are there times now?"). On T4 they went straight to Change. P2 learned the workaround, but still came away thinking the site was broken: "I want those buttons on the left side to work, when I click 18 and i'm on 9, no times show up... It's weird they have a broken button."

When I asked what the class names meant, P1 said "I didn't really pay attention to them too much. I just clicked on 9 holes at the beginning because that was the first one I had to find." P2 understood them fine ("Whether you wanted to play 18 holes, 9 holes, or by your self"), and it didn't help, because the buttons that look like they pick holes don't.

MacKenzie (2024, Ch. 3) says the main problem with modes is feedback about which mode you're in. The "Booking as" badge is the only feedback here, and it sits above the results, away from the holes buttons people are actually clicking.

### Theme 2: An Empty List Means "Sold Out"

Both participants took "There are no tee times available with your current search criteria" to mean everything was booked. When I asked what they thought it meant, P1 said "That every time had been booked," and P2 said "That the times had been booked. But then I switched the booking as at the top and I found times, so I think the sites broken."

The page shows that same message when the times are sold out, when the date isn't open yet, and when you're in the wrong class. It suggests you "try adjusting filters (date, holes, players or time of day)," which points at the holes filter that caused the problem and never mentions the booking class.

This costs the county too. P1 wanted to play 18 holes, decided both courses were full, and in real life would have gone somewhere else or not played. That's a tee time the course never sells.

### Theme 3: The Answers Are in the Rules, and Nobody Reads Them

The booking windows and the cancellation policy are both written on the page, but neither participant used them.

In T4, P1 clicked next Friday, saw nothing, and assumed it was full. They never saw the welcome text saying 18 holes opens "3 days in advance... Starting at 9:00 pm." The rules are in a block of centered, highlighted text beside the tee times, and P1's attention was on the calendar and the buttons, which is where the task was.

T5 went the same way. P1 first said they didn't know what would happen to their money, and only checked the page after I suggested it. When they found Valley View's rule, they said they couldn't believe there was no refund or rain check, and then, "I didn't think I would find this out. This doesn't make sense." P1's one change to the site would be "That I would be able to cancel a golf round if something comes up." P2 found Davis Park's 50% rain check and thought it was "pretty nice," but said "the text was a little small and hard to read."

Neither of them noticed that the two courses have different rules. At 90 minutes out, Davis Park gives a rain check for the full amount and Valley View gives nothing. The terms look almost identical, so there's no reason to expect a difference, and that's the part that would actually cost them money. She et al. (2025) put warnings near the bottom of their list of ways to control errors, and these sessions show why: the rules are on the page, just not where people are making the decision.

### Theme 4: Comparing Courses Happens in Your Head

What the participants said about the two separate sites didn't match what they did. When I asked, P1 said the two sites "look the same, just have different times available," and P2 said "I would just switch tabs. Pretty easy."

But in T2, P2 kept flipping between the Davis Park and Valley View tabs and took a while to keep both sets of times straight. When I asked what took the most effort, P2 said "Having to switch the 'booking as' at the top of the page and having to keep track of the times." P1 handled it by searching for Valley View from scratch and going through the same steps again.

I think nobody complained because every course having its own site is normal to them, so it doesn't come up when you ask. It only showed up because I was watching.

### Theme 5: The More Experienced User Hit the Same Traps

P2 is probably the kind of user a developer would test with, and P2 passed four of five tasks. But P2 hit the same traps P1 did, just faster.

| Trap | P1 (first-time user) | P2 (active user) |
| --- | --- | --- |
| Holes button vs booking class | Never got past it. Concluded there were no 18 hole times | Refreshed, then found Change by trial and error |
| Empty list | Believed it, with full confidence | Believed it, then decided the site was broken |
| Rules text | Didn't see it | Not observed. I didn't catch how they worked out T4 |
| Cancellation difference | Missed it, even with a hint | Missed it |
| Comparing courses | Searched and repeated every step | Constant tab switching |

P1 ended up thinking the courses were full and P2 ended up thinking the site was broken. Both were wrong.

### Mental Model Mismatches

| What the user thinks | What the system does | Evidence |
| --- | --- | --- |
| The 9 Holes / 18 Holes buttons choose how many holes I'm playing | The booking class decides. The buttons only filter what the class loaded | P1 T3 and T4, P2 T2, P2 debrief Q6 |
| An empty list means everything's booked | It can mean sold out, not open yet, or wrong class | P1 debrief Q3, P2 debrief Q3, P1 T4 |
| "Both" shows 9 and 18 hole times | Under 9 Hole Groups, "Both" only shows 9 hole times | P1 T3 log, `screenshots/class-switch-3-9-groups-both.png` |
| My class shows every open time | Group classes hide times with only 1 spot left | P2 T3: "I'm not sure why just 9 holes didn't show the 1 person available spots" |
| Two courses run by the same county have the same rules | The cancellation rules are different | Both participants, T5 |

### Breakdown Log

| ID | Who | Task | What they expected | What happened | Result |
| --- | --- | --- | --- | --- | --- |
| B-01 | P1 | T3 | Clicking "18 Holes" shows 18 hole times | Empty list, because they were still in 9 Hole Groups | Concluded there were no 18 hole times tomorrow |
| B-02 | P1 | T4 | Clicking next Friday shows times or says when it opens | Empty list with no reason given | Concluded "These courses are very full," with 5/5 confidence |
| B-03 | P1 | T5 | Knows or can easily find the cancellation rule | Didn't look until given a hint | Found Valley View's rule, missed that Davis Park's is different |
| B-04 | P2 | T2 | Clicking "9 Holes" shows 9 hole times | Empty list, because they were still in 18 Hole Groups | Refreshed the page, then found Change by trial and error |
| B-05 | P2 | T2 | Comparing two courses is a quick look | Constant tab switching to keep both sets of times in mind | Finished, but slowly, and named it the hardest part |
| B-06 | P2 | T5 | Cancellation works the same at both county courses | It doesn't | Missed the difference |

These breakdowns map to findings in `heuristic-evaluation.md`: B-01 and B-04 are H-01, B-02 is H-02 and H-04, B-03 and B-06 are H-05, and B-05 is H-03.

### Limitations

- Both participants are from my family. That's enough to find problems, but not to say how common they are.
- P1 used a phone and P2 used a desktop, so I can't separate the effect of the device from the effect of experience. Some of P1's trouble could be from the phone layout.
- There were no 18 hole times tomorrow, so I changed T1 for both participants in different ways. That's also why P1 started on 9 holes and hit the class trap in T3 instead of T2.
- I didn't record the sessions, so for P2 especially I only have what I could remember right after.
- Both sessions ran just after 8 PM, about an hour before the next day opened, so the booking windows they saw were the most limited ones of the day.

### References

MacKenzie, I. S. (2024). *Human-computer interaction: An empirical research perspective* (2nd ed.). Morgan Kaufmann. https://doi.org/10.1016/C2022-0-02755-0

She, M., Yin, Z., & Li, Z. (2025). Human error. In C. Stephanidis & G. Salvendy (Eds.), *Foundations and fundamentals in human-computer interaction*. CRC Press. https://doi.org/10.1201/9781003495109-6
