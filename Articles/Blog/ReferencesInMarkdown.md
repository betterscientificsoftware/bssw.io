# Wiki-Media Like References In GitHub Markdown

In each major sub-section that follows, we use blocks of Lorem Ipsum text to
demonstrate various ways of attempting using
[GitHub Flavored Markdown](https://github.github.com/gfm/)
to achieve Wiki-Media style footnoting and references. Also, I am using 4
different link examples; one ftp link to a pdf file, one YouTube video link,
one normal wikipedia page link and one link to a specific page of a PDF. I have
noticed GitHub's rendering doesn't support the FTP link but the BSSw site does
I think. Some of our goals include

- Mobile friendly
- Get teaser or summary text about the purpose of a linked reference
  before having to actually follow the link
- Link to reference list then to actual reference
- Separately listed references at the end of the article
- Maximally GitHib Markdown friendly
- Minimal use of in-line HTML
  - `<sup>XX</sup>` for footnote super-scripting
- Minimal requirement on back-end processing
- Avoid duplication of link/reference content
- Ease of use for authors

### Examples

 - [GitHub Reference Style Links w/Duplication](#just-github-reference-style-links)
 - [Using In-Line HTML Anchors](#using-in-line-html-anchors)

---

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vel velit eget elit tempor tristique nec sed leo. Vivamus commodo nisl tellus, lobortis imperdiet nisl consequat in. Sed tellus ex, laoreet eu dapibus sed, malesuada imperdiet diam. Nunc eu rutrum dui. Nam ut turpis neque. Mauris at nulla faucibus, ullamcorper dolor in, tincidunt ante. Quisque consequat ullamcorper quam, quis ullamcorper sapien sollicitudin eu. Curabitur mattis ipsum et elit semper sollicitudin. Cras ut eros vitae tellus pharetra commodo. Donec blandit sagittis purus ac commodo. Curabitur fermentum suscipit odio, ac pellentesque ipsum auctor eu.

Quisque ac augue iaculis, mollis sem vel, vehicula ante. Mauris sollicitudin metus placerat risus sodales cursus. Duis euismod nisi justo, non fermentum est posuere sed. Praesent sagittis eros non aliquet ultricies. Nullam sit amet tincidunt elit. Vivamus scelerisque, enim ut pharetra cursus, odio velit molestie eros, sed ultrices orci urna a nibh. Integer luctus mi metus, id porta neque ornare ac. Curabitur viverra feugiat leo ut convallis. Suspendisse potenti. Proin a libero pharetra, convallis sapien in, facilisis turpis. Integer eget dui turpis.

Fusce sollicitudin feugiat odio, sit amet dictum mi euismod eu. Nam quam orci, elementum sed lacinia in, rutrum volutpat magna. In viverra porta vulputate. Duis interdum, lorem vel cursus accumsan, quam eros eleifend eros, quis posuere augue nisi sed lectus. Phasellus vel pretium enim. Nam ut risus lectus. Vestibulum blandit neque in est pulvinar, non fringilla elit venenatis. Fusce varius metus nec eros eleifend faucibus. Nam tempor commodo ante, non vulputate mauris eleifend at. Donec nisl lorem, lobortis vel dui at, sollicitudin pellentesque ipsum. Maecenas enim nisi, elementum at facilisis vel, lacinia id sapien. Vivamus tristique accumsan nulla a vestibulum. Aliquam porttitor quam mi, ut egestas eros maximus eu. Sed dictum diam ac convallis condimentum. Sed fringilla auctor risus a pretium.

Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed scelerisque eros eget risus cursus, sit amet congue elit tincidunt. Quisque porttitor gravida urna imperdiet malesuada. Cras semper arcu velit, quis tincidunt mi commodo at. Duis vitae ornare nisl. Donec accumsan, sapien nec tristique sagittis, augue nibh volutpat tortor, luctus gravida tellus felis vitae neque. Morbi scelerisque risus scelerisque dolor ultrices placerat. Phasellus vulputate, metus a tristique aliquam, enim quam ultricies nunc, in ullamcorper odio sapien ut neque. Phasellus suscipit fringilla risus ut vulputate.

Vestibulum eu lacinia risus. Sed id mollis dui, et hendrerit orci. Sed ac tempus purus. Curabitur venenatis eget elit eu posuere. Nunc euismod consequat lectus, nec aliquet nisl efficitur eu. Fusce a feugiat felis. Sed maximus metus eget tempus pharetra. Maecenas pharetra fermentum massa id bibendum. Integer ac metus iaculis, euismod purus et, convallis justo.

---

## Just GitHub Reference Style Links

Pros:
 - Simplest
 - Link balloons notes about where links go

Cons:
 - Duplication and re-format of reference content
 - Links direct to ref instead of down to ref list

Lorem ipsum dolor sit amet, consectetur adipiscing elit<sup>[1]</sup>.
Sed quis dui et tortor molestie malesuada. Donec non consectetur arcu,
at semper magna.  Maecenas consectetur porttitor justo ac aliquam.
Curabitur vel faucibus augue<sup>[1],[LCM]</sup>. Maecenas vestibulum
orci vitae libero blandit, sit amet maximus turpis pharetra. Sed ultrices
tellus non pulvinar lacinia. In nec mi lobortis, euismod dui at, dapibus
turpis. Proin et ornare ex<sup>[3]</sup>. Praesent in posuere risus.
Vivamus eleifend nulla eu nisi tincidunt, a mollis mi tincidunt. Nulla
quis velit vel felis mattis tincidunt a ac neque. Aenean viverra leo et
mollis gravida. Integer et fermentum tellus. Phasellus a arcu vitae ipsum
interdum finibus.<sup>[1],[02],[3]</sup>

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vel velit eget elit tempor tristique nec sed leo. Vivamus commodo nisl tellus, lobortis imperdiet nisl consequat in. Sed tellus ex, laoreet eu dapibus sed, malesuada imperdiet diam. Nunc eu rutrum dui. Nam ut turpis neque. Mauris at nulla faucibus, ullamcorper dolor in, tincidunt ante. Quisque consequat ullamcorper quam, quis ullamcorper sapien sollicitudin eu. Curabitur mattis ipsum et elit semper sollicitudin. Cras ut eros vitae tellus pharetra commodo. Donec blandit sagittis purus ac commodo. Curabitur fermentum suscipit odio, ac pellentesque ipsum auctor eu.

Quisque ac augue iaculis, mollis sem vel, vehicula ante. Mauris sollicitudin metus placerat risus sodales cursus. Duis euismod nisi justo, non fermentum est posuere sed. Praesent sagittis eros non aliquet ultricies. Nullam sit amet tincidunt elit. Vivamus scelerisque, enim ut pharetra cursus, odio velit molestie eros, sed ultrices orci urna a nibh. Integer luctus mi metus, id porta neque ornare ac. Curabitur viverra feugiat leo ut convallis. Suspendisse potenti. Proin a libero pharetra, convallis sapien in, facilisis turpis. Integer eget dui turpis.

Fusce sollicitudin feugiat odio, sit amet dictum mi euismod eu. Nam quam orci, elementum sed lacinia in, rutrum volutpat magna. In viverra porta vulputate. Duis interdum, lorem vel cursus accumsan, quam eros eleifend eros, quis posuere augue nisi sed lectus. Phasellus vel pretium enim. Nam ut risus lectus. Vestibulum blandit neque in est pulvinar, non fringilla elit venenatis. Fusce varius metus nec eros eleifend faucibus. Nam tempor commodo ante, non vulputate mauris eleifend at. Donec nisl lorem, lobortis vel dui at, sollicitudin pellentesque ipsum. Maecenas enim nisi, elementum at facilisis vel, lacinia id sapien. Vivamus tristique accumsan nulla a vestibulum. Aliquam porttitor quam mi, ut egestas eros maximus eu. Sed dictum diam ac convallis condimentum. Sed fringilla auctor risus a pretium.

Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed scelerisque eros eget risus cursus, sit amet congue elit tincidunt. Quisque porttitor gravida urna imperdiet malesuada. Cras semper arcu velit, quis tincidunt mi commodo at. Duis vitae ornare nisl. Donec accumsan, sapien nec tristique sagittis, augue nibh volutpat tortor, luctus gravida tellus felis vitae neque. Morbi scelerisque risus scelerisque dolor ultrices placerat. Phasellus vulputate, metus a tristique aliquam, enim quam ultricies nunc, in ullamcorper odio sapien ut neque. Phasellus suscipit fringilla risus ut vulputate.

Vestibulum eu lacinia risus. Sed id mollis dui, et hendrerit orci. Sed ac tempus purus. Curabitur venenatis eget elit eu posuere. Nunc euismod consequat lectus, nec aliquet nisl efficitur eu. Fusce a feugiat felis. Sed maximus metus eget tempus pharetra. Maecenas pharetra fermentum massa id bibendum. Integer ac metus iaculis, euismod purus et, convallis justo.

<!--- FTP link to PDF file, numeric id --->
[1]: ftp://ssh.esac.esa.int/pub/ekuulker/Apollo15/The-Apollo-Guidance-Computer-Architecture-and-Operation.pdf "Whole Book 'Apollo Guidance Computer Architecture and Operation'"

<!--- YouTube link, textual id --->
[LCM]: https://youtu.be/YIBhPsyYCiM "Women Manufacturing AGC Rope Core"

<!--- Wikipedia link --->
[02]: https://en.wikipedia.org/wiki/IBM_System/360_Model_20 "IBM System 360 Model 20 Specs"

<!--- Link to specific page of a pdf --->
[3]: https://www.ibiblio.org/apollo/klabs/history/history_docs/r713.pdf?#page=39 "Random Page of Reliability Report"

|References|
|:---|
|<sup>1</sup>[Whole Book 'Apollo Guidance Computer Architecture and Operation'](ftp://ssh.esac.esa.int/pub/ekuulker/Apollo15/The-Apollo-Guidance-Computer-Architecture-and-Operation.pdf)|
|<sup>LCM</sup>[Women Manufacturing AGC Rope Core](https://youtu.be/YIBhPsyYCiM)|
|<sup>02</sup>[IBM System 360 Model 20 Specs](https://en.wikipedia.org/wiki/IBM_System/360_Model_20)|
|<sup>3</sup>[Random Page of Reliability Report](https://www.ibiblio.org/apollo/klabs/history/history_docs/r713.pdf?#page=39)|

## Using In-Line HTML Anchors

Pros:
- Link to reference list before going to actual reference

Cons:
- Funky syntax where ref handle is duplicated multiple times
- More in-line HTML
- Not sure `a` element `name` or `id` attribute should be used
- No link balloons

Lorem ipsum dolor sit amet, consectetur adipiscing elit<sup>[1](#1)</sup>.
Sed quis dui et tortor molestie malesuada. Donec non consectetur arcu,
at semper magna.  Maecenas consectetur porttitor justo ac aliquam.
Curabitur vel faucibus augue<sup>[1](#1),[LCM](#LCM)</sup>. Maecenas vestibulum
orci vitae libero blandit, sit amet maximus turpis pharetra. Sed ultrices
tellus non pulvinar lacinia. In nec mi lobortis, euismod dui at, dapibus
turpis. Proin et ornare ex<sup>[3](#3)</sup>. Praesent in posuere risus.
Vivamus eleifend nulla eu nisi tincidunt, a mollis mi tincidunt. Nulla
quis velit vel felis mattis tincidunt a ac neque. Aenean viverra leo et
mollis gravida. Integer et fermentum tellus. Phasellus a arcu vitae ipsum
interdum finibus.<sup>[1](#1),[02](#02),[3](#3)</sup>

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vel velit eget elit tempor tristique nec sed leo. Vivamus commodo nisl tellus, lobortis imperdiet nisl consequat in. Sed tellus ex, laoreet eu dapibus sed, malesuada imperdiet diam. Nunc eu rutrum dui. Nam ut turpis neque. Mauris at nulla faucibus, ullamcorper dolor in, tincidunt ante. Quisque consequat ullamcorper quam, quis ullamcorper sapien sollicitudin eu. Curabitur mattis ipsum et elit semper sollicitudin. Cras ut eros vitae tellus pharetra commodo. Donec blandit sagittis purus ac commodo. Curabitur fermentum suscipit odio, ac pellentesque ipsum auctor eu.

Quisque ac augue iaculis, mollis sem vel, vehicula ante. Mauris sollicitudin metus placerat risus sodales cursus. Duis euismod nisi justo, non fermentum est posuere sed. Praesent sagittis eros non aliquet ultricies. Nullam sit amet tincidunt elit. Vivamus scelerisque, enim ut pharetra cursus, odio velit molestie eros, sed ultrices orci urna a nibh. Integer luctus mi metus, id porta neque ornare ac. Curabitur viverra feugiat leo ut convallis. Suspendisse potenti. Proin a libero pharetra, convallis sapien in, facilisis turpis. Integer eget dui turpis.

Fusce sollicitudin feugiat odio, sit amet dictum mi euismod eu. Nam quam orci, elementum sed lacinia in, rutrum volutpat magna. In viverra porta vulputate. Duis interdum, lorem vel cursus accumsan, quam eros eleifend eros, quis posuere augue nisi sed lectus. Phasellus vel pretium enim. Nam ut risus lectus. Vestibulum blandit neque in est pulvinar, non fringilla elit venenatis. Fusce varius metus nec eros eleifend faucibus. Nam tempor commodo ante, non vulputate mauris eleifend at. Donec nisl lorem, lobortis vel dui at, sollicitudin pellentesque ipsum. Maecenas enim nisi, elementum at facilisis vel, lacinia id sapien. Vivamus tristique accumsan nulla a vestibulum. Aliquam porttitor quam mi, ut egestas eros maximus eu. Sed dictum diam ac convallis condimentum. Sed fringilla auctor risus a pretium.

Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed scelerisque eros eget risus cursus, sit amet congue elit tincidunt. Quisque porttitor gravida urna imperdiet malesuada. Cras semper arcu velit, quis tincidunt mi commodo at. Duis vitae ornare nisl. Donec accumsan, sapien nec tristique sagittis, augue nibh volutpat tortor, luctus gravida tellus felis vitae neque. Morbi scelerisque risus scelerisque dolor ultrices placerat. Phasellus vulputate, metus a tristique aliquam, enim quam ultricies nunc, in ullamcorper odio sapien ut neque. Phasellus suscipit fringilla risus ut vulputate.

Vestibulum eu lacinia risus. Sed id mollis dui, et hendrerit orci. Sed ac tempus purus. Curabitur venenatis eget elit eu posuere. Nunc euismod consequat lectus, nec aliquet nisl efficitur eu. Fusce a feugiat felis. Sed maximus metus eget tempus pharetra. Maecenas pharetra fermentum massa id bibendum. Integer ac metus iaculis, euismod purus et, convallis justo.

|References|
|:---|
<a name="1"></a><sup>1</sup>[Whole Book 'Apollo Guidance Computer Architecture and Operation'](ftp://ssh.esac.esa.int/pub/ekuulker/Apollo15/The-Apollo-Guidance-Computer-Architecture-and-Operation.pdf)
|<a name="02"></a><sup>02</sup>[IBM System 360 Model 20 Specs](https://en.wikipedia.org/wiki/IBM_System/360_Model_20)|
|<a name="LCM"></a><sup>LCM</sup>[Women Manufacturing AGC Rope Core](https://youtu.be/YIBhPsyYCiM)
|<a name="3"></a><sup>3</sup>[Random Page of Reliability Report](https://www.ibiblio.org/apollo/klabs/history/history_docs/r713.pdf?#page=39)

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vel velit eget elit tempor tristique nec sed leo. Vivamus commodo nisl tellus, lobortis imperdiet nisl consequat in. Sed tellus ex, laoreet eu dapibus sed, malesuada imperdiet diam. Nunc eu rutrum dui. Nam ut turpis neque. Mauris at nulla faucibus, ullamcorper dolor in, tincidunt ante. Quisque consequat ullamcorper quam, quis ullamcorper sapien sollicitudin eu. Curabitur mattis ipsum et elit semper sollicitudin. Cras ut eros vitae tellus pharetra commodo. Donec blandit sagittis purus ac commodo. Curabitur fermentum suscipit odio, ac pellentesque ipsum auctor eu.

Quisque ac augue iaculis, mollis sem vel, vehicula ante. Mauris sollicitudin metus placerat risus sodales cursus. Duis euismod nisi justo, non fermentum est posuere sed. Praesent sagittis eros non aliquet ultricies. Nullam sit amet tincidunt elit. Vivamus scelerisque, enim ut pharetra cursus, odio velit molestie eros, sed ultrices orci urna a nibh. Integer luctus mi metus, id porta neque ornare ac. Curabitur viverra feugiat leo ut convallis. Suspendisse potenti. Proin a libero pharetra, convallis sapien in, facilisis turpis. Integer eget dui turpis.

Fusce sollicitudin feugiat odio, sit amet dictum mi euismod eu. Nam quam orci, elementum sed lacinia in, rutrum volutpat magna. In viverra porta vulputate. Duis interdum, lorem vel cursus accumsan, quam eros eleifend eros, quis posuere augue nisi sed lectus. Phasellus vel pretium enim. Nam ut risus lectus. Vestibulum blandit neque in est pulvinar, non fringilla elit venenatis. Fusce varius metus nec eros eleifend faucibus. Nam tempor commodo ante, non vulputate mauris eleifend at. Donec nisl lorem, lobortis vel dui at, sollicitudin pellentesque ipsum. Maecenas enim nisi, elementum at facilisis vel, lacinia id sapien. Vivamus tristique accumsan nulla a vestibulum. Aliquam porttitor quam mi, ut egestas eros maximus eu. Sed dictum diam ac convallis condimentum. Sed fringilla auctor risus a pretium.

Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed scelerisque eros eget risus cursus, sit amet congue elit tincidunt. Quisque porttitor gravida urna imperdiet malesuada. Cras semper arcu velit, quis tincidunt mi commodo at. Duis vitae ornare nisl. Donec accumsan, sapien nec tristique sagittis, augue nibh volutpat tortor, luctus gravida tellus felis vitae neque. Morbi scelerisque risus scelerisque dolor ultrices placerat. Phasellus vulputate, metus a tristique aliquam, enim quam ultricies nunc, in ullamcorper odio sapien ut neque. Phasellus suscipit fringilla risus ut vulputate.

Vestibulum eu lacinia risus. Sed id mollis dui, et hendrerit orci. Sed ac tempus purus. Curabitur venenatis eget elit eu posuere. Nunc euismod consequat lectus, nec aliquet nisl efficitur eu. Fusce a feugiat felis. Sed maximus metus eget tempus pharetra. Maecenas pharetra fermentum massa id bibendum. Integer ac metus iaculis, euismod purus et, convallis justo.
