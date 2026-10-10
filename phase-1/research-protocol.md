## User Research Protocol

### Goal

Watch how real people find and book tee times at Davis Park and Valley View with ForeUp, and see where they get stuck. The problem statement lists the friction I expect, but I already know how ForeUp works, so I need to see what happens to people who don't. I'm mostly looking for:

- How people pick a booking class, and what they think "18 Hole Groups," "9 Hole Groups," and "Single Golfers" mean
- How they compare the two courses when they're on two separate sites
- What they think an empty list means (sold out, not open yet, or wrong class)
- Whether they find the rules (booking windows, sunset cutoff, cancellation) before they'd commit money

### Method

Each session is a think-aloud in the style of a contextual inquiry. The participant does realistic tasks on their own device and talks out loud while I watch and take notes, then we do a short semi-structured interview. Each session is about 30-40 minutes.

Becker (2020, Ch. 5) calls this moderated observation: you give the user a task and check it against success criteria. The downside is that people act differently when they know they're being watched, so just observing would be more natural. But nobody books a tee time on a schedule I can sit in on, and I can't see what someone is thinking on a booking page unless they say it, so think-aloud is worth it here.

They use whatever device they'd normally book on, because that's the real context. If they'd normally use their phone, we use their phone.

### Participants

| ID | Who | Why they're in the study |
| --- | --- | --- |
| P1 | Family member, older generation | Stands in for the older end of the user base. The warm-up covers how much they've booked online before |
| P2 | Family member, younger generation | Pretty tech literate. Stands in for the younger, confident end of the user base |
| P3 | *(optional)* A friend I golf with | Actually books on these courses. Would make it 3 users, and one of them an active user |

Participants are only called P1, P2, and P3 in my notes and the report. I don't say how they're related to me beyond "family member" for the same reason.

Since they're family, they might go easier on the site or try to impress me. I'll tell them I didn't build this website (true, I didn't build ForeUp) so they can't hurt my feelings, and I won't show them my own tee time site at any point. I'll run each session separately so nobody watches someone else do the tasks first.

Two or three people from one family can't stand in for every golfer in Davis County, so in the report I'll treat this as finding problems, not measuring how common they are.

For ethics, Khalid et al. (2025) list consent, confidentiality, and risk of harm as the things to cover. The intro script explains what we're doing and asks if it's okay before we start. Only P1, P2, and P3 show up in anything I turn in. Nobody pays for anything or makes a real booking, and they can stop whenever they want.

### Before Each Session

- [ ] Write down the date and start time. Windows open at 9:00 PM and the sunset cutoff moves every day, so what's bookable depends on when we do this. Run all sessions on the same evening before 9 PM if I can.
- [ ] Check the right answers for Tasks 2 and 3 myself right before the session, so I can tell if they got it right.
- [ ] Open a blank browser tab. They start from there, not from a booking page, so I see how they'd actually find it.

I'm taking notes instead of recording. Without a recording my notes are the only record, so I'll write quotes down word for word as they're said, timestamp the log table, and write first impressions right after each session. I'll still miss things while I'm writing, and I won't have anything to check my memory against later.

### Intro Script

> Thanks for helping me out. This is for my HCI class. I'm testing a golf booking website, not you, so if something is confusing that's exactly what I want to find out. I didn't make this website, so you won't hurt my feelings. While you go, please say out loud whatever you're thinking, like what you're looking for, what you expect to happen, and anything that surprises or annoys you. I'm not going to help you much, because I want to see what you'd do on your own. **Please don't actually pay for anything.** When you get to the point where it asks for a card, or to log in, stop and tell me. You can stop at any time. I'll be taking notes while you go. Is that okay? Your name won't be in anything I turn in.

### Warm-Up Questions

Every question asks for a story instead of a yes or no, since Becker (2020, Ch. 5) says to cut yes/no, multiple choice, and leading questions.

1. Tell me about how golf fits into your life. How often, and where?
2. Walk me through the last time you got a tee time. Who booked it, and how?
3. Tell me about any time you've booked a tee time online, at any course.
4. What other kinds of things do you book online, and what's that usually like?
5. If you were booking a tee time tonight, what would you use to do it?

Probes to use on any answer: "Tell me more about that." "What do you mean by that?" "Why do you think that is?"

### Tasks

The tasks are written as situations, not instructions. I never say "booking class" or tell them which button to press. I'll read each one out loud and also give it to them on paper so they don't have to remember it.

| Task | Read to participant | Done when | What I'm watching for |
| --- | --- | --- | --- |
| T1. Book for a group | "You and three friends want to play 18 holes at Davis Park tomorrow, sometime after 2 PM. Find a time and go as far as you can without paying." | They pick a time after 2 PM for 4 players, 18 holes, tomorrow, and reach the payment or login step | How they find the site. Which class they pick and why. Picking the date and the number of players. Whether they notice the prepay rule and where the times end in the evening |
| T2. Compare the courses | "Your friend thinks Valley View might have something earlier. For 2 people playing 9 holes the day after tomorrow, which course has the earliest tee time, Davis Park or Valley View?" | They give an answer and I check it | How they get to the other course. Coming off T1 they'll still be booking as 18 Hole Groups, so whether they click the 9 Holes filter, what they make of the empty message, and whether they ever find the Change button. Whether they redo the class and date. Whether they write things down, flip tabs, or misremember what the first course had |
| T3. Go as a single | "Now you're going by yourself. What's the latest time tomorrow you could play at either course?" | They give an answer and I check it | Whether they find Single Golfers or stay in a group class and miss last spot times. What they think when the times stop in the late afternoon |
| T4. Booking window | "You want to play 18 holes with a group next Friday. Can you book it right now? If not, when will you be able to?" | They give an answer | What they think the empty list means. Whether they find the policy text and can turn "3 days in advance, starting at 9:00pm" into an actual day and time. I'm not 100% sure of the exact answer myself, which says something too |
| T5. Cancellation | "Say you booked tomorrow at 10 AM and something comes up at 8:30 AM. What happens to your money? Would it be different at the other course?" | They give an answer | Where they look for the policy (welcome message, terms, "see email confirmation"). Whether they notice the two courses have different rules. 8:30 is 90 minutes out on purpose: Davis Park gives a full rain check and Valley View gives nothing |

If they get stuck, I don't help unless it's been about 3 minutes or they say they'd give up. Then I mark the task as failed, give the smallest hint I can, and mark it assisted if they finish.

I'll only use neutral prompts so I don't lead them:

- "What are you thinking right now?"
- "What are you looking for?"
- "What did you expect to happen there?"
- "What would you do next if I wasn't here?"

### After Each Task

1. "Overall, how easy or hard was that, from 1 (very hard) to 7 (very easy)?"
2. "How sure are you that your answer is right, from 1 to 5?"
3. "Walk me through what just happened, in your own words."
4. "What did you expect to happen that didn't?"

### What I Record for Each Task

I'm deciding how each thing gets measured ahead of time so the notes are consistent across sessions.

| Measure | How |
| --- | --- |
| Result | Success, assisted, or failed |
| Time on task | Start and end time from my watch |
| Errors | Wrong class, wrong date, wrong course, wrong player count, wrong answer |
| Backtracks | Times they hit Back, reloaded, or started over |
| Ease and confidence | From the first two questions above |
| Quotes | Word for word, with a timestamp |
| Breakdowns | Any point where what they expected and what happened didn't match |

I want the confidence score next to the actual result. Someone who's sure they're right and is wrong (like saying nothing's open when there is) is worse off than someone who's unsure, because they'll just give up.

### Debrief Interview

1. Which part took the most effort? Tell me about it.
2. When you first saw "18 Hole Groups," "9 Hole Groups," and "Single Golfers," what did you think they meant?
3. When the list said nothing was available, what did you think that meant?
4. Tell me about going from Davis Park's site to Valley View's.
5. How would you feel about paying for your whole group on this site?
6. If you could change one thing, what would it be, and why?
7. What else did you notice that we haven't talked about?

After the debrief I'll explain how the booking classes and windows actually work, in case they ever book on it for real.

### Field Notes

Raw notes go in `field-notes/`, one file per session (`P1.md`, `P2.md`, and `P3.md` if I get a third person), committed without cleaning them up. The blank files are set up ahead of time with the answer key, every task, the measures above, a running log table, and the debrief questions, so I'm not flipping back to this protocol during a session. Each one ends with first impressions I write right after the session.

### References

Becker, C. R. (2020). *Learn human-computer interaction: Solve human problems and focus on rapid prototyping and validating solutions through user testing*. Packt Publishing.

Khalid, M., Fernández Castillo, G., & Salas, E. (2025). Applying the science of social and organizational psychology to HCI. In C. Stephanidis & G. Salvendy (Eds.), *Foundations and fundamentals in human-computer interaction*. CRC Press. https://doi.org/10.1201/9781003495109-9
