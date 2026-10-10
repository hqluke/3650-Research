# Phase 1: Contextual Research & Diagnostic Usability Audit

**ForeUp Online Booking at Davis County's Davis Park and Valley View Golf Courses**

Luke Peterson · CS 3650 Human-Computer Interaction · Weber State University · October 10, 2026

Research repository: [github.com/hqluke/3650-Research](https://github.com/hqluke/3650-Research)

> [!summary] Summary
> Davis County's two public golf courses, Davis Park and Valley View, both sell tee times through ForeUp, but golfers get two separate booking sites, and each one splits its tee sheet into three booking classes that show different times. I watched two golfers do five booking tasks, ran a heuristic evaluation, and audited the site against WCAG 2.1 AA.
>
> - Both participants picked 9 or 18 holes with the buttons on the left, got an empty list, and decided the courses were full or the site was broken. Only the booking class decides which times load.
> - 14 heuristic problems: one rated 4 (catastrophe) and six rated 3 (major).
> - 10 WCAG 2.1 AA failures, 5 at Level A. You can't pick a tee time with a keyboard at all, and the county has to fix that under ADA Title II by April 26, 2027.

## 1. System Selection & Problem Statement

> [!important] Problem Statement
> Davis County owns two public golf courses, Davis Park and Valley View, and both sell tee times through ForeUp's online booking. To a golfer they're two separate websites with separate accounts, and each one splits the same tee sheet into three booking classes ("18 Hole Groups," "9 Hole Groups," and "Single Golfers") that show different times and open on different days. To answer "where can we play tomorrow afternoon?", a golfer has to pick the right class on the right course and date, then remember what the other site showed. When they get it wrong they miss times that are actually open.

### 1.1 The System

| | Davis Park | Valley View |
| --- | --- | --- |
| Owner | Davis County Government | Davis County Government |
| Booking software | ForeUp | ForeUp |
| Booking page | `foreupsoftware.com/index.php/booking/19500/1757` | `foreupsoftware.com/index.php/booking/19501/1759` |
| Golfer account | Its own sign-up | Its own sign-up |
| iPhone app | "Davis Park Golf Course" | "Valley View Golf Course" |
| Booking classes | 18 Hole Groups, 9 Hole Groups, Single Golfers | The same three |
| Late cancellation | "Within 1 hour of Tee Time: No refund. 50% rain check will be provided." | "Less Than 2 Hours Before Tee Time or No-Show: No refund or rain check will be provided." |

I golf at both courses, and booking on them bugged me enough that I built my own site (utahgolftimes) that pulls the open tee times from these and a few other local courses into one list. Building it meant learning how ForeUp's booking page works under the hood, so I already know which class to pick and why times disappear. That makes me a bad judge of how hard this is for a normal golfer, which is why the user sessions count for more than my opinion here.

### 1.2 Two Courses, Two Separate Sites

There's no way to see both courses in one place. The course dropdown at the top looks like it would switch courses, but the only option is the one you're on. To compare them I need two tabs, and I have to remember what the first one showed while I redo everything in the second. She et al. (2025) say the information a user needs should be at the task, not carried in their head between displays.

The county already sells one "Park/View Season pass" that "may be used at either Davis Park or Valley View golf courses," and the booking page sends the tee sheet to ForeUp's times API as a list (`schedule_ids[]=1757`), so I don't think a combined view is something ForeUp can't do. You also need a separate account at each course. I use the same password on both, and I'd guess most people do, which isn't great on a site that stores your card.

> [!warning] The cancellation rules don't match
> The two policies are clearly copied from the same template, but the last line is different. Cancel 90 minutes out at Davis Park and you get a rain check for the full amount. At Valley View you get nothing. Neither page shows the policy where you book. The welcome message just says "Cancellation (see email confirmation)."

### 1.3 Three Booking Classes in One Tee Sheet

Before you see a single tee time, the page makes you pick a booking class. These were the settings on both courses on October 9, 2026:

| Booking class | Min players | Days shown (including today) | What it hides |
| --- | --- | --- | --- |
| 18 Hole Groups | 2 | 4 | Times with only 1 spot left, and every 9 hole only time |
| 9 Hole Groups | 2 | 3 | Times with only 1 spot left, and every 18 hole only time |
| Single Golfers | 1 | 3 | The 4th day out, which 18 hole groups can already see |

The classes are how ForeUp handles pricing, and the page makes them the golfer's first decision. Picking the wrong one doesn't give an error, you just see fewer times. MacKenzie (2024, Ch. 3) describes a mode as a state where the same action gives a different result, and says feedback about which mode you're in is the main problem. The booking class works like that, and the 9 Holes / 18 Holes / Both buttons on the left look like a second control for it but don't decide anything (H-01).

### 1.4 Users, Tasks, and Why It Matters

The users are anyone in the area who golfs, from someone young booking on their phone to someone older booking online for the first time.

| User type | What they need | Where ForeUp gets in the way |
| --- | --- | --- |
| Group organizer (2-4 people) | A time that works for everyone, paid for the whole group | Has to pick 9 or 18 holes before seeing any times, and a wrong date costs the whole group |
| Single golfer | Any open spot to join | Has to know to use Single Golfers, and last spot times only show up there |
| First-time online booker | Just a tee time | ForeUp's own words ("booking class"), and rules spread across the welcome text, terms, and confirmation email |
| Golfers with disabilities | The same thing as everyone else | Keyboard access, zoom, and screen reader support all have to work |

Core tasks:

1. Find a tee time at one course for a specific day, time, group size, and 9 or 18 holes.
2. Compare the two courses for the better time.
3. Book and prepay for the group, knowing the cancellation policy first.
4. Join as a single.
5. Check back for cancellations, or for the next day to open at 9:00 PM.

For golfers, checking one day at both courses can take six views (3 classes x 2 courses), and the wrong class just shows fewer times, so people think nothing's open and give up. Whoever books also prepays for the whole group, so booking the wrong date and catching it under 12 hours out gets you a rain check that expires in a month instead of a refund.

For the county, a tee time nobody could find is lost money, and confused golfers turn into calls to the pro shop. Davis County is also a local government, so ADA Title II applies. The DOJ's 2024 rule requires WCAG 2.1 AA for web content a government provides, including through "contractual, licensing, or other arrangements" (U.S. Department of Justice, 2024), so the ForeUp page counts even though ForeUp built it. The county's deadline is April 26, 2027 (Rivenburgh, 2026).

## 2. Qualitative Contextual Research

### 2.1 Research Protocol

I ran think-aloud sessions in the style of a contextual inquiry. Each participant did five tasks on the device they'd normally book on and talked through it while I took notes, with a short interview before and after. Becker (2020, Ch. 5) calls this moderated observation, where you give the user a task and check it against success criteria. Knowing I was watching might change how they act, but nobody books a tee time on a schedule I can sit in on.

I wrote the tasks as situations and never said "booking class" or told them what to click. T5's 8:30 is 90 minutes out on purpose, since that's where the two courses' rules differ.

| Task | Read to participant |
| --- | --- |
| T1. Group | "You and three friends want to play 18 holes at Davis Park tomorrow, sometime after 2 PM. Find a time and go as far as you can without paying." |
| T2. Compare | "Your friend thinks Valley View might have something earlier. For 2 people playing 9 holes the day after tomorrow, which course has the earliest tee time, Davis Park or Valley View?" |
| T3. Single | "Now you're going by yourself. What's the latest time tomorrow you could play at either course?" |
| T4. Booking window | "You want to play 18 holes with a group next Friday. Can you book it right now? If not, when will you be able to?" |
| T5. Cancellation | "Say you booked tomorrow at 10 AM and something comes up at 8:30 AM. What happens to your money? Would it be different at the other course?" |

Interview questions were open-ended ("Walk me through the last time you got a tee time"), not yes/no. After each task I asked for an ease rating (1-7) and a confidence rating (1-5), and logged the result, time, errors, backtracks, hints, and quotes in a template I set up beforehand.

Both participants agreed to take part, are only called P1 and P2, and didn't pay for or book anything. I ran the sessions separately. Both are family and might go easy on the site, so I told them I didn't build it and never showed them my own site.

### 2.2 Participants and Results

| | P1 | P2 |
| --- | --- | --- |
| Generation | Older | Younger |
| How often they golf | Every few weeks now, a few times a year before that | Once or twice a month |
| Booked a tee time online before? | Never. Someone else has always booked for them | Yes, once or twice a month, "a few days out" |
| Device | Samsung phone, Firefox | Windows PC, Chrome |
| Session | 8:04-8:17 PM, 13 minutes | 8:20-8:26 PM, 6 minutes |

| Task | P1 | P2 |
| --- | --- | --- |
| T1. Group | Success (switched to 9 holes, since there were no 18 hole times tomorrow) | Success (switched to the day after tomorrow, same reason) |
| T2. Compare | Success | Success, after a dead end and a page refresh |
| T3. Single | Marked success, but never left 9 Hole Groups, so never saw Single Golfers or any 18 hole time | Success |
| T4. Booking window | **Failed.** Decided there were no 18 hole times at all | Success |
| T5. Cancellation | **Failed.** Needed a hint, didn't notice the courses differ | **Failed.** Didn't notice the courses differ |

On T4, P1 rated the task 3 out of 7 for ease and 5 out of 5 for confidence, and their answer was wrong. If you're sure nothing is open, you don't keep looking. P2 finished all five tasks in 6 minutes, less than half of P1's 13.

### 2.3 Themes

#### Theme 1: The holes buttons don't do what they say

Both participants used the 9 Holes / 18 Holes buttons on the left to pick how many holes they were playing, which makes sense since that's what they're labeled. But the booking class at the top decides what loads, and when the two disagree the list is empty.

P1 never got past it. In T3 and T4 they clicked "18 Holes" while booking as 9 Hole Groups, saw nothing, switched courses, and saw nothing again. P2 clicked "9 Holes" while booking as 18 Hole Groups in T2, saw nothing, and refreshed because they thought the page was broken. Then they tried Change, picked 9 Hole Groups, and the times showed up. By T4 they went straight to Change.

> [!quote] P1
> "These courses are very full. I can't find an 18 hole time."
>
> "There's no 18 hole times available anytime at either of the courses."

> [!quote] P2
> "Why are there times now?"
>
> "I want those buttons on the left side to work, when I click 18 and i'm on 9, no times show up... It's weird they have a broken button."

P2 understood the class names fine ("Whether you wanted to play 18 holes, 9 holes, or by your self"). It didn't help, because the buttons that look like they pick holes don't.

#### Theme 2: An empty list means "sold out"

Both participants took "There are no tee times available with your current search criteria" to mean everything was booked. When I asked what they thought it meant, P1 said "That every time had been booked," and P2 said "That the times had been booked. But then I switched the booking as at the top and I found times, so I think the sites broken."

The page shows that same message when the times are sold out, when the date isn't open yet, and when you're in the wrong class. It suggests you "try adjusting filters (date, holes, players or time of day)," which points at the holes filter that caused the problem and never mentions the booking class. P1 wanted to play 18 holes, decided both courses were full, and in real life would have gone somewhere else.

#### Theme 3: The answers are in the rules, and nobody reads them

The booking window and the cancellation policy are both written on the page, but neither participant used them. In T4, P1 clicked next Friday, saw nothing, and assumed it was full. They never saw the welcome text saying 18 holes opens "3 days in advance... Starting at 9:00 pm."

T5 went the same way. P1 first said they didn't know what would happen to their money, and only checked the page after I suggested it. When they found Valley View's rule, they said, "I didn't think I would find this out. This doesn't make sense." P2 found Davis Park's 50% rain check and thought it was "pretty nice," but said "the text was a little small and hard to read." Neither of them noticed that the two courses have different rules, and that's the part that would actually cost them money.

#### Theme 4: Comparing courses happens in your head

When I asked, P1 said the two sites "look the same, just have different times available," and P2 said "I would just switch tabs. Pretty easy." But in T2, P2 kept flipping between the Davis Park and Valley View tabs and took a while to keep both sets of times straight. In the debrief, P2 named "having to keep track of the times" as the hardest part. I think nobody complained because every course having its own site is normal to them, so it only showed up because I was watching.

### 2.4 Mental Model Mismatches

| What the user thinks | What the system does | Evidence |
| --- | --- | --- |
| The 9 Holes / 18 Holes buttons choose how many holes I'm playing | The booking class decides. The buttons only filter what the class loaded | P1 T3 and T4, P2 T2, P2 debrief |
| An empty list means everything's booked | It can mean sold out, not open yet, or wrong class | Both debriefs, P1 T4 |
| "Both" shows 9 and 18 hole times | Under 9 Hole Groups, "Both" only shows 9 hole times | P1 T3 |
| My class shows every open time | Group classes hide times with only 1 spot left | P2 T3: "I'm not sure why just 9 holes didn't show the 1 person available spots" |
| Two county courses have the same rules | The cancellation rules are different | Both participants, T5 |

### 2.5 Breakdown Log

| ID | Who | Task | Expected | What happened | Result | Finding |
| --- | --- | --- | --- | --- | --- | --- |
| B-01 | P1 | T3 | "18 Holes" shows 18 hole times | Empty list, still in 9 Hole Groups | Concluded there were no 18 hole times | H-01 |
| B-02 | P1 | T4 | Next Friday shows times or says when it opens | Empty list, no reason given | "These courses are very full," 5/5 confidence | H-02, H-04 |
| B-03 | P1 | T5 | Can find the cancellation rule | Didn't look until given a hint | Missed that Davis Park's rule is different | H-05 |
| B-04 | P2 | T2 | "9 Holes" shows 9 hole times | Empty list, still in 18 Hole Groups | Refreshed, then found Change by trial and error | H-01 |
| B-05 | P2 | T2 | Comparing courses is a quick look | Constant tab switching to keep both sets of times in mind | Finished, named it the hardest part | H-03 |
| B-06 | P2 | T5 | Cancellation works the same at both courses | It doesn't | Missed the difference | H-05 |

## 3. Heuristic Evaluation

### 3.1 Method

I went through the booking flow on both courses twice on October 9. The first time was just to learn it. The second time I went screen by screen, at both desktop and phone widths, and checked each screen against Nielsen's (2024) 10 heuristics. I wrote down every problem before rating any of them so I could compare them against each other. Then I rated each one on how many people it affects, how hard it is to get past, and whether people learn their way around it. When P1 or P2 ran into a problem, I based the rating on what happened to them instead of my own guess.

| Rating | Meaning |
| --- | --- |
| 0 | Not a usability problem |
| 1 | Cosmetic only |
| 2 | Minor. Slows people down, but they finish |
| 3 | Major. Causes errors or wrong results, and some people give up |
| 4 | Catastrophe. People can't finish, or finish wrong without knowing |

![Valley View's tee time page booked as 9 Hole Groups, with six numbered boxes: 1 the course dropdown, 2 the calendar, 3 the time of day, player, and holes filter buttons, 4 the Booking as badge and Change button, 5 the gray hole count badge on the first tee time, and 6 the booking rules text in the sidebar.](screenshots/annotated/fig-teesheet.png)

*Figure 1. The tee time page (Valley View, desktop, October 9). 1: course dropdown with only one course in it (H-12). 2: calendar that shows the booking window only by shading and can't be used with a keyboard (H-04, SC 2.1.1). 3: filter buttons that conflict with the booking class (H-01, SC 2.1.1). 4: the booking class, which actually decides what loads (H-01). 5: hole count badge at 3.98:1 contrast (SC 1.4.3). 6: booking rules, all caps warnings instead of prevention (H-06, H-13).*

### 3.2 Findings Summary

The table lists every finding and the heuristics it breaks. The number is the severity I gave the finding, and the bottom row shows the worst rating under each heuristic.

| ID | Finding | H1 | H2 | H3 | H4 | H5 | H6 | H7 | H8 | H9 | H10 |
| --- | --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| H-01 | The holes buttons and the booking class don't match, and the wrong combo shows no times | **4** |  |  | **4** | **4** |  |  |  |  |  |
| H-02 | Same empty message for sold out, not open yet, or wrong class, and it suggests fixing the wrong thing | **3** |  |  |  |  |  |  |  | **3** |  |
| H-03 | Both county courses have separate sites, accounts, and apps, so you compare them yourself |  |  |  | **3** |  | **3** | **3** |  |  |  |
| H-04 | The calendar doesn't show the booking window | **3** |  |  |  |  | **3** |  |  |  | **3** |
| H-05 | The cancellation policy is hard to find and different at each course |  |  |  | **3** |  | **3** |  |  |  | **3** |
| H-06 | All caps warnings instead of preventing the mistakes |  |  | **3** |  | **3** |  |  |  |  |  |
| H-07 | The sunset cutoff isn't written anywhere, and a glitch lets you book past it | **3** |  |  |  | **3** |  |  |  |  | **3** |
| H-08 | The first choice is ForeUp's pricing categories, with no explanation |  | 2 |  |  |  |  |  |  |  | 2 |
| H-09 | Change sends you back to the class picker instead of switching in place |  |  | 2 |  |  |  | 2 |  |  |  |
| H-10 | It doesn't remember your search and you can't share it |  |  |  |  |  |  | 2 |  |  |  |
| H-11 | The plain booking link opens a Log In popup on a passes page |  | 2 | 2 |  |  |  |  |  |  |  |
| H-14 | "Both" only shows 9 hole times |  | 2 |  | 2 |  |  |  |  |  |  |
| H-12 | The course dropdown only has one course in it |  |  |  | 1 |  |  |  |  |  |  |
| H-13 | The welcome text has typos, fake looking links, and a lot of yelling |  |  |  | 1 |  |  |  | 1 |  |  |
| | **Worst** | **4** | **2** | **3** | **4** | **4** | **3** | **3** | **1** | **3** | **3** |

*H1 Visibility of system status, H2 Match between system and the real world, H3 User control and freedom, H4 Consistency and standards, H5 Error prevention, H6 Recognition rather than recall, H7 Flexibility and efficiency of use, H8 Aesthetic and minimalist design, H9 Help users recognize, diagnose, and recover from errors, H10 Help and documentation.*

### 3.3 Severity 4 and 3 Findings

#### H-01: The holes buttons and the booking class don't match (Severity 4)

The page has two controls that look like they pick how many holes you're playing. One is the booking class at the top ("Booking as 18 Hole Groups" with a Change button), and the other is the 9 Holes / 18 Holes / Both buttons on the left. Only the booking class decides which tee times load. The buttons just filter what's already there, so if you pick a button that doesn't match your class, the list comes up empty.

![Valley View's tee time page in dark mode with three numbered boxes: 1 around Booking as 18 Hole Groups and the Change button at the top, 2 around the selected 9 Holes button on the left, and 3 around the message There are no tee times available with your current search criteria.](screenshots/annotated/fig-class-trap.png)

*Figure 2. The class trap (Valley View, Saturday Oct 10). 1: booking as 18 Hole Groups. 2: the 9 Holes button selected. 3: an empty list, even though Valley View had 9 hole times open that afternoon.*

| Booking as | Holes button | Result |
| --- | --- | --- |
| 18 Hole Groups | 18 Holes | Only 18 hole times |
| 18 Hole Groups | 9 Holes | Empty |
| 18 Hole Groups | Both | Only 18 hole times |
| 9 Hole Groups | 9 Holes | Only 9 hole times |
| 9 Hole Groups | 18 Holes | Empty |
| 9 Hole Groups | Both | Only 9 hole times |

The only thing telling you which class you're in is a small badge above the results, away from the buttons people are actually clicking. Both participants fell into this. P2 figured out the workaround after refreshing the page, but P1 never did. I rated it a 4 because P1 walked away with the wrong answer and rated their confidence 5 out of 5.

#### H-02: Same empty message no matter what went wrong (Severity 3)

This is the message from Theme 2. The page shows it whether the times are sold out, the day isn't open yet, or you're in the wrong booking class. The site has to know which one it is, since it knows every class's booking window and limits, but it never says. Both participants read it as sold out. It also tells you to adjust the holes filter, and in the H-01 case that filter is what emptied the list in the first place.

#### H-03: Both courses have separate sites, accounts, and apps (Severity 3)

Davis Park and Valley View are run by the same county on the same software, but there's no page that shows both. To compare them, you open two tabs, set the class, date, and players on each one, and remember the first course's times while you look at the second.

I used the Keystroke-Level Model (KLM) to estimate how long that takes. The KLM breaks a task into small actions and adds up a set time for each one, assuming an expert who doesn't make mistakes (MacKenzie, 2024, Ch. 7). The actions here are deciding what to do next (M, 1.35 s), moving the mouse to something (P, 1.1 s), clicking (K, 0.2 s), and waiting for the page to load (R, which I guessed at 1 s). The task I modeled is T2, finding the earliest 9 hole time for 2 players, with both sites already open.

| Step | Operators | Time |
| --- | --- | --- |
| Pick the class and wait | M P K, R | 3.65 s |
| Pick the date and wait | M P K, R | 3.65 s |
| Pick 2 players and find the earliest time | M P K, M | 4.00 s |
| **One course** | | **11.30 s** |
| Switch tabs | P K M | 2.65 s |
| Repeat on the second course | | 11.30 s |
| Remember the first course's time and compare | M | 1.35 s |
| **Two separate sites** | | **26.60 s** |
| **Both courses on one page** (pick date, pick 2 players, look once) | M P K, R, M P K, M | **7.65 s** |

Two sites take 26.6 seconds and one combined page would take 7.65, so comparing the courses takes about 3.5 times as long as it needs to. That's for an expert who never makes a mistake. On this same task, P2 hit a dead end and had to refresh, and P1 took about a minute.

#### H-04: The calendar doesn't show the booking window (Severity 3)

You can only book a few days out, and how many depends on your class. 18 Hole Groups get 4 days counting today, 9 Hole Groups and Single Golfers get 3, and the next day opens every night at 9:00 PM. The only hint on the calendar is that the days you can't book are a slightly lighter gray (`#6f777e` instead of `#333333`). It doesn't say why you can't book them or when they'll open. That's only in the welcome text, and you'd still have to count the days yourself to figure out when next Friday opens. P1 never found it. In T4 they clicked next Friday, got an empty list, and decided the courses were full.

#### H-05: The cancellation policy is hard to find and different at each course (Severity 3)

The only mention of cancelling in the welcome message is "Cancellation (see email confirmation)," so you're pointed to the rules after you've already paid. The actual policy is further down in "FOREUP TERMS & CONDITIONS," and its last line is different at each course (Section 1.2). Neither participant noticed the difference, even though the person booking has prepaid for the whole group.

#### H-06: All caps warnings instead of preventing the mistakes (Severity 3)

Instead of preventing mistakes, the courses warn about them in the welcome text: "(Double Check your DATE!!)," "Please be accurate in your bookings," and at Valley View, "Do not hit the back button or refresh during payment process. Double charge could happen." If a course has to say it in all caps, I'd guess people make that mistake a lot. She et al. (2025) rank warnings second to last in their list of ways to control errors, just above tolerating the error. Showing the date and day of the week on the pay button, and making sure a refresh can't charge you twice, would stop these mistakes instead of warning about them. I stopped before paying, so this rating is based on the courses' own warnings, not my testing.

#### H-07: The sunset cutoff isn't written anywhere, and a glitch lets you book past it (Severity 3)

The tee time list stops 100 minutes before sunset so groups can finish before dark. It's set in the page's settings (`sunset_offset: 100`), but it isn't written anywhere a golfer would see, so the list just ends in the late afternoon with no explanation. Booking itself stays open all day. Only the list gets cut off. The bigger problem is that the site sometimes glitches and shows every time, and booking one past the cutoff goes through like normal. That happened to me. I prepaid for a late tee time on ForeUp's own page, and at check-in the course told me it shouldn't have been bookable. I still got to play, but they weren't happy about it.

#### Severity 2 and 1 findings

![Valley View's class picker page with three numbered boxes: 1 around the centered welcome text with booking rules, 2 around underlined italic text that reads Stating at 9:00 pm, and 3 around the four class buttons, 18 Hole Groups, 9 Hole Groups, Single Golfers, and Season Pass.](screenshots/annotated/fig-class-picker.png)

*Figure 3. The class picker, the first screen of every booking. 1: the welcome text, all caps and centered (H-13). 2: "Stating at 9:00 pm," a typo that's underlined and italic, so it looks like a link but isn't (H-13). 3: ForeUp's pricing categories as the first decision, with Season Pass shown to everyone (H-08).*

| ID | Finding |
| --- | --- |
| H-08 | The first screen asks you to pick "18 Hole Groups," "9 Hole Groups," "Single Golfers," or "Season Pass" before you see any tee times, and nothing explains the difference. P1 said, "I didn't really pay attention to them too much." |
| H-09 | Change takes you back to the full class picker screen instead of switching on the same page. Your date and filters carry over, but every switch between 9 and 18 holes is a trip to another screen. |
| H-10 | The address stays `#/teetimes` no matter what you pick, so you can't bookmark or share a search like "Valley View, 9 Hole Groups, Saturday." P2 books once or twice a month and has to set up the same search every time. |
| H-11 | If you go to the booking address without `#teetimes` on the end, you get a Log In/Register popup over an empty "passes" page. |
| H-14 | Under 9 Hole Groups, "Both" is selected by default but only shows 9 hole times. It's a smaller version of H-01, and since it's the default, everyone sees it first. |
| H-12 | The course dropdown at the top only lists the course you're already on. |
| H-13 | The welcome text is centered, mostly in caps, and has typos ("Stating," "2 day"). When everything is bold and loud, nothing stands out, which might be part of why P1 never read the rules. |

## 4. WCAG 2.1 AA Accessibility Audit

I tested Valley View's booking pages against WCAG 2.1 AA (Kirkpatrick et al., 2018) on October 9 in Chrome. I ran an `axe-core` scan, went through the page using only the keyboard, and checked the HTML and Chrome's accessibility tree. Davis Park uses the same template, but I only tested Valley View. The full results are in [accessibility-audit.md](https://github.com/hqluke/3650-Research/blob/main/phase-1/accessibility-audit.md).

10 criteria fail, 5 of them at Level A:

| SC | Level | What fails |
| --- | --- | --- |
| 2.1.1 Keyboard | A | Tee times, filter buttons, and the desktop calendar can't be used with a keyboard |
| 4.1.2 Name, Role, Value | A | Dropdowns have no name, and filters don't say which one is selected |
| 2.4.3 Focus Order | A | Focus jumps back to the top after every class change |
| 1.3.1 Info and Relationships | A | No `<h1>` or `<main>`, and the only heading is an `<h4>` |
| 2.4.1 Bypass Blocks | A | No skip link or landmarks to jump between |
| 1.4.4 Resize Text | AA | Pinch-to-zoom is turned off |
| 4.1.3 Status Messages | AA | Result changes and the empty message are never announced |
| 1.4.3 Contrast (Minimum) | AA | The hole count badge and the site title |
| 1.3.5 Identify Input Purpose | AA | Login fields have no `autocomplete` |
| 2.4.6 Headings and Labels | AA | The previous and next day buttons are named "<" and ">" |

Focus Visible (2.4.7), Language of Page (3.1.1), Page Titled (2.4.2), and Labels or Instructions (3.3.2) pass.

### 4.1 Keyboard and Focus (SC 2.1.1, 2.4.7)

![Valley View's tee time page in the narrow layout with the keyboard Tab order marked. Badges 1 through 9 sit on the menu button, the site title link, the course dropdown, the previous day button, the date dropdown, the next day button, the terms link, the View Booking Rules link, and the Change button. One box labeled Skipped by Tab covers the time of day, player, and holes filter buttons, and another box labeled Never reached by Tab covers the list of tee times.](screenshots/annotated/fig-keyboard.png)

*Figure 4. Every Tab stop on the tee time page, in order (narrow layout). Stop 10 leaves the page and starts over at the top. The filter buttons are skipped and the tee times are never reached.*

You can't book a tee time with a keyboard. Tab only reaches nine things on the page (Figure 4), and none of them are tee times or filter buttons. The tee times are `<div>`s and the filters are links with no `href`, so the browser doesn't treat either one as something you can focus. On desktop you can't reach the calendar either. The axe scan didn't catch any of this, and I only found it by tabbing through the page.

That means anyone who uses a keyboard, a switch, or a screen reader can't book online at either course. Focus Visible passes, but only because the few things that can get focus show a ring. The fix is to make the tee times and filters real `<button>`s.

### 4.2 Screen Readers and Page Structure (SC 1.3.1, 4.1.2, 4.1.3)

I didn't test with a real screen reader, so this is based on the page's HTML and Chrome's accessibility tree.

- There's no `<h1>` or `<main>`, so there are no headings or landmarks to jump between.
- The course and date dropdowns have no labels, and the previous and next day buttons would be read as "less than" and "greater than."
- The selected filter is only shown by color, so a screen reader can't tell which one is on.
- Nothing is announced when the list changes or goes empty, because the page has no `aria-live` region. This is the screen reader side of H-02.

### 4.3 Contrast and Text Size (SC 1.4.3, 1.4.4)

Most of the text easily passes the 4.5:1 contrast minimum, but two things fail:

| Element | Colors | Ratio |
| --- | --- | --- |
| Hole count badge on every tee time | `#f0f0f1` on `#7a7575` | 3.98:1 |
| Site title in the header | `#777777` on `#ffffff` to `#f8f8f8` | 4.48 to 4.22:1 |

The hole count badge is the one that matters. It's the only thing on a tee time that says whether it's 9 or 18 holes. Darkening its background to `#5f5a5a` would raise it to 5.95:1.

The page also blocks pinch-to-zoom (`user-scalable=no`), so on a phone you can't make the 12.5 px prices any bigger. P1 used a phone for the whole session, and P2 said the policy text was "a little small and hard to read."

## 5. Limitations

- Both participants are from my family. That's enough to find problems, but not to say how common they are.
- P1 used a phone and P2 used a desktop, so I can't separate the effect of the device from the effect of experience.
- There were no 18 hole times tomorrow, so I changed T1 for both participants in different ways. That's also why P1 hit the class trap in T3 instead of T2.
- I didn't record the sessions. P2 moved too fast for me to write during the tasks, so I wrote P2's notes right after, and their per-task times are estimates.
- I was the only evaluator, and I already know the workarounds from building my own site on ForeUp's data.
- I didn't test with a real screen reader or run WAVE, I only measured Valley View for accessibility, and I didn't go past checkout.

## 6. Post-Mortem Reflection

### 6.1 How did combining qualitative user observations with an expert heuristic evaluation reveal usability flaws that a developer testing their own code would likely overlook?

I'm basically the developer testing their own code here. I built a site on ForeUp's data, so I always pick the right booking class and never see the empty list, and on my own I would have rated H-01 a 2 or 3. Watching P1 is what made it a 4. They clicked "18 Holes" on both courses, saw nothing, and decided the courses were full, with 5 out of 5 confidence. MacKenzie (2024, Ch. 3) says "programmers' discretion rules the day." The booking class makes sense if you built the system, and it only falls apart for people who didn't.

It worked the other way too. Neither participant used a keyboard or noticed the cancellation rules were different, so the expert review is what caught those. Looking back, my biggest mistake would have been testing with only P2. P2 passed four of five tasks, so I'd have said the site works, but P2 hit the same problem as P1 and just pushed through it. That's what a developer testing with people like themselves would miss.

### 6.2 Identify one heuristic violation that directly creates a legal or ethical accessibility barrier under WCAG 2.1 AA, and explain how resolving that violation improves the user experience for both disabled users and the general public.

I'd pick H-02, the empty results message. The page shows the same message whether the times are sold out, not open yet, or hidden by the booking class. It doesn't tell you what's going on (H1) or how to fix it (H9). Screen reader users have it worse. The page has no `aria-live` region, so they aren't told anything when the list changes. That fails **SC 4.1.3 Status Messages**, and since Davis County has to meet WCAG 2.1 AA under Title II (U.S. Department of Justice, 2024), it's a legal problem too.

The fix is a status message that says why the list is empty, like "No 18 hole times because you're booking as 9 Hole Groups." A screen reader would read it out and everyone else would see it, so P1 would have found the 18 hole times and P2 wouldn't have refreshed the page. Becker (2020, Ch. 2) says "A product, service, or interface that is not accessible is not usable," and here fixing one fixes the other. The keyboard failure (SC 2.1.1) is the bigger legal problem and I'd fix it first, but it mostly helps people who can't use a mouse, while fixing the empty message helps every golfer who sees it.

## 7. Documentation Links

Everything in this report comes from the files in [github.com/hqluke/3650-Research](https://github.com/hqluke/3650-Research):

| Document | Link |
| --- | --- |
| Problem statement | [phase-1/problem-statement.md](https://github.com/hqluke/3650-Research/blob/main/phase-1/problem-statement.md) |
| Research protocol | [phase-1/research-protocol.md](https://github.com/hqluke/3650-Research/blob/main/phase-1/research-protocol.md) |
| P1 field notes | [phase-1/field-notes/P1.md](https://github.com/hqluke/3650-Research/blob/main/phase-1/field-notes/P1.md) |
| P2 field notes | [phase-1/field-notes/P2.md](https://github.com/hqluke/3650-Research/blob/main/phase-1/field-notes/P2.md) |
| Synthesis | [phase-1/synthesis.md](https://github.com/hqluke/3650-Research/blob/main/phase-1/synthesis.md) |
| Heuristic evaluation | [phase-1/heuristic-evaluation.md](https://github.com/hqluke/3650-Research/blob/main/phase-1/heuristic-evaluation.md) |
| Accessibility audit | [phase-1/accessibility-audit.md](https://github.com/hqluke/3650-Research/blob/main/phase-1/accessibility-audit.md) |
| Post-mortem | [phase-1/post-mortem.md](https://github.com/hqluke/3650-Research/blob/main/phase-1/post-mortem.md) |
| Screenshots | [phase-1/screenshots](https://github.com/hqluke/3650-Research/tree/main/phase-1/screenshots) |

## 8. GenAI Documentation

I used Claude for parts of the accessibility audit. It ran axe, tabbed through the booking pages, and measured contrast in my Chrome browser, and I went over everything it found. Claude also helped make the annotated screenshots and the KLM table, and helped create the PDF and make it accessible.

## 9. References

Becker, C. R. (2020). *Learn human-computer interaction: Solve human problems and focus on rapid prototyping and validating solutions through user testing*. Packt Publishing.

Kirkpatrick, A., O Connor, J., Campbell, A., & Cooper, M. (Eds.). (2018). *Web content accessibility guidelines (WCAG) 2.1*. World Wide Web Consortium. https://www.w3.org/TR/WCAG21/

MacKenzie, I. S. (2024). *Human-computer interaction: An empirical research perspective* (2nd ed.). Morgan Kaufmann. https://doi.org/10.1016/C2022-0-02755-0

Nielsen, J. (2024). *10 usability heuristics for user interface design*. Nielsen Norman Group. https://www.nngroup.com/articles/ten-usability-heuristics/

Rivenburgh, K. (2026, April 17). *DOJ extends ADA Title II web compliance deadline 1 year*. Accessible.org. https://accessible.org/news/doj-extends-ada-title-ii-web-compliance-deadline/

She, M., Yin, Z., & Li, Z. (2025). Human error. In C. Stephanidis & G. Salvendy (Eds.), *Foundations and fundamentals in human-computer interaction*. CRC Press. https://doi.org/10.1201/9781003495109-6

U.S. Department of Justice. (2024). *Nondiscrimination on the basis of disability; Accessibility of web information and services of state and local government entities* (89 Fed. Reg. 31320). https://www.federalregister.gov/d/2024-07758
