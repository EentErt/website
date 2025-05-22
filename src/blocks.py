from enum import Enum
from htmlnode import HTMLNode, ParentNode, LeafNode
from splitdelimiter import text_to_textnodes
from textnode import text_node_to_html_node
import re

class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

class BlockNode():
    def __init__(self, text, block_type):
        self.text = text
        self.block_type = block_type

    def __eq__(self, other):
        if (
                self.text == other.text and
                self.block_type == other.block_type
            ):
            return True
        return False

    def __repr__(self):
        return f"BlockNode({self.text}, {self.block_type})"

def block_to_block_type(block):
    if block.startswith("#"):
        return BlockType.HEADING
    elif block.startswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith("- "):
        return BlockType.UNORDERED_LIST
    elif block.startswith("1."):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    

def markdown_to_blocks(markdown):
    block_list = markdown.split("\n\n")
    block_list = list(map(lambda x : x.strip(), block_list))
    block_list = [x for x in block_list if x != ""]
    return block_list

# get the number of # in the heading block
def heading_number(text):
    heading_string = re.search(r"(\#)[^#]", text).group()
    return len(heading_string)

def block_to_html_node(block_node):
    match block_node.block_type:
        case BlockType.PARAGRAPH:
            children = text_to_children(block_node.text)
            node = ParentNode("p", children)
            return node
        case BlockType.HEADING:
            text = re.sub(r"(^\#+\s)", "", block_node.text)
            return ParentNode(f"h{heading_number(block_node.text)}", text_to_children(text))
        case BlockType.CODE:
            text = block_node.text.strip("`")
            text = text.lstrip("\n")
            child = [LeafNode("code", text)]
            parent = ParentNode("pre", children = child)
            return parent
        case BlockType.QUOTE:
            text = block_node.text.lstrip(">")
            return ParentNode("blockquote", text_to_children(text))
        case BlockType.UNORDERED_LIST:
            node = ParentNode("ul", text_to_list_items(block_node.text, block_node.block_type))
            return node
        case BlockType.ORDERED_LIST:
            node = ParentNode("ol", text_to_list_items(block_node.text, block_node.block_type))
            return node
        case _:
            raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    leaf_nodes = list(map(lambda x : text_node_to_html_node(x), text_nodes))
    return leaf_nodes

def text_to_list_items(text, block_type):
    list_items = text.split("\n")
    match block_type:
        case BlockType.UNORDERED_LIST:
            list_items = list(map(lambda x : x.lstrip("- "), list_items))
            list_items = list(map(lambda x : make_list_item(x), list_items))
            print(list_items)
            return list_items
        case BlockType.ORDERED_LIST:
            list_items = list(map(lambda x : re.sub(r"(^\d+\.\s)", "", x), list_items))
            list_items = list(map(lambda x : make_list_item(x), list_items))
            print(list_items)
            return list_items
        case _:
            raise ValueError("invalid block type")

def make_list_item(text):
    node = ParentNode("li", children = text_to_children(text))
    return node

            