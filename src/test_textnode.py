import unittest
from textnode import TextNode, TextType, text_node_to_html_node, text_to_textnodes



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://notexample.com")
        self.assertNotEqual(node, node2)

    def test_eq_text_type(self):
        node = TextNode("This is a text node", TextType.ITALIC, "http://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        self.assertNotEqual(node, node2)

    def test_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        node2 = TextNode("This is a different text node", TextType.BOLD, "http://example.com")
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD,)
        node2 = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "http://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "http://example.com"})

    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "http://example.com/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "http://example.com/image.jpg", "alt": "This is an image node"})

    def test_image_no_link(self):
        node = TextNode("This is an image node", TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        self.assertRaises(Exception)

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )

    def test_text_to_textnodes_multiples_of_each_type(self):
        text = "This is **text** with an _italic_ word **and** a `code block` _and_ an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) `and` a [link](https://boot.dev) and another ![fake image](https://i.imgur.com/fakeimage.jpeg) and another [link](https://another.link)"
        new_nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word ", TextType.TEXT),
                TextNode("and", TextType.BOLD),
                TextNode(" a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" ", TextType.TEXT), 
                TextNode("and", TextType.ITALIC),
                TextNode(" an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" ", TextType.TEXT),
                TextNode("and", TextType.CODE),
                TextNode(" a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("fake image", TextType.IMAGE, "https://i.imgur.com/fakeimage.jpeg"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://another.link")
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()