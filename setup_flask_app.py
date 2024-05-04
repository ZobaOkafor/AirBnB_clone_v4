#!/usr/bin/python3
"""Script that starts a Flask web application"""

import os
import shutil
import uuid


def start_flask_app():
    # Define source and destination directories
    src_dir = "web_flask"
    dest_dir = "web_dynamic"

    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Copy required files and directories
    shutil.copytree(os.path.join(src_dir, "static"),
                    os.path.join(dest_dir, "static"))

    # Create 'templates' directory in 'web_dynamic' if it doesn't exist
    templates_dir = os.path.join(dest_dir, "templates")
    if not os.path.exists(templates_dir):
        os.makedirs(templates_dir)

    # Copy and rename the HTML file
    shutil.copy(os.path.join(src_dir, "templates", "100-hbnb.html"),
                os.path.join(templates_dir, "0-hbnb.html"))

    # Copy other files
    shutil.copy(os.path.join(src_dir, "__init__.py"), dest_dir)
    shutil.copy(os.path.join(src_dir, "100-hbnb.py"),
                os.path.join(dest_dir, "0-hbnb.py"))

    # Rename files
    os.rename(os.path.join(dest_dir, "100-hbnb.html"),
              os.path.join(dest_dir, "0-hbnb.html"))
    os.rename(os.path.join(dest_dir, "100-hbnb.py"),
              os.path.join(dest_dir, "0-hbnb.py"))

    # Update 0-hbnb.py
    with open(os.path.join(dest_dir, "0-hbnb.py"), "r+") as file:
        content = file.read()
        content = content.replace("/100-hbnb/", "/0-hbnb/")
        file.seek(0)
        file.write(content)
        file.truncate()

    # Add cache_id to render_template in 0-hbnb.py
    cache_id = str(uuid.uuid4())
    with open(os.path.join(dest_dir, "0-hbnb.py"), "r+") as file:
        content = file.read()
        content = content.replace(
                "render_template", f"render_template(cache_id='{cache_id}')")
        file.seek(0)
        file.write(content)
        file.truncate()

    # Add cache_id as query string to <link> tags in 0-hbnb.html
    with open(os.path.join(templates_dir, "0-hbnb.html"), "r+") as file:
        content = file.read()
        content = content.replace(".css\"", f".css?{cache_id}\"")
        file.seek(0)
        file.write(content)
        file.truncate()

    print("Flask web application started successfully.")


if __name__ == "__main__":
    start_flask_app()
