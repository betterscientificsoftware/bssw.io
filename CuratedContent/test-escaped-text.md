# Test of Escaped Text

A test for how to include greater-than and less-than symbols in text.

2021-12-28 update: as of <https://github.com/Parallactic/bssw.io/tree/dfc25ab65cef9470f17a0382e0e8295941d00d76> BSSw's rendering is consistent wth GitHub's and VS Code's.

### Case 1

This is a simple test with <bare text enclosed in the symbols>.

Results:
* VS Code's renderer drops the symbols and contents
* Github's renderer drops the symbols and contents
* BSSw's renderer drops the symbols and contents

### Case 2

This is a more complex test case with \<escaped symbols\> at the front and back.

Results:
* VS Code's renderer displays the symbols and contents, as expected
* Github's renderer displays the symbols and contents, as expected
* BSSw's renderer displays the symbols and contents, as expected

### Case 3

What happens if we put them in `an inline <code block> like this?`

Or an `inline code block \<with escapes\>`?

Results:
* VS Code's renderer displays inline code blocks literally, including the symbols, contents, and escape characters when present.
* Github's renderer displays inline code blocks literally, including the symbols, contents, and escape characters when present.
* BSSw's renderer displays inline code blocks literally, including the symbols, contents, and escape characters when present.

### Case 4

What happens if we put them in a display code block?
```

This is some <code we want> to display;
How about if we \<escape the symbols\>?;

```

Results:
* VS Code's renderer displays inline code blocks literally, including the symbols, contents, and escape characters when present.
* Github's renderer displays inline code blocks literally, including the symbols, contents, and escape characters when present.
* BSSw's renderer displays inline code blocks literally, including the symbols, contents, and escape characters when present.
### Case 5

What about if we use HTML &lt;character entities&gt; like this?

Or in a code block `&lt;like this&gt;` or even

```

In a display block &lt;like this&gt;

```

Results: 
* VS Code's renderer displays the symbols and contents in the regular text.  In code blocks they are displayed literally (i.e., the entity markup codes)
* Github's renderer displays the symbols and contents in the regular text.  In code blocks they are displayed literally (i.e., the entity markup codes)
* BSSw's renderer displays the symbols and contents in the regular text.  In code blocks they are displayed literally (i.e., the entity markup codes)

<!--
Publish: yes 
-->
 
