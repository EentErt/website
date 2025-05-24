import re
from textnode import TextType, TextNode

def extract_markdown_images(text):
    image_list = []
    image_list = re.findall(r"!\[(.*?)\]\((.*?)\)+", text)
    #image_list = list(map(lambda x : re.search(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", x).group(1,2), image_list))
    return image_list

def extract_markdown_links(text):
    link_list = []
    link_list = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)+", text)
    #link_list = list(map(lambda x : re.search(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", x).group(1,2), link_list))
    return link_list

def split_nodes_image(old_nodes):
    node_list = []

    # skip nodes that are not TextType.TEXT
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue

        image_list = extract_markdown_images(node.text)
        if len(image_list) > 0:
            for image in image_list:
                text_split = node.text.split(f"![{image[0]}]({image[1]})")
                if text_split[0] != "":
                    node_list.append(TextNode(text_split[0], TextType.TEXT))
                node_list.append(TextNode(image[0], TextType.IMAGE, image[1]))
                node.text = text_split[1]
            if text_split[1] != "":
                node_list.append(TextNode(text_split[1], TextType.TEXT))
        else:
            node_list.append(node)
    
    return node_list


def split_nodes_link(old_nodes):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue

        link_list = extract_markdown_links(node.text)
        if len(link_list) > 0:
            
            for link in link_list:
                text_split = node.text.split(f"[{link[0]}]({link[1]})")
                if text_split[0] != "":
                    node_list.append(TextNode(text_split[0], TextType.TEXT))
                node_list.append(TextNode(link[0], TextType.LINK, link[1]))
                node.text = text_split[1]
            if text_split[1] != "":
                node_list.append(TextNode(text_split[1], TextType.TEXT))
        else:
            node_list.append(node)

    return node_list


        

    
            

