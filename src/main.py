from textnode import TextNode
import os
import shutil
import re
from markdown_to_html import markdown_to_html_node

def clean_directory():
    if os.path.exists("public"):
        shutil.rmtree("public")

def copy_files(current_path, public_path):
    if os.path.isfile(current_path):
        shutil.copy(current_path, public_path)
        pass
    if os.path.isdir(current_path):
        os.mkdir(public_path)
        contents = os.listdir(current_path)
        for item in contents:
            new_path = os.path.join(current_path, item)
            new_public_path = os.path.join(public_path, item)
            copy_files(new_path, new_public_path)
    pass

def extract_title(markdown):
    match = re.search(r"(?<!#)#\s(.*?)\n", markdown)
    if match is None:
        raise Exception("No title found")
    title = match.group(1)
    return title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        markdown = file.read()
    title = extract_title(markdown)    
    html = markdown_to_html_node(markdown)
    with open(template_path) as file:
        template = file.read()
        output = template.replace(r"{{ Title }}", title)
        output = output.replace(r"{{ Content }}", html)
        with open(dest_path, "w") as destination:
            destination.write(output)
    pass

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.isfile(dir_path_content):
        with open(dir_path_content) as file:
            markdown = file.read()
        title = extract_title(markdown)
        html = markdown_to_html_node(markdown)
        with open(template_path) as file:
            template = file.read()
            output = template.replace(r"{{ Title }}", title)
            output = output.replace(r"{{ Content }}", html)
            dest_path = re.sub(r".md$", ".html", dest_dir_path)
            with open(dest_path, "w") as destination:
                destination.write(output)
    if os.path.isdir(dir_path_content):
        if os.path.exists(dest_dir_path) != True:
            os.mkdir(dest_dir_path)
        contents = os.listdir(dir_path_content)
        for item in contents:
            new_path = os.path.join(dir_path_content, item)
            new_dest_path = os.path.join(dest_dir_path, item)
            generate_pages_recursive(new_path, template_path, new_dest_path)

    pass



def main():
    clean_directory()
    copy_files("static", "public")
    generate_pages_recursive("content", "template.html", "public")

    

    

main()
