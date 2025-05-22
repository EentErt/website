from blocks import markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode, ParentNode, LeafNode
from splitdelimiter import text_to_textnodes
from blocks import BlockNode, block_to_html_node

def markdown_to_html_node(markdown):
    block_list = markdown_to_blocks(markdown)
    block_list = list(map(lambda x : BlockNode(x, block_to_block_type(x)), block_list))
    node_list = list(map(lambda x : block_to_html_node(x), block_list))
    div_node = ParentNode("div", node_list)

    return div_node.to_html()




        