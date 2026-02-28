import os
from htmlnode import*
from blocks import *


def generate_page(basepath, src, template, dest):

    print(f"Generating page from {src} to {dest} using {template}")
    with  open(src, "r") as source:
        content = source.read()

    with open(template, "r") as tmp:
        template_string = tmp.read()

    html = markdown_to_html_node(content)
    html_string = html.to_html()
    title = extract_title(content)

    final = template_string.replace("{{ Title }}", title)
    final = final.replace("{{ Content }}", html_string)
    final = final.replace('href="/', f"href={basepath}")
    final = final.replace('src=/"', f"src={basepath}" )

    dest_dir = os.path.dirname(dest)
    if dest_dir:  # dest might be just "public/index.html" (has a dir) or "index.html" (no dir)
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest, "w") as f:
        f.write(final)

def generate_pages_recursive(basepath, source_dir, template, dest_dir):

    for entry in os.listdir(source_dir):
        source_path = os.path.join(source_dir, entry)
        dest_path = os.path.join(dest_dir, entry)
    
        if os.path.isfile(source_path):

            dest_path = dest_path.replace(".md", ".html")
            generate_page(basepath, source_path, template, dest_path)

        else:

            generate_pages_recursive(basepath, source_path, template, dest_path)
