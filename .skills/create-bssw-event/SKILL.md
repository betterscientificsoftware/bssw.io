---
name: create-bssw-event
description: Use when creating or updating BSSw.io event listings in the Events directory, especially when a user provides an event URL, asks to add a conference/workshop/webinar/school/survey/event announcement, or wants a future event file drafted in the repository's Markdown style.
---

# Create BSSw Event

Use this skill to add or update event listings under `Events/` in the `bssw.io` repository.

## Core Workflow

1. Gather event facts from the official event page or announcement. If the user provides a URL, open it and extract dates, deadlines, location, organizers, eligibility limits, cost, application/registration links, and program topics. If the page lists both upcoming and past events, use the clearly marked upcoming event unless the user asks for an archive entry.
2. Inspect nearby or similar files in `Events/` before writing. Prefer a recent, closely related event as the pattern.
3. Check the event styling guidance only as needed:
   - `docs/pages/bssw/bssw_styling_event.md`
   - `docs/pages/bssw/bssw_styling_common.md`
   - `docs/pages/bssw/bssw_content_metadata.md`
4. Create or update a Markdown file in `Events/`. Prefer `YYYY-MM-short-slug.md` for dated events unless the repository already uses a specific event-series naming pattern.
5. Keep wording third-person, timeline-neutral where possible, and concise. Do not copy the full event page.
6. Verify formatting and metadata before finishing.

## Fact Gathering Rules

- Prefer official event URLs over third-party pages, search results, and inferred dates.
- If the official page appears stale, cached, or ambiguous, fetch it directly with no-cache headers or another primary-source route before deciding which event to draft.
- Do not infer missing years from third-party listings when official page context, calendar data, or live HTML can answer the question.
- For event times, list only the natural timezone of the host organization when that can be determined. Check whether the event date falls under standard time or daylight saving time, and correct timezone abbreviations when the source page is wrong.

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

Adapt the table rows to the source. Common rows include `Abstract Deadline`, `Submission Deadline`, `Application Deadline`, `Event Date`, `Event Dates`, `Date and Time`, `Presenter`, `Website`, `Registration`, and `Limits on participation`. Do not include empty rows.

Do not include `Location`, notification dates, or costs in the event information table. Keep location in the deck attributes and, if useful, in the body text. Mention costs or travel support in the body only when important to participants.

Use the broader official event page for `Website`. Add a separate `Registration` row when the official event page exposes a direct registration link that is useful to participants. Use a separate `Application` row only when the application link is distinct from the broader official event page and important to the event workflow.

## BSSw Style Rules

- Use level-one heading only for the title. Body section headings start at `##` and must be properly nested without skipping levels. The `#### Contributed by ...` and `#### Publication date: ...` deck headings are the only expected exceptions.
- Use deck comments exactly as `<!-- deck text start -->` and `<!-- deck text end -->`.
- Keep deck text to one or two sentences and do not include links in it.
- Use physical location for in-person events, `Online` for online events, and `City, ST and online` for hybrid events.
- Include "The current deadline is ..." and "Please see the event website for deadline updates." when deadlines may change.
- Use absolute URLs for external event pages.
- Prefer official event URLs over third-party pages or search results.
- For body text, use the official event abstract or description verbatim when it is concise enough for a BSSw event entry. Summarize only when the source text is too long, too detailed, or unsuitable for direct reuse.
- Use ASCII punctuation in new event files unless the surrounding file already intentionally uses Unicode.
- Preserve unrelated local changes. Check `git status --short` before and after edits.

## Contributors

Base the `Contributed by` field on the identity of the user creating the event when that can be determined. Prefer an existing contributor format already used in the repository for that person.

To determine the contributor, use the conversation context first. If needed, check local Git config such as `git config user.name` and search existing files for that name or GitHub handle. Use a linked contributor line when a confident match is found:

```markdown
#### Contributed by [Contributor Name](https://github.com/contributor)
```

Fall back to the BSSw.io team language only when the creator's identity or GitHub profile cannot be determined confidently:

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
4. Run `git diff -- Events/path-to-file.md` and review the actual changes. For an untracked new file, `git diff -- path` is empty; use `git diff --no-index -- /dev/null Events/path-to-file.md` instead.
5. Report the file path, main facts captured, and any checks that could not be run.
