from textnode import TextNode
import os
import shutil
import re

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

def main():
    clean_directory()
    copy_files("static", "public")
    title = extract_title("# Title\n## Not Title")
    print(title)

    

    

main()
