## Problem Statement & Context of Use

### Problem Statement

> Davis County owns two public golf courses, Davis Park and Valley View, and both sell tee times through ForeUp's online booking. To a golfer they're two separate websites with separate accounts, and each one splits the same tee sheet into three booking classes ("18 Hole Groups," "9 Hole Groups," and "Single Golfers") that show different times and open on different days. To answer "where can we play tomorrow afternoon?", a golfer has to pick the right class on the right course and date, then remember what the other site showed. When they get it wrong they miss times that are actually open.

### The System

| | |
| --- | --- |
| **Platform** | ForeUp online booking, the golfer facing part of ForeUp's golf course management software |
| **Courses** | Davis Park Golf Course (Fruit Heights) and Valley View Golf Course (Layton) |
| **Owner** | Davis County Government, for both |
| **Booking pages** | `foreupsoftware.com/index.php/booking/19500/1757` (Davis Park) and `foreupsoftware.com/index.php/booking/19501/1759` (Valley View) |

ForeUp is the software a lot of public courses in Utah use for their tee sheet, point of sale, and online booking. I'm auditing the online booking page, where a golfer picks a booking class, a date, a number of players, and a tee time, and then prepays. It fits two of the eligible categories: it's a scheduling system, and since the county runs both courses, it's also a public service.

#### Why I Picked It

I golf at both courses, and booking on them bugged me enough that I built my own site (utahgolftimes) that pulls the open tee times from these and a few other local courses into one list. Building it meant learning how ForeUp's booking page works under the hood, and I found that a lot of what bugged me comes from how the courses are set up in ForeUp.

It also means I'm a bad judge of how hard this is for a normal golfer. I know which class to pick and why times disappear, so I don't get stuck anymore. That's basically the "developer testing their own code" problem from the post-mortem question, and it's why the sessions with real users count for more than my opinion.

### Two Courses, Two Separate Sites

| | Davis Park | Valley View |
| --- | --- | --- |
| Owner | Davis County Government | Davis County Government |
| Booking software | ForeUp | ForeUp |
| ForeUp course ID | `19500` | `19501` |
| Booking page | Its own URL | Its own URL |
| Golfer account | Its own sign-up | Its own sign-up |
| iPhone app | "Davis Park Golf Course" by Davis County Government | "Valley View Golf Course" by Davis County Government |
| Booking classes | 18 Hole Groups, 9 Hole Groups, Single Golfers | 18 Hole Groups, 9 Hole Groups, Single Golfers |
| Booking class IDs | `2094`, `2095`, `7559` | `1208`, `1209`, `5578` |
| Posted reservation policy | Same text | Same text, plus a warning not to hit Back during payment |
| Latest tee time shown | 100 minutes before sunset | 100 minutes before sunset |
| Late cancellation | "Within 1 hour of Tee Time: No refund. 50% rain check will be provided." | "Less Than 2 Hours Before Tee Time or No-Show: No refund or rain check will be provided." |

The two courses have the same owner, the same software, the same booking classes, and almost the same policy text, but there's no way to see both in one place. The course dropdown in the top left of the booking page looks like it would switch courses, but the only option in it is the one you're already on.

You also need a separate account at each course. ForeUp makes you sign up separately at every course that uses it, so a golfer who plays both has two logins for one county's courses. I use the same password on both, and I'd guess most people do, which isn't great on a site that stores your card.

To compare the two, I need two tabs. I pick a class and date in one, look at the times, then do it all again in the other while remembering what the first one showed. She et al. (2025) say the information a user needs should be at the task, not carried in their head between displays.

The county already treats the courses as one product when it's selling a season pass. The "Park/View Season pass" on both booking pages "may be used at either Davis Park or Valley View golf courses," and that's the only place either page mentions the other course. I don't think a combined view is beyond ForeUp either. Every request the booking page sends to ForeUp's times API passes the tee sheet as a list (`schedule_ids[]=1757`). The two courses are just set up as two unrelated ForeUp courses with one tee sheet each.

The cancellation rules are where the differences cost the most. The two policies are clearly copied from the same template, so someone who learns Davis Park's rule would expect Valley View to work the same way, and it doesn't. Cancel 90 minutes out at Davis Park and you get a rain check for the full amount. At Valley View you get nothing, because its cutoff is two hours instead of one. Neither page shows the policy where you book. The welcome message says "Cancellation (see email confirmation)," even though the rule is in the terms and conditions.

### Three Booking Classes in One Tee Sheet

Before you see any tee times, the page makes you pick a booking class. These were the settings on both courses on October 9, 2026:

| Booking class | Min players | Days shown (including today) | What it hides |
| --- | --- | --- | --- |
| 18 Hole Groups | 2 | 4 | Times with only 1 spot left, and every 9 hole only time |
| 9 Hole Groups | 2 | 3 | Times with only 1 spot left, and every 18 hole only time |
| Single Golfers | 1 | 3 | The 4th day out, which 18 hole groups can already see |

Each course also has a "Season Pass" class that only works with a pass login.

The classes are how ForeUp handles pricing and permissions, and the page makes them the golfer's first decision. A golfer is thinking "I want to play tomorrow afternoon with my friends," and the page asks which product they're buying (H2). Picking the wrong one doesn't give an error, you just see fewer times. MacKenzie (2024, Ch. 3) describes a mode as a state where the same action gives a different result, and says feedback about which mode you're in is the main problem. The booking class works like that. Picking "tomorrow" shows a different list depending on the class, and nothing on the list hints at what the other classes would show.

A few things the classes hide:

- Last spot tee times only show up under Single Golfers, because the group classes need at least 2 open spots. In my own data from this fall, Valley View had a 2:40 PM tee time with 0 spots under both group classes and 1 spot under Single Golfers. Someone playing alone who picks "9 Hole Groups" because they want 9 holes would never see it.
- An empty list can mean three things. For a date outside a class's window, ForeUp's API returns the same empty response it gives for a sold out day, so the golfer can't tell sold out from not open yet or wrong class (H1, H9).
- The posted policy and the settings count days differently. The policy says "Group tee times are available 3 days in advance for 18 holes, and 2 day in advance for 9 holes. Starting at 9:00pm." The settings say 4 and 3 because ForeUp counts today. It's the same rule, but you have to do the math yourself. On October 9, booking as 18 Hole Groups lit up the 9th through the 12th on the calendar, and 9 Hole Groups only went through the 11th.

#### Two Controls for the Same Choice

The page has two controls for how many holes you're playing. One is the booking class at the top ("Booking as 18 Hole Groups" with a Change button), and the other is the 9 Holes / 18 Holes / Both buttons on the left. Only the booking class decides what loads.

These screenshots are all Valley View for Saturday, October 10, taken October 9:

| Booking as | Holes filter | What shows up | Screenshot |
| --- | --- | --- | --- |
| 18 Hole Groups | 18 Holes | One tee time, 2:50 PM | `screenshots/class-switch-1-18-groups-18-holes.png` |
| 18 Hole Groups | 9 Holes | "There are no tee times available with your current search criteria" | `screenshots/class-switch-2-18-groups-9-holes-empty.png` |
| 9 Hole Groups | Both | Five 9 hole tee times from 1:30 PM on, and no 18 hole ones | `screenshots/class-switch-3-9-groups-both.png` |
| 9 Hole Groups | 18 Holes | "There are no tee times available with your current search criteria" | `screenshots/class-switch-4-9-groups-18-holes-empty.png` |

If you're booking as 18 Hole Groups and decide you'd rather play 9, the obvious move is to click "9 Holes," and you get nothing, even though Valley View has 9 hole times that afternoon. To see them you have to click Change next to "Booking as" and pick 9 Hole Groups, then do the reverse to go back. "Both" doesn't show both either. Under 9 Hole Groups it only shows 9 hole times.

The empty message says "To see more times, try adjusting filters (date, holes, players or time of day)." The holes filter is what caused the empty list, and the message never mentions the booking class, which is the actual fix (H9). There are two controls for one job (H4), and you can pick a filter that will never return anything for your class (H5).

### Rules You Can't See

Both tee sheets only show tee times up to 100 minutes before sunset (`sunset_offset: 100` in the page settings) so groups can finish before dark. Booking stays open all day. Only the list gets cut off, and the rule isn't in either course's policy, welcome message, or terms. On October 6, sunset in Kaysville was about 7:05 PM, so the last tee time shown was around 5:25 PM, and the list just ended there.

Sometimes the site glitches and shows every time anyway, including the ones past the cutoff. I've seen the late times flash up for about half a second and disappear, and sometimes they stay. Booking one goes through like normal. That happened to me. I prepaid for a late tee time on ForeUp's own page, and at check-in the course told me it shouldn't have been bookable (H5).

The courses seem to know people make mistakes, because they try to fix them with text. Both policies say "(Double check your DATE!!)" and "Please be accurate in your bookings," and Valley View adds:

> Do not hit the back button or refresh during payment process. Double charge could happen.

If a course has to put that in all caps, I'd guess people keep making that mistake (H3, H5). She et al. (2025) rank ways to control errors from strongest to weakest: remove the cause, substitute something less risky, control it, use warnings and procedures, and last, tolerate it. A "Double check your DATE!!" note is a warning, second to last on that list.

### Target Users

The users are anyone in Davis County who golfs, plus people from the rest of the Wasatch Front, from someone young booking on their phone to someone older booking online for the first time. MacKenzie (2024, Ch. 2) says to design for the edges of the population instead of the average user, and both edges use this site.

That's why I picked the participants I did. P1 and P2 are a generation apart. P1 has never booked a tee time online, and P2 books online once or twice a month, so between them they cover both ends.

| User type | What they need | Where ForeUp gets in the way |
| --- | --- | --- |
| Group organizer (books for 2-4 people) | A time that works for everyone, paid for the whole group | Has to pick 9 or 18 holes before seeing any times, and a wrong date costs the whole group |
| Single golfer | Any open spot to join | Has to know to use Single Golfers, gets one less day than 18 hole groups, and last spot times only show up there |
| First-time online booker | Just a tee time | ForeUp's own words ("booking class"), and rules spread across the welcome message, policy, terms, and confirmation email |
| Older golfers and golfers with disabilities | The same thing as everyone else | Small text, keyboard access, and screen reader support all have to work, and here that's a legal requirement |

### Core User Tasks

1. Find a tee time at one course for a specific day, time range, number of players, and 9 or 18 holes.
2. Compare the two courses to see which has the better time.
3. Book and prepay for the whole group, knowing the cancellation policy first.
4. Join as a single by finding a tee time with an open spot.
5. Check back for cancellations, or for the next day to open at 9:00 PM.

### Why It Matters

#### For Golfers

Checking one day at both courses can take six views (3 classes x 2 courses), and each one means picking the date again. I estimated the time cost with a Keystroke-Level Model in the heuristic evaluation (H-03). The wrong class doesn't give an error, it just shows fewer times, so people think nothing's open and give up, call, or go somewhere else.

They can also lose money. The person booking prepays for the whole group. Book the wrong date and catch it less than 12 hours out, and you get a rain check instead of a refund, and the welcome message says rain checks expire a month after they're issued. Inside the last hour Davis Park drops that to a 50% rain check, and Valley View gives nothing from two hours out.

#### For the County

A tee time can't be sold after it passes, so a time a single golfer couldn't find is money the course doesn't get back. Every confused golfer also turns into a phone call to the pro shop or a fix at the counter, like my check-in.

There's also the legal side. Davis County is a local government, so ADA Title II applies. The DOJ's 2024 rule requires WCAG 2.1 AA for web content a government provides, including through "contractual, licensing, or other arrangements" (U.S. Department of Justice, 2024), so the ForeUp page and both apps count even though ForeUp built them. Davis County had 362,679 people in the 2020 Census (U.S. Census Bureau, n.d.), which puts it in the 50,000+ group with a deadline of April 26, 2027 (Rivenburgh, 2026). That's about six and a half months from now.

H1 through H10 are Nielsen's (2024) heuristics, listed in `heuristic-evaluation.md`.

### References

MacKenzie, I. S. (2024). *Human-computer interaction: An empirical research perspective* (2nd ed.). Morgan Kaufmann. https://doi.org/10.1016/C2022-0-02755-0

Nielsen, J. (2024). *10 usability heuristics for user interface design*. Nielsen Norman Group. https://www.nngroup.com/articles/ten-usability-heuristics/

Rivenburgh, K. (2026, April 17). *DOJ extends ADA Title II web compliance deadline 1 year*. Accessible.org. https://accessible.org/news/doj-extends-ada-title-ii-web-compliance-deadline/

She, M., Yin, Z., & Li, Z. (2025). Human error. In C. Stephanidis & G. Salvendy (Eds.), *Foundations and fundamentals in human-computer interaction*. CRC Press. https://doi.org/10.1201/9781003495109-6

U.S. Census Bureau. (n.d.). *QuickFacts: Davis County, Utah*. Retrieved October 9, 2026, from https://www.census.gov/quickfacts/fact/table/daviscountyutah

U.S. Department of Justice. (2024). *Nondiscrimination on the basis of disability; Accessibility of web information and services of state and local government entities* (89 Fed. Reg. 31320). https://www.federalregister.gov/d/2024-07758
