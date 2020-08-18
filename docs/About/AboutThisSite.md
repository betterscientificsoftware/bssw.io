## About this site

This is a throw-away site created to demonstrate option 4 of 
[various options](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/issues/530#issuecomment-639034431)
for managing BSSw.io content development process documentation.

This site is a [GitHub Pages](https://pages.github.com) site using the 
[*built-in*](https://pages.github.com/themes/), [Jekyll](https://jekyllrb.com/)
[Leap-day](https://github.com/pages-themes/leap-day) theme with a few
modifications...

* The default layout, `_layouts/default.html` was instantiated here and modified
  to customize for
  * Breadcrumbs
  * The logo image (which still is not quite right)
  * Edit this page button
  * Removal of download buttons
* Some docs (not all those that would be necessary if we decided to really take
  this appraoch) from `bssw.io` repo were copied here and modified slightly...
  * Removed all manual table of contents stuff
  * Removed all xml-style comments bracketed with `<!--` and `-->`
  * Created `index.md` files in each top-level directory
* A simple [password-protected subtree](../Protected/index.html) was added using
  [static hashing from this project](https://github.com/pages-themes/leap-day). The
  demo password is `BsswIsGreat`.
* The [Leap-day](https://github.com/pages-themes/leap-day) supports table of contents
  for level 1 (`#`) and level 2 (`##`) headings automatically. We can adjust this too
  for greater depth if necessary.
