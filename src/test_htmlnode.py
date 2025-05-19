import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("tag", "value", "children", {"prop": "value"})
        node2 = HTMLNode("tag", "value", "children", {"prop": "value"})
        self.assertEqual(node, node2)

    def test_eq_tag(self):
        node = HTMLNode("tag", "value", "children", {"prop": "value"})
        node2 = HTMLNode("different_tag", "value", "children", {"prop": "value"})
        self.assertNotEqual(node, node2)

    def test_eq_value(self):
        node = HTMLNode("tag", "value", "children", {"prop": "value"})
        node2 = HTMLNode("tag", "different_value", "children", {"prop": "value"})
        self.assertNotEqual(node, node2)

    def test_eq_children(self):
        node = HTMLNode("tag", "value", "children", {"prop": "value"})
        node2 = HTMLNode("tag", "value", "different_children", {"prop": "value"})
        self.assertNotEqual(node, node2)

    def test_eq_props(self):
        node = HTMLNode("tag", "value", "children", {"prop": "value"})
        node2 = HTMLNode("tag", "value", "children", {"different_prop": "value"})
        self.assertNotEqual(node, node2)

    def test_eq_no_props(self): 
        node = HTMLNode("tag", "value", "children")
        node2 = HTMLNode("tag", "value", "children", {"prop": "value"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode(props={"prop": "value"})
        output = node.props_to_html()
        expected = ' prop="value"'
        self.assertEqual(output, expected)

if __name__ == "__main__":
    unittest.main()