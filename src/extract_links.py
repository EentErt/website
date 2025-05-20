import re

def extract_markdown_images(text):
    image_list = []
    image_list = re.findall(r"!\[(.*?)\]\((.*?)\)\s", text+" ")
    #image_list = list(map(lambda x : re.search(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", x).group(1,2), image_list))
    return image_list

def extract_markdown_links(text):
    link_list = []
    link_list = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)\s", text+" ")
    #link_list = list(map(lambda x : re.search(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", x).group(1,2), link_list))
    return link_list

#def split_nodes_image(node):

