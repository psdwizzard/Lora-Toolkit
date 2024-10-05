# Lora-Toolkit
This toolkit will help you clean, organize, and even build a site for your training tags for a Lora.
A Toolkit for Lora Training Data
Overview
This application is a unified suite of tools designed to streamline the management and processing of training data for LORA (Low-Rank Adaptation) models. It combines four essential utilities into a single, user-friendly interface with a dark mode, material design aesthetic.

Features
Site Builder

Create a searchable website to visualize all your training images and associated tags.
Generates an HTML searchable gallery with individual pages for each image. All built automatically from text and image pairs.
Enhances data exploration and presentation.
Prompt Cleaner

Remove specific words or phrases from all your training tags.
Useful for cleaning up unwanted or repetitive text in your dataset.
Add Trigger Word

Prepend any word or phrase to the front of your training tags.
Ideal for adding consistent triggers or identifiers across your dataset.
Prompts to CSV

Compile all your training tags into a single CSV file.
Facilitates data analysis and sharing.
Table of Contents
Installation
Usage
Launching the Application
Site Builder
Prompt Cleaner
Add Trigger Word
Prompts to CSV
Dependencies
Contributing
License
Installation
Follow these steps to set up the application on your local machine.

Prerequisites
Python 3.6 or higher installed on your system.
pip (Python package installer).
Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Install Required Packages
Install the necessary Python libraries using pip:

bash
Copy code
pip install tkinter pillow
tkinter: For the graphical user interface (usually included with Python).
pillow: For image processing in the Site Builder.
Usage
Launching the Application
Run the Python script to start the Lora Toolkit:

bash
Copy code
Lora_toolkit.pyw

Navigating the Interface
Upon launching, you'll see a dropdown menu at the top.
Select the desired tool from the dropdown to switch between applications.
Site Builder
Purpose: Create a searchable website to visualize all your training images and associated tags.

Steps:
Select Image and Text Files Folder:

Click the Browse button to choose the directory containing your images and corresponding .txt files.
Each image should have an accompanying .txt file with the same name (e.g., image1.png and image1.txt).
Enter Project Name:

Provide a name for your project. This will be used as the title of the website and the main HTML file (e.g., MyProject.html).
Select Output Folder:

Choose the directory where the generated website files will be saved.
Generate Website:

Click the Generate Website button.
The application will create an index HTML file with a gallery of images and a search functionality.
Individual HTML pages for each image will also be generated.
Prompt Cleaner
Purpose: Remove specific words or phrases from all your training tags.

Steps:
Select Directory:

Click Browse to choose the folder containing your .txt files (tags).
Enter Text to Remove:

Input the word or phrase you want to remove from all tags.
Execute:

Click Go Burr to start the cleaning process.
The specified text will be removed from all .txt files in the directory.
Add Trigger Word
Purpose: Add specific words or phrases to the beginning of your training tags.

Steps:
Select Directory:

Click Browse to choose the folder containing your .txt files (tags).
Enter Text to Add:

Input the word or phrase you want to prepend to all tags.
Execute:

Click Go Burr to start the process.
The specified text will be added to the front of each .txt file's content.
Prompts to CSV
Purpose: Compile all your training tags into a single CSV file.

Steps:
Select Directory:

Click Browse to choose the folder containing your .txt files (tags).
Enter CSV File Name:

Provide a name for the output CSV file (e.g., training_tags.csv).
Generate CSV:

Click Go Burr to create the CSV file.
The CSV will contain two columns: File Name and Content.
Dependencies
Ensure the following Python packages are installed:

tkinter (usually included with Python)
pillow (for image handling in Site Builder)
os (standard library)
shutil (standard library)
csv (standard library)
Install pillow using:

bash
Copy code
pip install pillow
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes with clear messages.
Push to your branch.
Create a Pull Request explaining your changes.
License
This project is licensed under the MIT License - see the LICENSE file for details.

