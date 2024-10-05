import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import shutil
import csv

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

root = tk.Tk()
root.title("Lora Toolkit")
root.configure(bg='#262626')  # Dark background color

# Configure styles for dark mode and material design
style = ttk.Style()
style.theme_use('clam')

# General Styles
style.configure('TFrame', background='#262626')
style.configure('TLabel', background='#262626', foreground='#cccccc', font=('Segoe UI', 10))
style.configure('TEntry', fieldbackground='#1E1E1E', foreground='#cccccc', background='#1E1E1E', insertcolor='#cccccc')
style.configure('TButton', background='#1f2e40', foreground='#cccccc', borderwidth=0)
style.configure('TCombobox', fieldbackground='#1E1E1E', background='#1E1E1E', foreground='#cccccc', selectbackground='#1E1E1E', selectforeground='#cccccc')

# Button Style
style.map('TButton',
    background=[('active', '#363636'), ('!disabled', '#1f2e40')],
    foreground=[('active', '#cccccc'), ('!disabled', '#cccccc')]
)

# Combobox Style
style.map('TCombobox',
    fieldbackground=[('readonly', '#1E1E1E')],
    background=[('readonly', '#1E1E1E')],
    foreground=[('readonly', '#cccccc')],
    arrowcolor=[('readonly', '#cccccc')]
)

# Define the frames for each app
site_builder_frame = ttk.Frame(root, style='TFrame')
prompt_cleaner_frame = ttk.Frame(root, style='TFrame')
add_trigger_word_frame = ttk.Frame(root, style='TFrame')
prompts_to_csv_frame = ttk.Frame(root, style='TFrame')

for frame in (site_builder_frame, prompt_cleaner_frame, add_trigger_word_frame, prompts_to_csv_frame):
    frame.grid(row=1, column=0, sticky='nsew')

# Create the dropdown menu
app_options = ['Site Builder', 'Prompt Cleaner', 'Add Trigger Word', 'Prompts to CSV']
app_selection_var = tk.StringVar()
app_selection_var.set(app_options[0])  # Default selection

def on_app_select(event=None):
    selection = app_selection_var.get()
    if selection == 'Site Builder':
        show_frame(site_builder_frame)
    elif selection == 'Prompt Cleaner':
        show_frame(prompt_cleaner_frame)
    elif selection == 'Add Trigger Word':
        show_frame(add_trigger_word_frame)
    elif selection == 'Prompts to CSV':
        show_frame(prompts_to_csv_frame)

dropdown = ttk.Combobox(root, textvariable=app_selection_var, values=app_options, state='readonly', style='TCombobox')
dropdown.grid(row=0, column=0, padx=10, pady=10)
dropdown.bind('<<ComboboxSelected>>', on_app_select)

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

    # Collect image and text files
    files = os.listdir(image_text_folder)
    image_extensions = ('.png', '.jpg', '.jpeg')
    image_files = [f for f in files if f.lower().endswith(image_extensions)]
    base_names = [os.path.splitext(f)[0] for f in image_files]

    if not image_files:
        messagebox.showerror("No Images Found", "No PNG or JPG images found in the selected folder.")
        return

    # List to store image data
    images = []

    for image_file in image_files:
        base_name, ext = os.path.splitext(image_file)
        image_path = os.path.join(image_text_folder, image_file)
        text_file = os.path.join(image_text_folder, base_name + '.txt')

        if not os.path.exists(text_file):
            description = ""
        else:
            with open(text_file, 'r', encoding='utf-8') as tf:
                description = tf.read().strip()

        # Copy image to images_folder
        dest_image_path = os.path.join(images_folder, image_file)
        shutil.copy2(image_path, dest_image_path)

        images.append({'name': image_file, 'description': description})

    # Generate index file with search functionality
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
        f.write('            background-color: #262626;\n')
        f.write('            color: #cccccc;\n')
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
        f.write('            color: #cccccc;\n')
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
        f.write('            color: #1f2e40;\n')
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
            # Update paths to include the project subfolder
            image_page = f'HTML/{project_name}/{image_base}.html'
            image_src = f'images/{project_name}/{image_filename}'
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

    # Generate individual HTML pages
    for img in images:
        image_filename = img['name']
        description = img['description']
        image_base = os.path.splitext(image_filename)[0]
        image_page = os.path.join(html_folder, f'{image_base}.html')
        # Calculate relative paths
        relative_image_path = os.path.relpath(os.path.join(images_folder, image_filename), start=os.path.dirname(image_page))
        relative_index_path = os.path.relpath(index_file, start=os.path.dirname(image_page))

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
            f.write('            background-color: #262626;\n')
            f.write('            color: #cccccc;\n')
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
            f.write('            color: #1f2e40;\n')
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
folder_path = tk.StringVar()
index_name = tk.StringVar()
output_path = tk.StringVar()

# Folder selection
ttk.Label(site_builder_frame, text="Select Image and Text Files Folder:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
ttk.Entry(site_builder_frame, textvariable=folder_path, width=50).grid(row=0, column=1, padx=10, pady=5)
ttk.Button(site_builder_frame, text="Browse", command=select_folder).grid(row=0, column=2, padx=10, pady=5)

# Project name
ttk.Label(site_builder_frame, text="Project Name:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
ttk.Entry(site_builder_frame, textvariable=index_name, width=50).grid(row=1, column=1, padx=10, pady=5)
ttk.Label(site_builder_frame, text="(An index file named 'ProjectName.html' will be created)").grid(row=2, column=1, padx=10, pady=0, sticky='w')

# Output folder selection
ttk.Label(site_builder_frame, text="Select Output Folder:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
ttk.Entry(site_builder_frame, textvariable=output_path, width=50).grid(row=3, column=1, padx=10, pady=5)
ttk.Button(site_builder_frame, text="Browse", command=select_output_folder).grid(row=3, column=2, padx=10, pady=5)

# Generate button
ttk.Button(site_builder_frame, text="Generate Website", command=generate_website).grid(row=4, column=1, padx=10, pady=20)

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
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                file_path = os.path.join(directory, filename)
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
    pc_directory_entry.delete(0, tk.END)
    pc_directory_entry.insert(0, directory)

# Create and place widgets for Prompt Cleaner
ttk.Label(prompt_cleaner_frame, text="Directory:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
pc_directory_entry = ttk.Entry(prompt_cleaner_frame, width=40)
pc_directory_entry.grid(row=0, column=1, padx=5, pady=5)
ttk.Button(prompt_cleaner_frame, text="Browse", command=pc_browse_directory).grid(row=0, column=2, padx=5, pady=5)

ttk.Label(prompt_cleaner_frame, text="Text to remove:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
pc_text_entry = ttk.Entry(prompt_cleaner_frame, width=40)
pc_text_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

ttk.Button(prompt_cleaner_frame, text="Go Burr", command=remove_text_from_files).grid(row=2, column=1, pady=20)

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
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                file_path = os.path.join(directory, filename)
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
    atw_directory_entry.delete(0, tk.END)
    atw_directory_entry.insert(0, directory)

# Create and place widgets for Add Trigger Word
ttk.Label(add_trigger_word_frame, text="Directory:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
atw_directory_entry = ttk.Entry(add_trigger_word_frame, width=40)
atw_directory_entry.grid(row=0, column=1, padx=5, pady=5)
ttk.Button(add_trigger_word_frame, text="Browse", command=atw_browse_directory).grid(row=0, column=2, padx=5, pady=5)

ttk.Label(add_trigger_word_frame, text="Text to add:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
atw_text_entry = ttk.Entry(add_trigger_word_frame, width=40)
atw_text_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

ttk.Button(add_trigger_word_frame, text="Go Burr", command=add_text_to_files).grid(row=2, column=1, pady=20)

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

            for filename in os.listdir(directory):
                if filename.endswith(".txt"):
                    file_path = os.path.join(directory, filename)
                    with open(file_path, 'r', encoding='utf-8') as txtfile:
                        content = txtfile.read()
                        csvwriter.writerow([filename, content])

        messagebox.showinfo("Success", f"CSV file '{csv_filename}' created successfully")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def ptc_browse_directory():
    directory = filedialog.askdirectory()
    ptc_directory_entry.delete(0, tk.END)
    ptc_directory_entry.insert(0, directory)

# Create and place widgets for Prompts to CSV
ttk.Label(prompts_to_csv_frame, text="Directory:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
ptc_directory_entry = ttk.Entry(prompts_to_csv_frame, width=40)
ptc_directory_entry.grid(row=0, column=1, padx=5, pady=5)
ttk.Button(prompts_to_csv_frame, text="Browse", command=ptc_browse_directory).grid(row=0, column=2, padx=5, pady=5)

ttk.Label(prompts_to_csv_frame, text="CSV File Name:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
ptc_filename_entry = ttk.Entry(prompts_to_csv_frame, width=40)
ptc_filename_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

ttk.Button(prompts_to_csv_frame, text="Go Burr", command=create_csv).grid(row=2, column=1, pady=20)

# Initialize with the first app
show_frame(site_builder_frame)

root.mainloop()
