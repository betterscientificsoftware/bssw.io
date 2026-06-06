---
name: create-bssw-blog-article
description: Use when creating, converting, or reviewing BSSw.io blog articles in Articles/Blog, especially when drafting from notes or author text, adding publication metadata, formatting deck text or hero images, placing figures, author bios, acknowledgements, DOI/cross-posting notes, or preparing formal references with wikize_refs.py.
---

# Create BSSw Blog Article

Use this skill to create or revise blog articles under `Articles/Blog/` in the `bssw.io` repository.

## Core Workflow

1. Gather the article facts: title, authors and profile links, target publication date, desired track, topics, deck text or hero image, body text, figures, acknowledgements, DOI, cross-posting note, author bios, and source links or formal citations.
2. Inspect recent nearby articles before writing. Prefer recent patterns over the older skeleton when they disagree. Good examples include:
   - `Articles/Blog/2027-05-rse-genai.md` for multi-author, cross-posted, figure-heavy, formally cited articles.
   - `Articles/Blog/2026-05-modern-memory-safe-cpp.md` for a long deep-dive with formal citations.
   - `Articles/Blog/2026-04-mpi-debugging.md` for a single-author fellowship article with body images.
   - `Articles/Blog/2026-04-everse.md` for a community/project article with hero image and multiple bios.
3. Read the compact format guide when needed: `references/blog-article-format.md`.
4. Create or update the article as `Articles/Blog/YYYY-MM-short-slug.md`, using the expected publication year and month unless the user specifies another naming plan.
5. Add images under `images/` and reference them as `../../images/name.ext`. Use slug-aligned names such as `2027-05-rse-genai-figure1.png`.
6. If the article uses formal citations, edit only the human-authored source references, then run `utils/wikize_refs.py` as described in `.skills/wikize-refs/SKILL.md`. Do not hand-edit the generated `sfer-ezikiw` block unless the user explicitly asks for a displayed-reference formatting change.
7. Verify the article before finishing.

## Article Structure

Use this order for most new deck-text blog articles:

```markdown
# Title in Headline Style

#### Contributed by [Firstname Lastname](https://github.com/user), [Second Author](https://example.org), and [Final Author](https://github.com/final)

#### Publication date: Month D, YYYY

<!-- begin deck -->
One or two concise sentences with no links.
<!-- end deck -->

Article body starts here.

## Body section

More content.

<br>
<img src='../../images/article-figure1.png' class='page lightbox' alt="Short accurate alt text"/>Figure 1: Optional caption.
<br>

## Acknowledgements

Optional acknowledgement text.

DOI: [10.xxxx/example](https://doi.org/10.xxxx/example)

Optional cross-posting note.

## Author bio

Single-author bio paragraph.

<!---
Publish: yes
Track: Community
Pinned: no
Topics: research software engineers, strategies for more effective teams
--->

<!--- References --->
```

For hero-image articles, place the `**Hero Image:**` block immediately after the title. Blog house style normally prefers either a hero image or deck text, but keep both when the user or editor says the deck text should appear as opening body text. Treat the checker's hero-plus-deck warning as non-actionable in that case. For multi-author articles, use `## Author bios` and one paragraph per author, normally in the same order as the contributor line unless the draft or user indicates another order.

## Writing Rules

- Keep the title as the only level-one heading. Body sections start at `##`.
- Use `#### Contributed by ...` and `#### Publication date: Month D, YYYY` near the top.
- Use `<!-- begin deck -->` and `<!-- end deck -->` for current blog deck text. Keep the deck to one or two sentences and do not include links. If a hero image is also present and the deck is intentionally retained, leave the deck block in place.
- Prefer third-person, reader-centered prose. For editorial conversions, preserve author voice while tightening repetition, date references, and unclear transitions.
- Keep blog length flexible. The author guide suggests 500-1,500 words for many articles; deep dives and community reports may be longer when the topic warrants it.
- Limit figures, tables, and links unless they directly support the article.
- Use ASCII punctuation in newly drafted text unless preserving author-provided names, titles, or quotations requires Unicode.
- Preserve unrelated local changes. Check `git status --short` before and after edits when making article changes.

## Metadata

Every blog article needs a formatted metadata comment near the end. Set `Publish: yes` for articles you create or edit unless the user explicitly asks for a draft or unpublished article:

```markdown
<!---
Publish: yes
Track: Community
Pinned: no
Topics: software engineering, testing
RSS update: 2026-05-28
--->
```

Required fields are `Publish`, `Track`, and `Topics`. `Pinned` is commonly present. `RSS update` is optional and should normally be added only for publication, republishing, or feed-visible updates.

Common tracks:

- `Community`
- `Deep Dive`
- `Experience`
- `How to`
- `Bright Spots`
- `BSSw Fellowship`

Choose a small set of existing topics from `docs/pages/bssw/bssw_content_metadata.md`. Match nearby article spelling and capitalization where possible.

## Figures and Images

- Store all images in `images/`.
- For hero images, use the finicky list-item syntax exactly:

  ```markdown
  **Hero Image:**

  - <img src='../../images/YOUR-IMAGE-NAME.png' />
  ```

- Include meaningful `alt` text for hero images; avoid generic text such as `alt="hero image"`.
- For body images, use HTML image tags, not Markdown image syntax.
- Include `class='page lightbox'` for diagrams or detailed figures that should expand; use `class='page'` for ordinary page-width images and `class='logo'` for logos or headshots.
- Include meaningful `alt` text.
- Place captions immediately after the image tag and avoid links in captions.
- Add `<br>` before and after body images unless the following line is a heading.

## References

For articles with many external sources, sensitive claims, research literature, or formal citation needs:

1. Use source reference definitions above the generated block:

   ```markdown
   [short-label]: https://doi.org/example "Short title {Full bibliographic text.}"
   ```

2. Cite in body text with `<sup>[short-label]</sup>` or `<sup>[label1],[label2]</sup>`.
3. Run `utils/wikize_refs.py -i Articles/Blog/file.md` from the repository root, preferably through `uv run python` if invoking Python directly is needed.
4. Review the diff and confirm the generated `sfer-ezikiw` block is present and idempotent.

If the user has manually edited displayed reference text or asks for displayed-reference formatting changes, do not rerun `wikize_refs.py` afterward unless they explicitly permit regeneration. Common manual display edits include changing `### References` to `## References`, removing generated short titles, and removing generated `<br>` tags. Preserve link anchors, numbered footnote definitions, and URLs while making those display-only edits.

## Verification

Before final response:

1. Read the new or edited article.
2. Run the local checker:

   ```bash
   uv run python .skills/create-bssw-blog-article/scripts/check_blog_article.py Articles/Blog/path-to-file.md
   ```

3. If formal citations changed and the displayed references have not been manually customized, run or rerun:

   ```bash
   uv run python utils/wikize_refs.py -i Articles/Blog/path-to-file.md
   ```

4. Run `codespell Articles/Blog/path-to-file.md` if available.
5. Run `git diff -- Articles/Blog/path-to-file.md` and review the actual changes. For a new untracked file, use `git diff --no-index -- /dev/null Articles/Blog/path-to-file.md`.
6. Report the article path, important metadata choices, citation/image checks, intentional checker warnings such as accepted hero-plus-deck usage, and any checks that could not be run.
