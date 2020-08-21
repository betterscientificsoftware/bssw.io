## About this site

This is the GitHub pages site that hosts the Better Scientific Software
Editorial Board process documents. It is being served out of the `docs`
folder of the of the [`bssw.io`](https://github.com/betterscientificsoftware/bssw.io) repository.
We considered
[various options](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/issues/530#issuecomment-639034431)
for managing this content.

This site is a [GitHub Pages](https://pages.github.com) site using the 
[*built-in*](https://pages.github.com/themes/), [Jekyll](https://jekyllrb.com/)
[Leap-day](https://github.com/pages-themes/leap-day) theme with a few
modifications. Ordinarily, using a *built-in* theme means that we wouldn't need
to maintain many of the extra directories typical of a full-fledged
Jekyll site. However, because we've costomized to be different than the *default*
*built-in* theme, we have some of those additional directories.

* Changed the color theme.
  * The *default* colors for the leap-day theme are blue and yellow. As an aside,
    that color scheme appears to have come from an episode of the TV comedy show
    [30 Rock](https://www.vulture.com/2020/02/30-rock-leap-day-william-episode.html)
  * To change it, I added `assets/css/styles.css` to override various of the colors
    used in various css settings.
* The default layout, `_layouts/default.html` was instantiated here and modified
  to customize for
  * Breadcrumbs (more about those below)
  * The logo image (which still is not quite right)
  * Edit this page button
  * Removal of download buttons
* Some docs from `bssw.io` repo were copied here and modified slightly...
  * Removed all manual table of contents stuff
  * Removed all xml-style comments bracketed with `<!--` and `-->`
  * Created `index.md` files in each level directory as a sort of landing page
    and table of contents for the sub-docs in that level of content.
* The [Leap-day](https://github.com/pages-themes/leap-day) automatically creates a
  left-side-bar table of contents based on all level 1 (`#`) and level 2 (`##`)
  headings in a page. We can adjust this for greater depth if necessary.
* The breadcrumb path strings seem to take their values frome the top-level
  heading in each page.
* Added some very initial CI checks. Be aware of the following...
  * **Using NodeJs implementation of `markdownlint`**
    * You can find it documentation about it [here](https://github.com/DavidAnson/markdownlint)
    * For command line options [see here](https://github.com/igorshubovych/markdownlint-cli)
    * For rules [see here](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md001)
    * For configuration file format, etc. [see here](https://github.com/igorshubovych/markdownlint-cli#configuration)
  * **CI build output shows errors:**
    * If you have a failing CI check, [like this one](https://travis-ci.com/github/betterscientificsoftware/bssw-eb-docs2/builds/173330547) follow the links to the failed build to see what markdown compliance issues it encountered.
  * **Using YML folded scalars for scripting in .travis.yml**
    * See [these docs](https://yaml.org/spec/1.2/spec.html#id2760844) on YML folded scalars
    * This essentially allows me to [maintain shell scripting code](https://github.com/betterscientificsoftware/bssw-eb-docs2/blob/f6c8f3578d0cc2b46133851b81dae369ececccb4/.travis.yml#L9) *in* the `.travis.yml` file instead of putting in a subfile
  * **Added spell checking:**
    * Uses [markdown-spellcheck](https://www.npmjs.com/package/markdown-spellcheck)
    * A separate `.spelling` file holds supported spellings
  * **First editors fix all CI compliance issues:**
    * CI checks were instantiated without ensuring *all existing* `*.md` files are compliant. If someone edits a `.md` file here and tries to merge it from a PR, its possible the CI check will say it failed for lines you never edited. When this happens, I am asking that *first* editors to encounter such issues then please fix them.

