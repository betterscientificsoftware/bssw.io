---
name: Wikize Refs
description: Use when editing BSSw.io markdown files that need formal external citations/references, when converting inline external links into BSSw reference-style links, or when running `utils/wikize_refs.py` to regenerate or verify the auto-generated references block.
---

# Wikize Refs

Use this skill for BSSw.io `*.md` files that manage external references with `utils/wikize_refs.py`.

## Canonical References

Read only what you need:

- Citation syntax, footnote style, and generated-block behavior:
  [`docs/pages/bssw/bssw_wikize_refs.md`](../../docs/pages/bssw/bssw_wikize_refs.md)
- When formal citations are appropriate, plus DOI/internal-vs-external link rules:
  [`docs/pages/bssw/bssw_styling_common.md`](../../docs/pages/bssw/bssw_styling_common.md)
- Review and pre-publish expectations:
  [`docs/pages/bssw/bssw_content_publishing.md`](../../docs/pages/bssw/bssw_content_publishing.md)
- Tool invocation details and common modes:
  [`utils/README.md`](../../utils/README.md)

## Compact Workflow

1. Inspect the target `*.md` file and confirm formal citations are warranted for this content type and article length.
2. Keep the author-managed source references as column-0 GFM reference definitions, usually near the end of the file above the auto-generated block:
   `[label]: URL "Short title {Full bibliographic text}"`
3. In body text, cite with `<sup>[label]</sup>` or `<sup>[label1],[label2]</sup>`. Follow BSSw punctuation guidance and use straight quotes only in reference definitions.
4. Prefer DOI URLs when available. Use absolute URLs for external resources and relative `.md` links for BSSw internal content.
5. Do not hand-edit anything containing `sfer-ezikiw` or the generated `### References` section. Regenerate it with the tool.
6. From the repo root, normally run:

   ```bash
   ./utils/wikize_refs.py -i path/to/file.md
   ```

   Useful alternatives:

   ```bash
   ./utils/wikize_refs.py -o /tmp/file-gen.md path/to/file.md
   ./utils/wikize_refs.py -u path/to/file.md
   ./utils/wikize_refs.py --help
   ```

7. Review the diff. Expected results:
   - inline `<sup>[label]</sup>` citations rewritten to generated numeric refs such as `<sup>[1]</sup>`
   - original link definitions renamed with `-sfer-ezikiw`
   - a generated `### References` section appended
   - rerunning the tool should be idempotent
8. `-i` creates `file.md~` unless `-s` is used. Handle that backup intentionally and do not commit it by accident.
9. Before finalizing content for publishing, ensure the file has been rerun through `wikize_refs.py -i`.

## Examples

- Current article example:
  [`Articles/Blog/2026-03-modern-memory-safe-cpp.md`](../../Articles/Blog/2026-03-modern-memory-safe-cpp.md)
- Historical applications found in git history:
  `e8c606ee`, `f1421315`, `c20101be`

## Notes

- Avoid `-c/--check-links` unless network access is intentionally available.
- The repo convention is to edit the human-authored references and rerun the tool, not to patch the generated block manually.
