import unittest
from htmlnode import ParentNode, LeafNode

def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )

def test_to_html_with_no_children(self):
    parent_node = ParentNode("div")
    self.assertRaises( ValueError, parent_node.to_html )

def test_to_html_with_no_tag(self):
    parent_node = ParentNode(children=[LeafNode("span", "child")])
    self.assertRaises( ValueError, parent_node.to_html )

def test_to_html_with_props(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node], {"class": "test"})
    self.assertEqual(
        parent_node.to_html(),
        '<div class="test"><span>child</span></div>',
    )

def test_to_html_with_props_and_children_with_props(self):
    child_node = LeafNode("span", "child", {"class": "child"})
    parent_node = ParentNode("div", [child_node], {"class": "test"})
    self.assertEqual(
        parent_node.to_html(),
        '<div class="test"><span class="child">child</span></div>',
    )

if __name__ == "__main__":
    unittest.main()