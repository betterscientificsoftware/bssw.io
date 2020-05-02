Table of Contents
=================
[Click to Return to HomePage Table of Contents](../README.md)

# Quirks in BSSw Processing and Styling
## Need to be double checked and moved to style guide. Rinku to take a look.

The working definition of quirks for this document are situations where the results obtained on the BSSw site differ from what a "reasonable person" would expect.  This includes differences between the way content is rendered by the GitHub web editing tools and the BSSw site, and differences from "simple" style defaults that authors may be accustomed to.

The goal of this document is to try to provide some assistance for BSSw authors until we get/develop more thorough documentation of the frontend and style sheets.  Workaround should be included, if known, or suggested alternatives.

## Only two levels of nested lists are supported

Strictly they're supported, but level-3 lists are styled the same as level-2 lists, so you don't get the desired nested list effect.

The suggested workaround from our lead designer is: we want to discourage the use of bullets.  Instead, use structural elements in so far as possible, and try to limit bullets to one level, if necessary.

To that end, it may be useful to note that a level-4 heading (`####`) is styled somewhat like a list item, with a leading dash and the text of the heading in bold.

Also, there is a "link-row" class that is the recommended alternative to a bulleted list containing only links.  The markup is `<a class="link-row" href=<url">text</a>` (yes, Virginia, valid HTML is valid MarkDown).  You can see how it is rendered near the bottom of <https://preview.bssw.io/blog_posts/software-verification>. *Caveat:* this doesn't work well when the row is a mix of linked and non-linked text.

## BSSw is picky about HTML comments in the body of an article

I have encountered a number of situations where attempts to use HTML comments (`<!-- -->`), which should be valid MarkDown too, only to have them appear in the rendered result.

In one case, the issue seemed to be the number of dashes used.  I had used three (`<!--- --->`) and when I changed to using two (`<!-- -->`) it worked properly as a comment.  Even though the original should have been interpreted as the text `- -` within a comment.

But in another case, the two dash version didn't work either.  I never found an explanation for that case.  I just deleted the text in the comment and moved on.

## The HTML comments used to delineate the article's metadata seem to be fine with three dashes

It seems that some example for the metadata that we need in articles used a three-dash-comment, and it has been propagated virtually everywhere on the site.  Fortunately, it seems to work fine for the metadata, even though it is interpreted differently elsehwere.

## There are some issues with images
* Images that go with a particular makdown document are in a separate repo. That means they involve two PRs and keeping paths between them up to date.
* In-line (e.g. not banner) images seem to require specific width or they wind up getting the lightbox treatment
* We don't seem to support images which are themselves links to other things (like maybe the same image at higher res)
* Left, right, center positioning of images is not supported (though non-essential also)

<!---
Publish: No
---!>
