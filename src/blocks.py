from enum import Enum
from htmlnode import HTMLNode

class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

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