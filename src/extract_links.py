import re
from textnode import TextType, TextNode

def extract_markdown_images(text):
    image_list = []
    image_list = re.findall(r"!\[(.*?)\]\((.*?)\)\s", text+" ")
    print(image_list)
    #image_list = list(map(lambda x : re.search(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", x).group(1,2), image_list))
    return image_list

def extract_markdown_links(text):
    link_list = []
    link_list = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)\s", text+" ")
    #link_list = list(map(lambda x : re.search(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", x).group(1,2), link_list))
    return link_list

def split_nodes_image(old_nodes):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node = TextNode(node.text, node.text_type)
            node_list.extend(new_node)

        new_node = TextNode(node.text.split("![", 1)"))
    node_list.extend(extract_markdown_images(node.text))
    print(node_list)
    return node_list

def split_nodes_link(old_nodes):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node = TextNode(node.text, node.text_type)
            node_list.extend(new_node)

        

    
            

