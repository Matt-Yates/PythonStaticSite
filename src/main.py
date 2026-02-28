from textnode import TextNode, TextType
import os
import shutil
from generate import *
import sys

def copy_directory(src, dst):
    # Clean destination directory if it exists, then recreate it
    if os.path.exists(dst):
        print(f"Deleting destination directory: {dst}")
        shutil.rmtree(dst)
    
    print(f"Creating directory: {dst}")
    os.mkdir(dst)

    # Iterate over all items in the source directory
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)
        else:
            print(f"Entering subdirectory: {src_path}")
            copy_directory(src_path, dst_path)



def main():

    basepath = sys.argv[0]
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    copy_directory("static", "docs")
    generate_pages_recursive(basepath, "content", "template.html", "docs")

main()
