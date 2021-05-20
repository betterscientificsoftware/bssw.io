# images

**NOTE: PLEASE FOLLOW THE INSTRUCTIONS GIVEN BELOW. All new images should be uploaded to the  `bssw.io/images` directory!**

This directory is for image files that will be displayed on the bssw.io site.

Note that you can place an image from any location on the web, but drawing images from this images directory and assigning the proper class for an image ensures it will display consistently with other images in the site.

### File format, file size, and resolution

Upload only `*.jpgs`, `*.pngs`, `*.gifs`, or `*.pdfs` files. If you are working with another file format, be sure to convert to one of these. Image resizing tools can be used, such as Photoshop, Apple Preview, [Gimp](https://www.gimp.org/downloads/), [Darktable](http://www.darktable.org), etc.

Before adding an image, please pay careful attention to the file size and the pixel size.

A file size above 10MB should be considered too large to commit to the `images/` directory. If you have an image this large to upload, please resize to a size below 5MB. Problems may be introduced with such large images in the repository.

Pixel size is different than the file size and is indicated by pixel width x pixel height. To determine the pixel size of your image:

* Find the location where the image is saved
* Place your cursor over the image icon, and right-click if you are using a PC or Ctrl-click if you are using a Mac.
* Choose Properties (or Get Info on Mac).
* On PC click the Details tab

An image with a pixel size less than 1000 px on its largest dimension is considered resolution deficient; please attempt to find a higher resolution (excludes logos).

### Image Class Options

Classes control how your image will appear on a page. The following classes should address each need. To see how they are placed into code, see "How to place an image on the page" below. Special cases for Blog post images and PDFs are included at the bottom of this document.

```
class='page'
```

(example to come)

```
class='logo'
```

(example to come)

```
class='page lightbox'
```

(example to come)

### Adding an image file

An image file should be added to the `images/` directory on a branch just like any other file when adding new content in an `*.md` file.

### Where/when to place an image on a page

#### Resources

The inclusion of images in the text area is intended to better explain the concept expressed in the resource -- diagrams, data viz --  nothing frivolous.

#### Blog posts

A hero image is allowed but not required for blog posts. The hero of the top blog item will be displayed on blog landing page. Hero images should contain no bold text; incidental text (in diagrams, for instance) is OK.

#### Events

Inclusion of logos and speaker images in the text area is OK, but the point of these pages is to give some detail and then pass users on to the official event page.

#### Articles

Articles are presented as resources, so resource rules apply.

### How to place an image on a page

At any point you can enter the following tag to call up an image (for example, for and `*.md` file under the `Articles/Blogs/` directory)

```
<img src='../../images/filename.jpg' class='page lightbox' />
```

To add caption text, place the image text in front of the image tag.

```
[Image text]<img src='../../images/filename.jpg' class='page lightbox' />
```

#### Notes

* You need to replace `filename.jpg` with the appropriate file that's been uploaded to the repository (name.format).
* The relative path `../../images/` directory used depends on where the `*.md` file is in the directory tree in relation to the base `images/` directory.
* The `class='page lightbox'` attribute accommodates a wide set of image shapes and allows user to enlarge the image to full screen. Always use `'page lightbox'` for vertical images.
* If your horizontal image is under 1000 px wide, you can substitute `class='page'` to prevent enlargement.
* If you are entering a logo or head-shot, you can substitute `class='logo'` to scale appropriately.
* If you are using either `class='page'` or `class='logo'` be sure to add a:

  ```
  <br> 
  ```

  tag after the preceding text and before the image to ensure adequate separation between the two.

#### Presence of a introductory text (a.k.a. a deck)

This is the introductory sentence or paragraph that appears in the gray hero area below the page title. The system uses the first paragraph of your body copy to populate this deck. Unless you are assigning a hero image specifically to a blog post or an article, you will want to be sure to enter a deck. This brings consistency to pages, provides readers with a brief overview of what's to come, and importantly, including a deck ensures that page images are placed below the prerequisites. Not doing so "breaks" the page.

### Images: Special cases

#### Blog hero images

These are a special case. Enter the code below substituting your filename at the end of the tag.

```
**Hero Image:**
 
- <img src='../../images/filename.png' />[The debut of Better Scientific Software.]
```

#### PDF Files

These are addressed as a text link and follow the formatting below.

```
[WhatIs doc](../../images//filename.pdf "What is Good Documentation?")
```
