import unittest
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html_node(self):
        md = ("""
This is the markdown

# This is a heading

This is a paragraph with **bold**, _italic_ and `code` text.

```
This is a code block
```

>This is a blockquote

- This is a list
- Item 1.
- Item 2.

1. This is an ordered list
2. Item 2.


        """)
        node = markdown_to_html_node(md)
        self.assertEqual(node, "<div><p>This is the markdown</p></div>")