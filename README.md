# Lora Toolkit

## Overview
**Lora Toolkit** is a unified suite of tools designed to streamline the management and processing of training data for LORA (Low-Rank Adaptation) models. It combines four essential utilities into a single, user-friendly interface with a dark mode, material design aesthetic.

## Features

### 1. Site Builder
- Create a searchable website to visualize all your training images and associated tags.
- Generates an HTML gallery with individual pages for each image.
- Enhances data exploration and presentation.

### 2. Prompt Cleaner
- Remove specific words or phrases from all your training tags.
- Useful for cleaning up unwanted or repetitive text in your dataset.

### 3. Add Trigger Word
- Prepend any word or phrase to the front of your training tags.
- Ideal for adding consistent triggers or identifiers across your dataset.

### 4. Prompts to CSV
- Compile all your training tags into a single CSV file.
- Facilitates data analysis and sharing.

### New Feature: Subfolder Support
- All tools now support processing of files in subfolders, allowing for more organized dataset structures.

## Installation

Follow these steps to set up the application on your local machine.

### Prerequisites
- **Python 3.6 or higher** installed on your system.
- **pip** (Python package installer).

### Clone the Repository

```bash
git clone https://github.com/psdwizzard/Lora-Toolkit.git
cd lora-toolkit
```

### Install Required Packages

Install the necessary Python libraries using pip:

```bash
pip install customtkinter pillow
```

- **customtkinter**: For an enhanced, custom-styled graphical user interface.
- **pillow**: For image processing in the Site Builder.

## Usage

### Launching the Application

Run the Python script to start the Lora Toolkit:

```bash
python lora_toolkit.py
```

*Note: Replace `lora_toolkit.py` with the actual filename if it's different.*

### Navigating the Interface

- Upon launching, you'll see a dropdown menu at the top.
- Select the desired tool from the dropdown to switch between applications.
- The interface now uses CustomTkinter for an improved user experience.

### Site Builder

**Purpose**: Create a searchable website to visualize all your training images and associated tags.

Steps:
1. **Select Image and Text Files Folder**:
   - Click the **Browse** button to choose the directory containing your images and corresponding `.txt` files.
   - The tool will now process files in the selected directory and all its subfolders.
   - Each image should have an accompanying `.txt` file with the same name (e.g., `image1.png` and `image1.txt`).
2. **Enter Project Name**:
   - Provide a name for your project. This will be used as the title of the website and the main HTML file (e.g., `MyProject.html`).
3. **Select Output Folder**:
   - Choose the directory where the generated website files will be saved.
4. **Generate Website**:
   - Click the **Generate Website** button.
   - The application will create an index HTML file with a gallery of images and a search functionality.
   - Individual HTML pages for each image will also be generated.

### Prompt Cleaner

**Purpose**: Remove specific words or phrases from all your training tags.

Steps:
1. **Select Directory**:
   - Click **Browse** to choose the folder containing your `.txt` files (tags).
   - The tool will process all `.txt` files in the selected directory and its subfolders.
2. **Enter Text to Remove**:
   - Input the word or phrase you want to remove from all tags.
3. **Execute**:
   - Click **Go Burr** to start the cleaning process.
   - The specified text will be removed from all `.txt` files in the directory and its subfolders.

### Add Trigger Word

**Purpose**: Add specific words or phrases to the beginning of your training tags.

Steps:
1. **Select Directory**:
   - Click **Browse** to choose the folder containing your `.txt` files (tags).
   - The tool will process all `.txt` files in the selected directory and its subfolders.
2. **Enter Text to Add**:
   - Input the word or phrase you want to prepend to all tags.
3. **Execute**:
   - Click **Go Burr** to start the process.
   - The specified text will be added to the front of each `.txt` file's content in the directory and its subfolders.

### Prompts to CSV

**Purpose**: Compile all your training tags into a single CSV file.

Steps:
1. **Select Directory**:
   - Click **Browse** to choose the folder containing your `.txt` files (tags).
   - The tool will process all `.txt` files in the selected directory and its subfolders.
2. **Enter CSV File Name**:
   - Provide a name for the output CSV file (e.g., `training_tags.csv`).
3. **Generate CSV**:
   - Click **Go Burr** to create the CSV file.
   - The CSV will contain two columns: `File Name` and `Content`, including data from all processed subfolders.
