# A markdown file to test wikizer
This markdown file simply contains a number of sub-sections with
of lorem ipsum text but with different instances of xml-style
comments, footnotes and reference definitions and combinations
thereof. Each section presents some different aspect of some
markdown text that the wikizer script needs to be able to process
correctly.

Some sections are just headers with no actual text simply to
remind ourselves of the test(s) that still need to be added.

At present, this is just gathering together all the different
cases to test as in TDD. Then, we'll actually develop the CI
test logic.

## Comment line processing

### Ordinary comment processing

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vel velit eget elit tempor tristique nec sed leo. Vivamus commodo nisl tellus, lobortis imperdiet nisl consequat in. Sed tellus ex, laoreet eu dapibus sed, malesuada imperdiet diam. Nunc eu rutrum dui. Nam ut turpis neque. Mauris at nulla faucibus, ullamcorper dolor in, tincidunt ante. Quisque consequat ullamcorper quam, quis ullamcorper sapien sollicitudin eu. Curabitur mattis ipsum et elit semper sollicitudin. Cras ut eros vitae tellus pharetra commodo. Donec blandit sagittis purus ac commodo. Curabitur fermentum suscipit odio, ac pellentesque ipsum auctor eu.

<!---
Ordinary comment not containing a ref or a footnote
--->

Quisque ac augue iaculis, mollis sem vel, vehicula ante. Mauris sollicitudin metus placerat risus sodales cursus. Duis euismod nisi justo, non fermentum est posuere sed. Praesent sagittis eros non aliquet ultricies. Nullam sit amet tincidunt elit. Vivamus scelerisque, enim ut pharetra cursus, odio velit molestie eros, sed ultrices orci urna a nibh. Integer luctus mi metus, id porta neque ornare ac. Curabitur viverra feugiat leo ut convallis. Suspendisse potenti. Proin a libero pharetra, convallis sapien in, facilisis turpis. Integer eget dui turpis.

### Comment containing two ref def lines defining the *same* ref

Fusce sollicitudin feugiat odio, sit amet dictum mi euismod eu. Nam quam orci, elementum sed lacinia in, rutrum volutpat magna. In viverra porta vulputate. Duis interdum, lorem vel cursus accumsan, quam eros eleifend eros, quis posuere augue nisi sed lectus. Phasellus vel pretium enim. Nam ut risus lectus. Vestibulum blandit neque in est pulvinar, non fringilla elit venenatis. Fusce varius metus nec eros eleifend faucibus. Nam tempor commodo ante, non vulputate mauris eleifend at. Donec nisl lorem, lobortis vel dui at, sollicitudin pellentesque ipsum. Maecenas enim nisi, elementum at facilisis vel, lacinia id sapien. Vivamus tristique accumsan nulla a vestibulum. Aliquam porttitor quam mi, ut egestas eros maximus eu. Sed dictum diam ac convallis condimentum. Sed fringilla auctor risus a pretium.

<!---
[45]: https://foo.bar.gorfo.com/index.html
[45]: https://www.ibiblio.org/apollo/Documents/SGA_Memo12_620716.pdf "SGA Memo #12 {}"
--->

### Comment containing text with footnotes to existing refs

Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed scelerisque eros eget risus cursus, sit amet congue elit tincidunt. Quisque porttitor gravida urna imperdiet malesuada. Cras semper arcu velit, quis tincidunt mi commodo at. Duis vitae ornare nisl. Donec accumsan, sapien nec tristique sagittis, augue nibh volutpat tortor, luctus gravida tellus felis vitae neque. Morbi scelerisque risus scelerisque dolor ultrices placerat. Phasellus vulputate, metus a tristique aliquam, enim quam ultricies nunc, in ullamcorper odio sapien ut neque. Phasellus suscipit fringilla risus ut vulputate.

Vestibulum<sup>[25]</sup> eu lacinia risus. Sed id mollis dui, et hendrerit orci. Sed ac tempus purus. Curabitur<sup>[26]</sup> venenatis eget elit eu posuere. Nunc euismod consequat lectus, nec aliquet nisl efficitur eu. Fusce a feugiat felis. Sed maximus metus eget tempus pharetra. Maecenas pharetra fermentum massa id bibendum. Integer ac metus iaculis, euismod purus et, convallis justo.

## Things to test

### Footnote to non-existent ref is fatal error

### Ref not used in any footnote is fatal error or warn

### More than 3 footnotes in same `<sup></sup>` is fatal error or warn

### Ref with no title or bibliographic data

### Ref with title but no bibliographic

### Ref with no title but bibliographic (is this nonsensical)

### Ref with http:// vs https://

### Refs in XML comment block should be ignored (except the one wikize_refs recognizes)

### Can we detect main content *after* link def block and flag it

## Ref link validation

Presently, wikizer script doesn't do any reference link validation. But, it could and maybe it should.
If it does, it should probably only validate links that are in the reference list and actually
referenced.

## Reference sub-part processing

## Real reference list used testing including
   - non-numeric handles
   - non-sorted handles
   - duplicate handles
   - no description string
   - empty description string
   - description string with no biblio data
   - description string with biblio data that duplicates description string

[26]: https://github.com/markcmiller86/SAF/blob/master/src/safapi/docs/miller002.pdf "The SAF Data Model"
[25]: https://en.wikipedia[.org/wiki/Mariner_1 "Info about Mariner 1 {}"

<!---
Publish: No
--->

