from textnode import TextType, TextNode
from extract_links import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)

    bold_nodes = split_nodes_delimiter([node], "**")
    italic_nodes = split_nodes_delimiter(bold_nodes, "_")
    code_nodes = split_nodes_delimiter(italic_nodes, "`")
    link_nodes = split_nodes_link(code_nodes)
    final_nodes = split_nodes_image(link_nodes)
    return final_nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type = TextType.TEXT):
    node_list = []
    if delimiter is None:
        raise ValueError("function requires a delimiter")

    # If node is not a text node, add it to the list as is
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node = TextNode(node.text, node.text_type)
            node_list.append(new_node)
            continue

        # if the delimiter appears an odd number of times, it is unclosed, and invalid
        # if the delimiter appears an even number of times, it is closed, and valid
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("invalid markdown syntax")
        
        # odd indexed elements are text nodes with the delimiter type
        # map new text nodes to the odd indexed elements of node_list
        match delimiter:
            case "**":
                node_split = node.text.split(delimiter)
                node_split[0::2] = list(map(lambda x: TextNode(x, TextType.TEXT), node_split[0::2]))
                node_split[1::2] = list(map(lambda x: TextNode(x, TextType.BOLD), node_split[1::2]))
                node_list.extend(node_split)
            
            case "_":
                node_split = node.text.split(delimiter)
                node_split[0::2] = list(map(lambda x: TextNode(x, TextType.TEXT), node_split[0::2]))
                node_split[1::2] = list(map(lambda x: TextNode(x, TextType.ITALIC), node_split[1::2]))
                node_list.extend(node_split)

            case "`":
                node_split = node.text.split(delimiter)
                node_split[0::2] = list(map(lambda x: TextNode(x, TextType.TEXT), node_split[0::2]))
                node_split[1::2] = list(map(lambda x: TextNode(x, TextType.CODE), node_split[1::2]))
                node_list.extend(node_split)

            case _:
                raise ValueError("invalid delimiter")

    return node_list


    