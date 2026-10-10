## CS 3650 Human-Computer Interaction - Research Repository

Luke Peterson, Weber State University, Fall 2026

This repo is the documentation trail for my CS 3650 research project. It has my research protocol, raw field notes, audit evidence, and the reports I build from them. I try to commit raw notes the day I take them. The Phase 1 sessions were on October 9, 2026, and everything was committed the next day.

### Layout

| Folder | What's in it |
| --- | --- |
| `reference/` | Study sheets on the methods and standards I'm auditing against |
| `phase-1/` | Phase 1: Contextual Research & Diagnostic Usability Audit (due Oct 9, 2026) |

Inside `phase-1/`:

| Path | What's in it |
| --- | --- |
| `problem-statement.md` | The system I picked, who uses it, their core tasks, and why the friction matters |
| `research-protocol.md` | My interview and observation script |
| `field-notes/` | Raw notes, one file per session, not cleaned up. Participants are only called P1 and P2 so they stay anonymous |
| `synthesis.md` | Pain points, quotes, mental model mismatches, and breakdowns |
| `heuristic-evaluation.md` | Nielsen's 10 heuristics audit with severity ratings |
| `accessibility-audit.md` | WCAG 2.1 AA audit |
| `post-mortem.md` | The two post-mortem reflection answers |
| `screenshots/` | Raw and annotated screenshots. Each finding names the screenshots that back it up |
| `Phase1_Usability_Audit.md` | Source for the report |
| `Phase1_Usability_Audit.pdf` | The report I submit, built from the markdown with `build_pdf.py` |
| `build_pdf.py` | Builds the accessible (PDF/UA-1) PDF. Needs `pip install markdown pikepdf` and Chrome |
