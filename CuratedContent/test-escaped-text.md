# Test of Escaped Text

A test for how to include greater-than and less-than symbols in text.

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
* **BSSw's renderer drops the symbols and contents**

### Case 3

What happens if we put them in `an inline <code block> like this?`

Or an `inline code block \<with escapes\>`?

Results:
* VS Code's renderer displays inline code blocks literally, including the symbols, contents, and escape characters when present.
* Github's renderer displays inline code blocks literally, including the symbols, contents, and escape characters when present.
* **BSSw's renderer drops the symbols and contents in both code blocks.  In the escaped version the first backslash remains, but the second disappears with the rest of the text inside the symbols**

### Case 4

What happens if we put them in a display code block?
```

This is some <code we want> to display;
How about if we \<escape the symbols\>?;

```

Results:
* VS Code's renderer displays inline code blocks literally, including the symbols, contents, and escape characters when present.
* Github's renderer displays inline code blocks literally, including the symbols, contents, and escape characters when present.
* **BSSw's renderer drops the symbols and contents in both code blocks.  In the escaped version the first backslash remains, but the second disappears with the rest of the text inside the symbols**

### Case 5

What about if we use HTML &lt;character entities&gt; like this?

Or in a code block `&lt;like this&gt;` or even

```

In a display block &lt;like this&gt;

```

Results: 
* VS Code's renderer displays the symbols and contents in the regular text.  In code blocks they are displayed literally (i.e., the entity markup codes)
* Github's renderer displays the symbols and contents in the regular text.  In code blocks they are displayed literally (i.e., the entity markup codes)
* **BSSw's renderer drops the symbols and contents in the regular text.  In the code blocks, the entities are rendered into the expected symbols**

<!--
Publish: yes 
-->
 
