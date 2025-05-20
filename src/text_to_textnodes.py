from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode
from splitdelimiter import split_nodes_delimiter
from extract_links import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    node_list = []

    bold_nodes = split_nodes_delimiter([node], "**")
    italic_nodes = split_nodes_delimiter(bold_nodes, "_")
    code_nodes = split_nodes_delimiter(italic_nodes, "`")
    link_nodes = split_nodes_link(code_nodes)
    final_nodes = split_nodes_image(link_nodes)


    return final_nodes