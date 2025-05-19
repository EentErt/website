import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_empty_string(self):
        node = LeafNode("a", "")
        self.assertEqual(node.to_html(), "<a></a>")

    def test_leaf_no_value(self):
        node = LeafNode("a")
        self.assertRaises(ValueError, node.to_html)