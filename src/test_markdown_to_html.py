import unittest
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html_node(self):
        md = ("This is the markdown")
        node = markdown_to_html_node(md)
        self.assertEqual(node, "<div><p>This is the markdown</p></div>")


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
        self.assertEqual(node, "<div><p>This is the markdown</p><h2>This is a heading</h2><p>This is a paragraph with <b>bold</b>, <i>italic</i> and <code>code</code> text.<pre><code>This is a code block\n</code></pre><blockquote>This is a blockquote</blockquote><ul><li>This is a list</li><li>Item 1.</li><li>Item 2.</li></ul><ol><li>This is an ordered list</li><li>Item 2.</li></ol></div>")

