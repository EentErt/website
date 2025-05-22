from textnode import TextNode
import os
import shutil

def clean_directory():
    if os.path.exists("../public/"):
        shutil.rmtree("../public/")

def get_static_file_list():
    file_list = os.listdir("../static/")

def copy_static_to_public(directory):
    file_list = os.listdir("../static/")
    print(files)

def main():
    clean_directory()
    copy_static_to_public()
    

    

main()
