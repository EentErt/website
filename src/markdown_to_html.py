from blocks import markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode
from textnode import text_to_textnodes

def markdown_to_html_node(markdown):
    block_list = markdown_to_blocks(markdown)
    node_list = list(map(lambda x : HTMLNode(x, block_to_block_type(x)), block_list))

def text_to_children(node_list):
    for node in node_list:
        leaf_list = list(map(lambda x : text_to_textnodes(x), node_list))
        for leaf in leaf_list:
        node.children = leaf_list