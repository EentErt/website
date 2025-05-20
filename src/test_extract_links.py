import unittest
from extract_links import extract_markdown_links, extract_markdown_images, split_nodes_image, split_nodes_link
from textnode import TextType, TextNode

class TestExtractLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_image_no_alt(self):
        matches = extract_markdown_images(
            "This is text with an ![](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_image_no_url(self):
        matches = extract_markdown_images(
            "This is text with an ![image]()"
        )
        self.assertListEqual([("image", "")], matches)

    def test_extract_markdown_link_with_parentheses(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://en.wikipedia.org/wiki/New_York,_New_York_(disambiguation))"
        )
        self.assertListEqual([("link", "https://en.wikipedia.org/wiki/New_York,_New_York_(disambiguation)")], matches)

    def test_extract_markdown_image_with_square_bracket_in_alt(self):
        matches = extract_markdown_images(
            "This is text with an ![image with[square brackets]](https://en.wikipedia.org/wiki/New_York,_New_York_(disambiguation))"
        )
        self.assertListEqual([("image with[square brackets]", "https://en.wikipedia.org/wiki/New_York,_New_York_(disambiguation)")], matches)

#    def test_extract_markdown_image_with_multiple_images_and_link(self):
#        matches = extract_markdown_images(
#            "This is text with an ![image1](https://en.wikipedia.org/wiki/New_York,_New_York_(disambiguation)), ![image2](https://i.imgur.com/zjjcJKZ.png) and a [link](https://fake.link)"
#        )
#        self.assertListEqual([("image1", "https://en.wikipedia.org/wiki/New_York,_New_York_(disambiguation)"), ("image2", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )