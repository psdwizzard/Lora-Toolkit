import os
import shutil
import csv
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Initialize customtkinter
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = ctk.CTk()
root.title("LORA Toolkit")
root.geometry("715x260")

# Define the frames for each app
site_builder_frame = ctk.CTkFrame(root)
prompt_cleaner_frame = ctk.CTkFrame(root)
add_trigger_word_frame = ctk.CTkFrame(root)
prompts_to_csv_frame = ctk.CTkFrame(root)

for frame in (site_builder_frame, prompt_cleaner_frame, add_trigger_word_frame, prompts_to_csv_frame):
    frame.grid(row=1, column=0, sticky='nsew')

# Create the dropdown menu
app_options = ['Site Builder', 'Prompt Cleaner', 'Add Trigger Word', 'Prompts to CSV']
app_selection_var = ctk.StringVar(value=app_options[0])  # Default selection

def on_app_select(choice):
    selection = app_selection_var.get()
    if selection == 'Site Builder':
        show_frame(site_builder_frame)
    elif selection == 'Prompt Cleaner':
        show_frame(prompt_cleaner_frame)
    elif selection == 'Add Trigger Word':
        show_frame(add_trigger_word_frame)
    elif selection == 'Prompts to CSV':
        show_frame(prompts_to_csv_frame)

dropdown = ctk.CTkOptionMenu(root, values=app_options, command=on_app_select, variable=app_selection_var)
dropdown.grid(row=0, column=0, padx=10, pady=10)

# Now, integrate each app into its frame

######################
# Site Builder Frame #
######################

def generate_website():
    image_text_folder = folder_path.get()
    project_name = index_name.get().strip()
    output_folder = output_path.get()

    if not image_text_folder or not project_name or not output_folder:
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return

    # Append .html to the project name to form the index file name
    index_filename = project_name + '.html'

    images_folder = os.path.join(output_folder, 'images', project_name)
    html_folder = os.path.join(output_folder, 'HTML', project_name)
    index_file = os.path.join(output_folder, index_filename)

    # Create necessary folders
    os.makedirs(images_folder, exist_ok=True)
    os.makedirs(html_folder, exist_ok=True)

    # Collect subfolders
    subfolders = []
    for root_dir, dirs, files in os.walk(image_text_folder):
        # Skip the root folder itself
        if root_dir == image_text_folder:
            subfolders.extend(dirs)
            break  # Only need immediate subdirectories

    # If no subfolders, treat root as a single subfolder
    if not subfolders:
        subfolders = ['']

    # Data structure to hold images per subfolder
    images_per_subfolder = {}
    subfolders_with_pairs = []

    for subfolder in subfolders:
        images = []
        # Build the path to the subfolder
        if subfolder == '':
            current_folder = image_text_folder
        else:
            current_folder = os.path.join(image_text_folder, subfolder)

        # Collect images and descriptions in current subfolder
        has_pairs = False
        for root_dir, _, files in os.walk(current_folder):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    base_name = os.path.splitext(file)[0]
                    image_path = os.path.join(root_dir, file)
                    # Corresponding text file
                    text_file = os.path.join(root_dir, base_name + '.txt')
                    if not os.path.exists(text_file):
                        # Do not include images without corresponding text file
                        continue
                    with open(text_file, 'r', encoding='utf-8') as tf:
                        description = tf.read().strip()
                    # Copy image to images_folder
                    dest_image_subfolder = os.path.join(images_folder, subfolder)
                    os.makedirs(dest_image_subfolder, exist_ok=True)
                    dest_image_path = os.path.join(dest_image_subfolder, file)
                    shutil.copy2(image_path, dest_image_path)
                    images.append({'name': file, 'description': description, 'subfolder': subfolder})
                    has_pairs = True
        if has_pairs:
            images_per_subfolder[subfolder] = images
            subfolders_with_pairs.append(subfolder)

    # Determine if only one subfolder has pairs
    if len(subfolders_with_pairs) == 1:
        # Use that subfolder's images as the main index
        subfolder = subfolders_with_pairs[0]
        images = images_per_subfolder[subfolder]
        # Generate main index page directly with images
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write('<!DOCTYPE html>\n')
            f.write('<html lang="en">\n')
            f.write('<head>\n')
            f.write('    <meta charset="UTF-8">\n')
            f.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
            f.write(f'    <title>{project_name}</title>\n')
            f.write('    <style>\n')
            f.write('        body {\n')
            f.write('            font-family: "Segoe UI", Arial, sans-serif;\n')
            f.write('            background-color: #121212;\n')
            f.write('            color: #ffffff;\n')
            f.write('        }\n')
            f.write('        .search-container {\n')
            f.write('            text-align: center;\n')
            f.write('            margin: 20px;\n')
            f.write('        }\n')
            f.write('        .search-container input {\n')
            f.write('            width: 50%;\n')
            f.write('            padding: 10px;\n')
            f.write('            font-size: 16px;\n')
            f.write('            background-color: #1E1E1E;\n')
            f.write('            color: #ffffff;\n')
            f.write('            border: none;\n')
            f.write('            border-radius: 4px;\n')
            f.write('        }\n')
            f.write('        .gallery {\n')
            f.write('            display: flex;\n')
            f.write('            flex-wrap: wrap;\n')
            f.write('            justify-content: center;\n')
            f.write('        }\n')
            f.write('        .gallery-item {\n')
            f.write('            margin: 10px;\n')
            f.write('            text-align: center;\n')
            f.write('            background-color: #1E1E1E;\n')
            f.write('            padding: 10px;\n')
            f.write('            border-radius: 8px;\n')
            f.write('        }\n')
            f.write('        .gallery-item img {\n')
            f.write('            width: 200px;\n')
            f.write('            height: auto;\n')
            f.write('            border-radius: 4px;\n')
            f.write('        }\n')
            f.write('        .hidden {\n')
            f.write('            display: none;\n')
            f.write('        }\n')
            f.write('        a {\n')
            f.write('            color: #1E88E5;\n')
            f.write('            text-decoration: none;\n')
            f.write('        }\n')
            f.write('        a:hover {\n')
            f.write('            text-decoration: underline;\n')
            f.write('        }\n')
            f.write('    </style>\n')
            f.write('</head>\n')
            f.write('<body>\n')
            f.write(f'    <h1 style="text-align:center;">{project_name}</h1>\n')
            f.write('    <div class="search-container">\n')
            f.write('        <input type="text" id="search-input" placeholder="Search images..." onkeyup="searchImages()">\n')
            f.write('    </div>\n')
            f.write('    <div class="gallery" id="gallery">\n')

            for img in images:
                image_filename = img['name']
                image_base = os.path.splitext(image_filename)[0]
                image_subfolder = img['subfolder']
                # Paths to image and image page
                image_src_full = os.path.join(images_folder, image_subfolder, image_filename)
                image_page_full = os.path.join(html_folder, image_subfolder, f'{image_base}.html')
                # Relative paths from index file
                image_src = os.path.relpath(image_src_full, start=output_folder)
                image_page = os.path.relpath(image_page_full, start=output_folder)
                # Replace backslashes with forward slashes
                image_src = image_src.replace('\\', '/')
                image_page = image_page.replace('\\', '/')
                description = img['description']
                f.write('        <div class="gallery-item">\n')
                f.write(f'            <a href="{image_page}"><img src="{image_src}" alt="{image_base}"></a>\n')
                # Include hidden elements for search
                f.write('            <div class="hidden">\n')
                f.write(f'                <span class="image-name">{image_base}</span>\n')
                f.write(f'                <span class="image-description">{description}</span>\n')
                f.write('            </div>\n')
                f.write('        </div>\n')

            f.write('    </div>\n')

            # Add JavaScript for search functionality
            f.write('    <script>\n')
            f.write('        function searchImages() {\n')
            f.write('            const input = document.getElementById("search-input");\n')
            f.write('            const filter = input.value.toLowerCase();\n')
            f.write('            const gallery = document.getElementById("gallery");\n')
            f.write('            const items = gallery.getElementsByClassName("gallery-item");\n')
            f.write('            for (let i = 0; i < items.length; i++) {\n')
            f.write('                const name = items[i].querySelector(".image-name").textContent.toLowerCase();\n')
            f.write('                const description = items[i].querySelector(".image-description").textContent.toLowerCase();\n')
            f.write('                if (name.includes(filter) || description.includes(filter)) {\n')
            f.write('                    items[i].style.display = "";\n')
            f.write('                } else {\n')
            f.write('                    items[i].style.display = "none";\n')
            f.write('                }\n')
            f.write('            }\n')
            f.write('        }\n')
            f.write('    </script>\n')

            f.write('</body>\n')
            f.write('</html>\n')

        # Generate individual image pages
        subfolder_html_folder = os.path.join(html_folder, subfolder)
        os.makedirs(subfolder_html_folder, exist_ok=True)
        for img in images:
            image_filename = img['name']
            description = img['description']
            image_base = os.path.splitext(image_filename)[0]
            image_page = os.path.join(subfolder_html_folder, f'{image_base}.html')
            # Calculate relative paths from the image page
            relative_image_path = os.path.relpath(os.path.join(images_folder, subfolder, image_filename), start=os.path.dirname(image_page))
            relative_index_path = os.path.relpath(index_file, start=os.path.dirname(image_page))
            # Replace backslashes with forward slashes
            relative_image_path = relative_image_path.replace('\\', '/')
            relative_index_path = relative_index_path.replace('\\', '/')

            with open(image_page, 'w', encoding='utf-8') as f:
                f.write('<!DOCTYPE html>\n')
                f.write('<html lang="en">\n')
                f.write('<head>\n')
                f.write('    <meta charset="UTF-8">\n')
                f.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
                f.write(f'    <title>{image_base}</title>\n')
                f.write('    <style>\n')
                f.write('        body {\n')
                f.write('            font-family: "Segoe UI", Arial, sans-serif;\n')
                f.write('            text-align: center;\n')
                f.write('            margin: 0;\n')
                f.write('            padding: 0;\n')
                f.write('            background-color: #121212;\n')
                f.write('            color: #ffffff;\n')
                f.write('        }\n')
                f.write('        img {\n')
                f.write('            max-width: 80%;\n')
                f.write('            height: auto;\n')
                f.write('            margin-top: 20px;\n')
                f.write('            border-radius: 8px;\n')
                f.write('        }\n')
                f.write('        .description {\n')
                f.write('            margin: 20px;\n')
                f.write('            font-size: 1.2em;\n')
                f.write('        }\n')
                f.write('        a {\n')
                f.write('            display: inline-block;\n')
                f.write('            margin-top: 20px;\n')
                f.write('            text-decoration: none;\n')
                f.write('            color: #1E88E5;\n')
                f.write('            font-size: 1.1em;\n')
                f.write('        }\n')
                f.write('        a:hover {\n')
                f.write('            text-decoration: underline;\n')
                f.write('        }\n')
                f.write('    </style>\n')
                f.write('</head>\n')
                f.write('<body>\n')
                f.write(f'    <h1>{image_base}</h1>\n')
                f.write(f'    <img src="{relative_image_path}" alt="{image_base}">\n')
                f.write(f'    <div class="description">{description}</div>\n')
                f.write(f'    <a href="{relative_index_path}">Back to Gallery</a>\n')
                f.write('</body>\n')
                f.write('</html>\n')

    else:
        # Existing behavior: generate index with subfolders
        # Generate main index file
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write('<!DOCTYPE html>\n')
            f.write('<html lang="en">\n')
            f.write('<head>\n')
            f.write('    <meta charset="UTF-8">\n')
            f.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
            f.write(f'    <title>{project_name}</title>\n')
            f.write('    <style>\n')
            f.write('        body {\n')
            f.write('            font-family: "Segoe UI", Arial, sans-serif;\n')
            f.write('            background-color: #121212;\n')
            f.write('            color: #ffffff;\n')
            f.write('        }\n')
            f.write('        .search-container {\n')
            f.write('            text-align: center;\n')
            f.write('            margin: 20px;\n')
            f.write('        }\n')
            f.write('        .search-container input {\n')
            f.write('            width: 50%;\n')
            f.write('            padding: 10px;\n')
            f.write('            font-size: 16px;\n')
            f.write('            background-color: #1E1E1E;\n')
            f.write('            color: #ffffff;\n')
            f.write('            border: none;\n')
            f.write('            border-radius: 4px;\n')
            f.write('        }\n')
            f.write('        .gallery {\n')
            f.write('            display: flex;\n')
            f.write('            flex-wrap: wrap;\n')
            f.write('            justify-content: center;\n')
            f.write('        }\n')
            f.write('        .gallery-item {\n')
            f.write('            margin: 10px;\n')
            f.write('            text-align: center;\n')
            f.write('            background-color: #1E1E1E;\n')
            f.write('            padding: 20px;\n')
            f.write('            border-radius: 8px;\n')
            f.write('            width: 200px;\n')
            f.write('        }\n')
            f.write('        .gallery-item h2 {\n')
            f.write('            color: #ffffff;\n')
            f.write('            text-decoration: none;\n')
            f.write('        }\n')
            f.write('        .hidden {\n')
            f.write('            display: none;\n')
            f.write('        }\n')
            f.write('        a {\n')
            f.write('            color: #1E88E5;\n')
            f.write('            text-decoration: none;\n')
            f.write('        }\n')
            f.write('        a:hover {\n')
            f.write('            text-decoration: underline;\n')
            f.write('        }\n')
            f.write('        img {\n')
            f.write('            width: 200px;\n')
            f.write('            height: auto;\n')
            f.write('            border-radius: 4px;\n')
            f.write('        }\n')
            f.write('    </style>\n')
            f.write('</head>\n')
            f.write('<body>\n')
            f.write(f'    <h1 style="text-align:center;">{project_name}</h1>\n')
            f.write('    <div class="search-container">\n')
            f.write('        <input type="text" id="search-input" placeholder="Search images..." onkeyup="searchImages()">\n')
            f.write('    </div>\n')
            f.write('    <div class="gallery" id="gallery">\n')

            # List subfolders with pairs
            for subfolder in subfolders_with_pairs:
                if subfolder == '':
                    subfolder_name = 'Main Folder'
                else:
                    subfolder_name = subfolder
                # Link to subfolder index page
                subfolder_index_page = f'{subfolder}.html' if subfolder != '' else 'main_folder.html'
                f.write('        <div class="gallery-item">\n')
                f.write(f'            <a href="{subfolder_index_page}"><h2>{subfolder_name}</h2></a>\n')
                f.write('        </div>\n')

            f.write('    </div>\n')

            # Hidden image data for search
            f.write('    <div id="image-data" class="hidden">\n')
            for subfolder, images in images_per_subfolder.items():
                for img in images:
                    image_filename = img['name']
                    image_base = os.path.splitext(image_filename)[0]
                    image_subfolder = img['subfolder']
                    description = img['description']
                    # Full paths to image and image page
                    image_src_full = os.path.join(images_folder, image_subfolder, image_filename)
                    image_page_full = os.path.join(html_folder, image_subfolder, f'{image_base}.html')
                    # Relative paths from index file
                    image_src = os.path.relpath(image_src_full, start=output_folder)
                    image_page = os.path.relpath(image_page_full, start=output_folder)
                    # Replace backslashes with forward slashes
                    image_src = image_src.replace('\\', '/')
                    image_page = image_page.replace('\\', '/')

                    f.write('        <div class="image-item">\n')
                    f.write(f'            <a href="{image_page}"><img src="{image_src}" alt="{image_base}" width="200"></a>\n')
                    f.write(f'            <span class="image-name">{image_base}</span>\n')
                    f.write(f'            <span class="image-description">{description}</span>\n')
                    f.write('        </div>\n')
            f.write('    </div>\n')

            # JavaScript for search
            f.write('    <script>\n')
            f.write('        function searchImages() {\n')
            f.write('            const input = document.getElementById("search-input");\n')
            f.write('            const filter = input.value.toLowerCase();\n')
            f.write('            const gallery = document.getElementById("gallery");\n')
            f.write('            const imageData = document.getElementById("image-data");\n')
            f.write('            const images = imageData.getElementsByClassName("image-item");\n')
            f.write('            gallery.innerHTML = "";\n')
            f.write('            if (filter === "") {\n')
            # Show subfolders
            for subfolder in subfolders_with_pairs:
                if subfolder == '':
                    subfolder_name = 'Main Folder'
                else:
                    subfolder_name = subfolder
                subfolder_index_page = f'{subfolder}.html' if subfolder != '' else 'main_folder.html'
                f.write('                gallery.innerHTML += \'<div class="gallery-item"><a href="' + subfolder_index_page + '"><h2>' + subfolder_name + '</h2></a></div>\';\n')
            f.write('            } else {\n')
            f.write('                // Show matching images\n')
            f.write('                for (let i = 0; i < images.length; i++) {\n')
            f.write('                    const imgLink = images[i].getElementsByTagName("a")[0];\n')
            f.write('                    const imgName = images[i].getElementsByClassName("image-name")[0].textContent.toLowerCase();\n')
            f.write('                    const imgDescription = images[i].getElementsByClassName("image-description")[0].textContent.toLowerCase();\n')
            f.write('                    const imgHref = imgLink.getAttribute("href");\n')
            f.write('                    const imgSrc = imgLink.getElementsByTagName("img")[0].getAttribute("src");\n')
            f.write('                    if (imgName.includes(filter) || imgDescription.includes(filter)) {\n')
            f.write('                        gallery.innerHTML += \'<div class="gallery-item"><a href="\' + imgHref + \'"><img src="\' + imgSrc + \'" alt="\' + imgName + \'"></a></div>\';\n')
            f.write('                    }\n')
            f.write('                }\n')
            f.write('            }\n')
            f.write('        }\n')
            f.write('    </script>\n')

            f.write('</body>\n')
            f.write('</html>\n')

        # Generate subfolder index pages and individual image pages
        for subfolder in subfolders_with_pairs:
            images = images_per_subfolder[subfolder]
            if subfolder == '':
                subfolder_index_file = os.path.join(output_folder, 'main_folder.html')
            else:
                subfolder_index_file = os.path.join(output_folder, f'{subfolder}.html')

            # Generate subfolder index page
            with open(subfolder_index_file, 'w', encoding='utf-8') as f:
                f.write('<!DOCTYPE html>\n')
                f.write('<html lang="en">\n')
                f.write('<head>\n')
                f.write('    <meta charset="UTF-8">\n')
                f.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
                f.write(f'    <title>{subfolder if subfolder != "" else "Main Folder"}</title>\n')
                f.write('    <style>\n')
                f.write('        body {\n')
                f.write('            font-family: "Segoe UI", Arial, sans-serif;\n')
                f.write('            background-color: #121212;\n')
                f.write('            color: #ffffff;\n')
                f.write('        }\n')
                f.write('        .search-container {\n')
                f.write('            text-align: center;\n')
                f.write('            margin: 20px;\n')
                f.write('        }\n')
                f.write('        .search-container input {\n')
                f.write('            width: 50%;\n')
                f.write('            padding: 10px;\n')
                f.write('            font-size: 16px;\n')
                f.write('            background-color: #1E1E1E;\n')
                f.write('            color: #ffffff;\n')
                f.write('            border: none;\n')
                f.write('            border-radius: 4px;\n')
                f.write('        }\n')
                f.write('        .gallery {\n')
                f.write('            display: flex;\n')
                f.write('            flex-wrap: wrap;\n')
                f.write('            justify-content: center;\n')
                f.write('        }\n')
                f.write('        .gallery-item {\n')
                f.write('            margin: 10px;\n')
                f.write('            text-align: center;\n')
                f.write('            background-color: #1E1E1E;\n')
                f.write('            padding: 10px;\n')
                f.write('            border-radius: 8px;\n')
                f.write('        }\n')
                f.write('        .gallery-item img {\n')
                f.write('            width: 200px;\n')
                f.write('            height: auto;\n')
                f.write('            border-radius: 4px;\n')
                f.write('        }\n')
                f.write('        .hidden {\n')
                f.write('            display: none;\n')
                f.write('        }\n')
                f.write('        a {\n')
                f.write('            color: #1E88E5;\n')
                f.write('            text-decoration: none;\n')
                f.write('        }\n')
                f.write('        a:hover {\n')
                f.write('            text-decoration: underline;\n')
                f.write('        }\n')
                f.write('    </style>\n')
                f.write('</head>\n')
                f.write('<body>\n')
                f.write(f'    <h1 style="text-align:center;">{subfolder if subfolder != "" else "Main Folder"}</h1>\n')
                # Link back to main index
                relative_main_index = os.path.relpath(index_file, start=os.path.dirname(subfolder_index_file))
                relative_main_index = relative_main_index.replace('\\', '/')
                f.write(f'    <a href="{relative_main_index}">Back to Home</a>\n')
                f.write('    <div class="search-container">\n')
                f.write('        <input type="text" id="search-input" placeholder="Search images..." onkeyup="searchImages()">\n')
                f.write('    </div>\n')
                f.write('    <div class="gallery" id="gallery">\n')

                for img in images:
                    image_filename = img['name']
                    image_base = os.path.splitext(image_filename)[0]
                    image_subfolder = img['subfolder']
                    # Paths to image and image page
                    image_src_full = os.path.join(images_folder, image_subfolder, image_filename)
                    image_page_full = os.path.join(html_folder, image_subfolder, f'{image_base}.html')
                    # Relative paths from subfolder index file
                    image_src = os.path.relpath(image_src_full, start=os.path.dirname(subfolder_index_file))
                    image_page = os.path.relpath(image_page_full, start=os.path.dirname(subfolder_index_file))
                    # Replace backslashes with forward slashes
                    image_src = image_src.replace('\\', '/')
                    image_page = image_page.replace('\\', '/')
                    description = img['description']
                    f.write('        <div class="gallery-item">\n')
                    f.write(f'            <a href="{image_page}"><img src="{image_src}" alt="{image_base}"></a>\n')
                    # Include hidden elements for search
                    f.write('            <div class="hidden">\n')
                    f.write(f'                <span class="image-name">{image_base}</span>\n')
                    f.write(f'                <span class="image-description">{description}</span>\n')
                    f.write('            </div>\n')
                    f.write('        </div>\n')

                f.write('    </div>\n')

                # Add JavaScript for search functionality
                f.write('    <script>\n')
                f.write('        function searchImages() {\n')
                f.write('            const input = document.getElementById("search-input");\n')
                f.write('            const filter = input.value.toLowerCase();\n')
                f.write('            const gallery = document.getElementById("gallery");\n')
                f.write('            const items = gallery.getElementsByClassName("gallery-item");\n')
                f.write('            for (let i = 0; i < items.length; i++) {\n')
                f.write('                const name = items[i].querySelector(".image-name").textContent.toLowerCase();\n')
                f.write('                const description = items[i].querySelector(".image-description").textContent.toLowerCase();\n')
                f.write('                if (name.includes(filter) || description.includes(filter)) {\n')
                f.write('                    items[i].style.display = "";\n')
                f.write('                } else {\n')
                f.write('                    items[i].style.display = "none";\n')
                f.write('                }\n')
                f.write('            }\n')
                f.write('        }\n')
                f.write('    </script>\n')

                f.write('</body>\n')
                f.write('</html>\n')

            # Generate individual image pages
            subfolder_html_folder = os.path.join(html_folder, subfolder)
            os.makedirs(subfolder_html_folder, exist_ok=True)
            for img in images:
                image_filename = img['name']
                description = img['description']
                image_base = os.path.splitext(image_filename)[0]
                image_page = os.path.join(subfolder_html_folder, f'{image_base}.html')
                # Calculate relative paths from the image page
                relative_image_path = os.path.relpath(os.path.join(images_folder, subfolder, image_filename), start=os.path.dirname(image_page))
                relative_index_path = os.path.relpath(subfolder_index_file, start=os.path.dirname(image_page))
                # Replace backslashes with forward slashes
                relative_image_path = relative_image_path.replace('\\', '/')
                relative_index_path = relative_index_path.replace('\\', '/')

                with open(image_page, 'w', encoding='utf-8') as f:
                    f.write('<!DOCTYPE html>\n')
                    f.write('<html lang="en">\n')
                    f.write('<head>\n')
                    f.write('    <meta charset="UTF-8">\n')
                    f.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
                    f.write(f'    <title>{image_base}</title>\n')
                    f.write('    <style>\n')
                    f.write('        body {\n')
                    f.write('            font-family: "Segoe UI", Arial, sans-serif;\n')
                    f.write('            text-align: center;\n')
                    f.write('            margin: 0;\n')
                    f.write('            padding: 0;\n')
                    f.write('            background-color: #121212;\n')
                    f.write('            color: #ffffff;\n')
                    f.write('        }\n')
                    f.write('        img {\n')
                    f.write('            max-width: 80%;\n')
                    f.write('            height: auto;\n')
                    f.write('            margin-top: 20px;\n')
                    f.write('            border-radius: 8px;\n')
                    f.write('        }\n')
                    f.write('        .description {\n')
                    f.write('            margin: 20px;\n')
                    f.write('            font-size: 1.2em;\n')
                    f.write('        }\n')
                    f.write('        a {\n')
                    f.write('            display: inline-block;\n')
                    f.write('            margin-top: 20px;\n')
                    f.write('            text-decoration: none;\n')
                    f.write('            color: #1E88E5;\n')
                    f.write('            font-size: 1.1em;\n')
                    f.write('        }\n')
                    f.write('        a:hover {\n')
                    f.write('            text-decoration: underline;\n')
                    f.write('        }\n')
                    f.write('    </style>\n')
                    f.write('</head>\n')
                    f.write('<body>\n')
                    f.write(f'    <h1>{image_base}</h1>\n')
                    f.write(f'    <img src="{relative_image_path}" alt="{image_base}">\n')
                    f.write(f'    <div class="description">{description}</div>\n')
                    f.write(f'    <a href="{relative_index_path}">Back to Gallery</a>\n')
                    f.write('</body>\n')
                    f.write('</html>\n')

    messagebox.showinfo("Success", f"Website '{project_name}' generated successfully!")

def select_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)

def select_output_folder():
    folder_selected = filedialog.askdirectory()
    output_path.set(folder_selected)

# Variables to store user input
folder_path = ctk.StringVar()
index_name = ctk.StringVar()
output_path = ctk.StringVar()

# Folder selection
ctk.CTkLabel(site_builder_frame, text="Select Image and Text Files Folder:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
ctk.CTkEntry(site_builder_frame, textvariable=folder_path, width=300).grid(row=0, column=1, padx=10, pady=5)
ctk.CTkButton(site_builder_frame, text="Browse", command=select_folder).grid(row=0, column=2, padx=10, pady=5)

# Project name
ctk.CTkLabel(site_builder_frame, text="Project Name:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
ctk.CTkEntry(site_builder_frame, textvariable=index_name, width=300).grid(row=1, column=1, padx=10, pady=5)
ctk.CTkLabel(site_builder_frame, text="(An index file named 'ProjectName.html' will be created)").grid(row=2, column=1, padx=10, pady=0, sticky='w')

# Output folder selection
ctk.CTkLabel(site_builder_frame, text="Select Output Folder:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
ctk.CTkEntry(site_builder_frame, textvariable=output_path, width=300).grid(row=3, column=1, padx=10, pady=5)
ctk.CTkButton(site_builder_frame, text="Browse", command=select_output_folder).grid(row=3, column=2, padx=10, pady=5)

# Generate button
ctk.CTkButton(site_builder_frame, text="Generate Website", command=generate_website).grid(row=4, column=1, padx=10, pady=20)

#########################
# Prompt Cleaner Frame  #
#########################

def remove_text_from_files():
    directory = pc_directory_entry.get()
    text_to_remove = pc_text_entry.get()

    if not directory or not text_to_remove:
        messagebox.showerror("Error", "Please fill in both fields")
        return

    try:
        files_modified = 0
        for root_dir, _, files in os.walk(directory):
            for filename in files:
                if filename.endswith(".txt"):
                    file_path = os.path.join(root_dir, filename)
                    with open(file_path, 'r+', encoding='utf-8') as file:
                        content = file.read()
                        if text_to_remove in content:
                            new_content = content.replace(text_to_remove, '')
                            file.seek(0)
                            file.write(new_content)
                            file.truncate()
                            files_modified += 1

        messagebox.showinfo("Success", f"Removed text from {files_modified} files")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def pc_browse_directory():
    directory = filedialog.askdirectory()
    pc_directory_entry.delete(0, ctk.END)
    pc_directory_entry.insert(0, directory)

# Create and place widgets for Prompt Cleaner
ctk.CTkLabel(prompt_cleaner_frame, text="Directory:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
pc_directory_entry = ctk.CTkEntry(prompt_cleaner_frame, width=300)
pc_directory_entry.grid(row=0, column=1, padx=5, pady=5)
ctk.CTkButton(prompt_cleaner_frame, text="Browse", command=pc_browse_directory).grid(row=0, column=2, padx=5, pady=5)

ctk.CTkLabel(prompt_cleaner_frame, text="Text to remove:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
pc_text_entry = ctk.CTkEntry(prompt_cleaner_frame, width=300)
pc_text_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

ctk.CTkButton(prompt_cleaner_frame, text="Go Burr", command=remove_text_from_files).grid(row=2, column=1, pady=20)

#############################
# Add Trigger Word Frame    #
#############################

def add_text_to_files():
    directory = atw_directory_entry.get()
    text_to_add = atw_text_entry.get()

    if not directory or not text_to_add:
        messagebox.showerror("Error", "Please fill in both fields")
        return

    try:
        files_modified = 0
        for root_dir, _, files in os.walk(directory):
            for filename in files:
                if filename.endswith(".txt"):
                    file_path = os.path.join(root_dir, filename)
                    with open(file_path, 'r+', encoding='utf-8') as file:
                        content = file.read()
                        file.seek(0, 0)
                        file.write(text_to_add + content)
                        file.truncate()
                    files_modified += 1

        messagebox.showinfo("Success", f"Added text to {files_modified} files")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def atw_browse_directory():
    directory = filedialog.askdirectory()
    atw_directory_entry.delete(0, ctk.END)
    atw_directory_entry.insert(0, directory)

# Create and place widgets for Add Trigger Word
ctk.CTkLabel(add_trigger_word_frame, text="Directory:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
atw_directory_entry = ctk.CTkEntry(add_trigger_word_frame, width=300)
atw_directory_entry.grid(row=0, column=1, padx=5, pady=5)
ctk.CTkButton(add_trigger_word_frame, text="Browse", command=atw_browse_directory).grid(row=0, column=2, padx=5, pady=5)

ctk.CTkLabel(add_trigger_word_frame, text="Text to add:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
atw_text_entry = ctk.CTkEntry(add_trigger_word_frame, width=300)
atw_text_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

ctk.CTkButton(add_trigger_word_frame, text="Go Burr", command=add_text_to_files).grid(row=2, column=1, pady=20)

#########################
# Prompts to CSV Frame  #
#########################

def create_csv():
    directory = ptc_directory_entry.get()
    csv_filename = ptc_filename_entry.get()

    if not directory or not csv_filename:
        messagebox.showerror("Error", "Please fill in both fields")
        return

    if not csv_filename.endswith('.csv'):
        csv_filename += '.csv'

    try:
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['File Name', 'Content'])

            for root_dir, _, files in os.walk(directory):
                for filename in files:
                    if filename.endswith(".txt"):
                        file_path = os.path.join(root_dir, filename)
                        with open(file_path, 'r', encoding='utf-8') as txtfile:
                            content = txtfile.read()
                            csvwriter.writerow([filename, content])

        messagebox.showinfo("Success", f"CSV file '{csv_filename}' created successfully")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def ptc_browse_directory():
    directory = filedialog.askdirectory()
    ptc_directory_entry.delete(0, ctk.END)
    ptc_directory_entry.insert(0, directory)

# Create and place widgets for Prompts to CSV
ctk.CTkLabel(prompts_to_csv_frame, text="Directory:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
ptc_directory_entry = ctk.CTkEntry(prompts_to_csv_frame, width=300)
ptc_directory_entry.grid(row=0, column=1, padx=5, pady=5)
ctk.CTkButton(prompts_to_csv_frame, text="Browse", command=ptc_browse_directory).grid(row=0, column=2, padx=5, pady=5)

ctk.CTkLabel(prompts_to_csv_frame, text="CSV File Name:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
ptc_filename_entry = ctk.CTkEntry(prompts_to_csv_frame, width=300)
ptc_filename_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

ctk.CTkButton(prompts_to_csv_frame, text="Go Burr", command=create_csv).grid(row=2, column=1, pady=20)

# Initialize with the first app
show_frame(site_builder_frame)

root.mainloop()
