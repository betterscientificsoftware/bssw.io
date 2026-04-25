---
name: create-bssw-event
description: Use when creating or updating BSSw.io event listings in the Events directory, especially when a user provides an event URL, asks to add a conference/workshop/webinar/school/survey/event announcement, or wants a future event file drafted in the repository's Markdown style.
---

# Create BSSw Event

Use this skill to add or update event listings under `Events/` in the `bssw.io` repository.

## Core Workflow

1. Gather event facts from the official event page or announcement. If the user provides a URL, open it and extract dates, deadlines, location, organizers, eligibility limits, cost, application/registration links, and program topics.
2. Inspect nearby or similar files in `Events/` before writing. Prefer a recent, closely related event as the pattern.
3. Check the event styling guidance only as needed:
   - `docs/pages/bssw/bssw_styling_event.md`
   - `docs/pages/bssw/bssw_styling_common.md`
   - `docs/pages/bssw/bssw_content_metadata.md`
4. Create or update a Markdown file in `Events/`. Prefer `YYYY-MM-short-slug.md` for dated events unless the repository already uses a specific event-series naming pattern.
5. Keep wording third-person, timeline-neutral where possible, and concise. Do not copy the full event page.
6. Verify formatting and metadata before finishing.

## Event File Pattern

Use this structure for most conferences, workshops, schools, bootcamps, and calls for participation:

```markdown
# Event Title

<!-- deck text start -->
One or two timeline-neutral sentences describing what the event is and who it serves. Avoid links, "applications now open", "call for submissions", and other time-sensitive phrasing in deck text.
<!-- deck text end -->

- Application Deadline: Month D, YYYY
- Event Dates: Month D-D, YYYY
- Location: City, ST, USA
- Event Website: https://example.org/event
- Organizers: Organizer Name

#### Contributed by [Contributor Name](https://github.com/contributor)

#### Publication date: Month D, YYYY

Event Information | Details
:--- | :---
Event Name | [Event Title](https://example.org/event)
Application Deadline | Month D, YYYY
Event Dates | Month D-D, YYYY
Website | https://example.org/event

## Description

Short third-person description of the event.

## Target Audience

Who the event is intended for and any eligibility constraints.

## Program Topics

- Topic 1
- Topic 2
- Topic 3

Please check the [event website](https://example.org/event) for full details and updates.

<!---
Publish: yes
Topics: conferences and workshops, software engineering
--->
```

Adapt the table rows to the source. Common rows include `Abstract Deadline`, `Submission Deadline`, `Application Deadline`, `Event Date`, `Event Dates`, `Date and Time`, `Presenter`, `Website`, and `Limits on participation`. Do not include empty rows.

Do not include `Location`, notification dates, or costs in the event information table. Keep location in the deck attributes and, if useful, in the body text. Mention costs or travel support in the body only when important to participants.

Do not include separate `Application`, `Registration`, or `Registration and Other Information` rows when the event website already links to the application or registration page. Use a separate application or registration row only when there is no broader official event page and that link is the primary official event URL.

## BSSw Style Rules

- Use level-one heading only for the title. Body section headings start at `##` and must be properly nested without skipping levels. The `#### Contributed by ...` and `#### Publication date: ...` deck headings are the only expected exceptions.
- Use deck comments exactly as `<!-- deck text start -->` and `<!-- deck text end -->`.
- Keep deck text to one or two sentences and do not include links in it.
- Use physical location for in-person events, `Online` for online events, and `City, ST and online` for hybrid events.
- Include "The current deadline is ..." and "Please see the event website for deadline updates." when deadlines may change.
- Use absolute URLs for external event pages.
- Prefer official event URLs over third-party pages or search results.
- Use ASCII punctuation in new event files unless the surrounding file already intentionally uses Unicode.
- Preserve unrelated local changes. Check `git status --short` before and after edits.

## Contributors

If the event page identifies the submitter or author and the repository has used that person as contributor before, reuse the same contributor format. Otherwise, use:

```markdown
#### Contributed by BSSw.io team
```

Use the current date as the publication date unless the user specifies a publication date.

## Metadata Topics

Choose a small, relevant set of existing BSSw topics. Useful event topics often include:

- `conferences and workshops`
- `in-person learning`
- `online learning`
- `software engineering`
- `software sustainability`
- `research software engineers`
- `testing`
- `peer code review`
- `continuous integration testing`
- `documentation`
- `licensing`
- `reproducibility`
- `software publishing and citation`
- `strategies for more effective teams`
- `funding sources and programs`

Match capitalization and spelling to nearby published files when possible.

## Verification

Before final response:

1. Read the new or edited file.
2. Run `rg -n "[^\x00-\x7F]" Events/path-to-file.md` to catch accidental non-ASCII characters.
3. Run `codespell Events/path-to-file.md` if `codespell` is available.
4. Run `git diff -- Events/path-to-file.md` and review the actual changes.
5. Report the file path, main facts captured, and any checks that could not be run.
