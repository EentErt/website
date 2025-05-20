import unittest
from splitdelimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitDelimiter(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is a node with **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**")
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a node with ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT)
            ]
        )
    
    def test_italic(self):
        node = TextNode("This is a node with _italic_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_")
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a node with ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT)
            ]
        )

    def test_code(self):
        node = TextNode("This is a node with `code` text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`")
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a node with ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" text", TextType.TEXT)
            ]
        )

    def test_no_delimiter(self):
        node = TextNode("This is a node with `code` text", TextType.TEXT)
        self.assertRaises(ValueError, split_nodes_delimiter, [node], None)

    def test_empty_delimiter(self):
        node = TextNode("This is a node with `code` text", TextType.TEXT)
        self.assertRaises(ValueError, split_nodes_delimiter, [node], "")

    def test_invalid_delimiter(self):
        node = TextNode("This is a node with `code` text", TextType.TEXT)
        self.assertRaises(ValueError, split_nodes_delimiter, [node], "*")

    def test_multiple_delimiters(self):
        node = TextNode("This is a node with **bold** and _italic_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**")
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a node with ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and _italic_ text", TextType.TEXT)
            ]
        )

    def test_nested_delimiters(self):
        node = TextNode("This is a node with **bold and _italic_** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**")
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a node with ", TextType.TEXT),
                TextNode("bold and _italic_", TextType.BOLD),
                TextNode(" text", TextType.TEXT)
            ]
        )
    
    def test_overlapping_delimiters(self):
        node = TextNode("This is a node _with **bold and italic_** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**")
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a node _with ", TextType.TEXT),
                TextNode("bold and italic_", TextType.BOLD),
                TextNode(" text", TextType.TEXT)
            ]
        )

    def test_multiple_nodes(self):
        node1 = TextNode("This is a node with **bold** text", TextType.TEXT)
        node2 = TextNode("This is another node with _italic_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "**")
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a node with ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
                TextNode("This is another node with _italic_ text", TextType.TEXT)
            ]
        )

    def test_node_list(self):
        node1 = TextNode("This is a node with **bold** text", TextType.TEXT)
        node2 = TextNode("This is another node with _italic_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "_")
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a node with **bold** text", TextType.TEXT),
                TextNode("This is another node with ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT)
            ]
        )



    
