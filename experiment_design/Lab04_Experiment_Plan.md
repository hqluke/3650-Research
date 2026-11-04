# Lab 04: Experiment Design & Variable Formulation Plan

**Finding a Tee Time Across Davis County's Two Public Golf Courses**

Luke Peterson · CS 3650 Human-Computer Interaction · Weber State University · November 2026

Research repository: [github.com/hqluke/3650-Research](https://github.com/hqluke/3650-Research)

## 1. Task Selection & Problem Framing

The flow is finding a tee time when you'd play at either Davis Park or Valley View. Both Phase 1 participants got stuck here, and when it goes wrong there's no error. You just think the course is full.

| | Interface A (baseline) | Interface B (treatment) |
| --- | --- | --- |
| What it is | ForeUp's live booking sites | My [Case Study 02 prototype](https://hqluke.github.io/3650-Case-Study-02/) |
| Courses | Two separate sites | Both in one list |
| 9 vs 18 holes | A hidden booking class plus 9 / 18 buttons that only filter | One Holes control |
| Cancellation rules | In the terms, different at each course | On the pay step for both courses |

I'm testing three problems from Phase 1. Comparing courses on ForeUp means redoing everything on a second site and remembering what the first one showed. The 9 / 18 buttons and the booking class can disagree, which shows an empty list, and that's how P1 decided there were no 18 hole times when there were (H-01). And neither participant noticed the two courses have different cancellation rules (H-05). The prototype should be faster, lose fewer tee times, and make the rules easier to find.

## 2. Hypotheses

Each one is tested at p < .05.

| | H1 | H0 |
| --- | --- | --- |
| Time | B users find a tee time significantly faster than A users | No significant difference in time on task |
| Lost tee times | B users lose significantly fewer tee times than A users | No significant difference in lost tee times |
| Rules | B users answer the cancellation question correctly more often | No significant difference in correct answers |
| Ease | B users rate the tasks significantly easier (SEQ) | No significant difference in SEQ ratings |

## 3. Variables

### 3.1 Independent Variable

The independent variable is **booking interface**: A (ForeUp) or B (prototype). I thought about making the holes control, the combined courses, and the rules three separate variables, but that's 8 groups and 40+ people. MacKenzie (2024, Ch. 5) says a variable that covers several changes should be named for all of them, so it's the interface and not one feature. The catch is that if B wins, I can't say which change did it.

### 3.2 Tasks

| Task | Read to participant |
| --- | --- |
| T1 | "You and a friend want to play 9 holes tomorrow afternoon. Which course has the earliest time after 12 PM? Go as far as you can without paying." |
| T2 | "Now four of you want to play 18 holes tomorrow after 2 PM at either course. Find the earliest time." |
| T3 | "Say you booked that time and something comes up 90 minutes before. What happens to your money? Would it be different at the other course?" |

T2 comes right after T1 on purpose. On ForeUp you're still in "9 Hole Groups," so clicking "18 Holes" shows nothing, which is the trap P1 (Participant #1 from phase 1 testing) hit. I check the right answers on both interfaces right before each session.

### 3.3 Dependent Variables

Full definitions are in [`data_dictionary.csv`](data_dictionary.csv).

| Measure | Variable | How |
| --- | --- | --- |
| Efficiency | `Task_Completion_Time_sec` | From the screen recording, start of the task to their answer or the payment step. 180 s cap counts as a fail |
| Effectiveness | `Task_Success_Binary` | 1 if the answer matches the key with no hint |
| Effectiveness | `Lost_Time_Binary` | 1 if they say nothing's open, or pick a later time, when an earlier one existed |
| Effectiveness | `Rules_Correct_Score` | T3 only, 1 point per course they get right (0-2) |
| Satisfaction | `SEQ_Rating` | After each task, 1 (very hard) to 7 (very easy) |

I wanted people to rank which site was easier, but each person only sees one, so the SEQ does that job. Nobody thinks out loud during the timed tasks since that adds time.

### 3.4 Confounds and Controls

| Confound | Control |
| --- | --- |
| Booking experience. P2 had used ForeUp and got through faster than P1 | Assign A and B evenly inside experience groups (Section 4) |
| Phone vs computer | Everyone uses my laptop in a fresh Chrome guest profile at 1920 x 1080 |
| ForeUp's times are live and the prototype's are fake | Run both on the same evenings, pin the prototype clock with `?now=`, and end before the 9 PM window opens |
| ForeUp makes you log in before paying | Stop the timer at the step before login or payment on both |
| Screen readers can't pick a tee time on ForeUp at all (A-01) | Left out. That needs its own study |
| I built B, so I might help those people more | Same script and prompts for everyone, and no help until 3 minutes |

## 4. Experiment Design

### 4.1 Between-Subjects

Each person uses one interface. These are finding tasks, and you can't unlearn an answer. Someone who used the prototype first would already know the earliest time when they got to ForeUp. MacKenzie (2024, Ch. 5) says between-subjects groups can be balanced "by explicitly placing participants in groups according to reasonable criteria," and participants shouldn't pick their own condition.

Each person is screened into one of three experience groups: never booked online (like P1), booked online but not on ForeUp, or booked on ForeUp at these courses (like P2). Each group has an envelope with 2 A slips and 2 B slips. People draw one without looking, so every group ends up with 2 on A and 2 on B.

### 4.2 Participants

12 total, 6 per condition. Participants are golfers 18 or older who would book their own tee time and can read English. P1 and P2 are excluded because I explained the booking classes to them after Phase 1, and so is anyone who's used my prototype. I'm not screening for how well people think or read. If someone wants to play golf they can probably book a tee time, and if they can't, that's the site's fault. I'd include 16 and 17 year olds with a parent's consent, but that adds steps, so I set it at 18. Six per group is small, so only a big difference will show up as significant.

## 5. Ethics

Khalid et al. (2025) list consent, confidentiality, and risk of harm as the three things to cover. People only show up as P01-P12, the recording only shows the screen and gets deleted once the times are written down, and nobody pays for anything.

> Thanks for helping me out. This is for my HCI class at Weber State. I'm comparing golf booking websites to see which one makes it easier to find a tee time. **The websites are being tested, not you.** Nothing today says anything about how smart you are or how good you are with computers. If something is confusing, that's the website's fault, and it's what I'm trying to find.
>
> I'll give you three short tasks and time each one. Please don't talk through them, just do them like you would at home. **Don't pay for anything.** If it asks you to log in or for a card, stop and tell me. I'll record the screen, not your face, and your name won't be in anything I turn in. You can stop at any time. Is it okay if we start?

## 6. Post-Mortem Reflection

### 6.1 Why is it critical in HCI empirical research to distinguish between statistical significance (p < .05) and practical significance (real-world clinical or operational impact) when evaluating interface performance metrics?

Statistical significance is proved by the numbers, and practical significance depends a lot on context. MacKenzie (2024, Ch. 5) says that with enough participants you'll get "statistically significant results for a small difference of no practical significance." If B saves 4 seconds, a big study might prove it, but no golfer would care.

My study has the opposite problem. With 6 per group, if 3 ForeUp users lose a tee time and no prototype users do, Fisher's exact test gives p = .091, which isn't significant. But half of ForeUp users thinking a course is full is a lost round for the golfer and a lost green fee for the county. So I'll report the raw counts next to every p-value and won't call a non-significant result "no difference." The real fix is testing with a lot more participants.

### 6.2 If you chose a Within-Subjects design, what specific asymmetric transfer or carryover effects could occur between interface conditions, and how does your counterbalancing matrix mathematically isolate that bias?

I didn't use within-subjects, and carryover is the reason. Someone who used the prototype first would already know the earliest tee time at both courses, so on ForeUp they'd never hit the booking class trap I'm trying to measure. ForeUp first wouldn't give away nearly as much, so the carryover goes mostly one way. An AB / BA counterbalance can't cancel that out. MacKenzie (2024, Ch. 5) says "the simplest way to avoid asymmetric skill transfer is to use a between-subjects design." The trade-off is needing twice as many people.

## 7. Documentation Links

[`data_dictionary.csv`](data_dictionary.csv) defines every variable, and [`session_sheet.csv`](session_sheet.csv) is the blank data sheet. The findings come from [`../phase-1/`](../phase-1/), and Interface B is the [Case Study 02 repo](https://github.com/hqluke/3650-Case-Study-02).

## 8. GenAI Documentation

I used Claude to help run the Fisher's exact numbers and make the CSV files. Every claim about users comes from my Phase 1 field notes.

## 9. References

Khalid, M., Fernández Castillo, G., & Salas, E. (2025). Applying the science of social and organizational psychology to HCI. In C. Stephanidis & G. Salvendy (Eds.), *Foundations and fundamentals in human-computer interaction*. CRC Press. https://doi.org/10.1201/9781003495109-9

MacKenzie, I. S. (2024). *Human-computer interaction: An empirical research perspective* (2nd ed.). Morgan Kaufmann. https://doi.org/10.1016/C2022-0-02755-0
