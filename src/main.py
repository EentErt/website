from textnode import TextNode
import os
import shutil

def clean_directory():
    if os.path.exists("../public/"):
        shutil.rmtree("../public/")

def get_file_list(current_path):
    if os.path.isfile(current_path):
        pass
    file_list = os.listdir(current_path)
    file_list = list(map(lambda x : get_file_list(x), file_list))
    return file_list

def copy_static_to_public():
    file_list = os.listdir("static")
    print(file_list)
    #file_list = get_file_list(file_list)
    print(file_list)

def main():
    clean_directory()
    copy_static_to_public()
    get_file_list("static")
    

    

main()
