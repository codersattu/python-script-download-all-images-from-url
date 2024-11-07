# Web Image Scraper for Downloading JPEG and PNG Images

## Project Description:

This project is a Python-based web scraping tool designed to download all types of images from a specified web URL. It utilizes popular Python libraries, requests, and BeautifulSoup, to access and parse the content of a webpage, extract image URLs, and download the images to a local directory while ensuring that no file is overwritten.

## Key Features:

Automated Image Extraction: Scrapes the provided webpage for all image tags (<img>), extracting source URLs of images with .jpg, .jpeg, and .png extensions.
URL Handling: Converts relative image paths to absolute URLs to ensure seamless downloading from any valid webpage.
Unique File Naming: Implements a file naming strategy that checks for existing files in the download directory. If a file with the same name already exists, the tool appends a numerical suffix (e.g., image_1.jpg, image_2.png) to maintain unique filenames.
Customizable Storage Location: Saves images in a default folder (downloaded_images) or a user-specified directory.
Error Handling: Handles common request errors gracefully to ensure the script can continue running even if individual images fail to download.
Simple and User-Friendly: Easy-to-use command-line interface where users can input the URL of the desired webpage.

## Prerequisites:

Python 3.x
requests library (pip install requests)
beautifulsoup4 library (pip install beautifulsoup4)

## Usage Instructions:

Run the script in a Python environment.
Enter the target URL when prompted.
The script will create a downloaded_images folder (or use an existing one) and download all valid images from the URL, saving them with unique filenames to prevent overwriting.

## Potential Applications:

Collecting images for data analysis and computer vision projects.
Downloading media for research or personal collections.
Archiving web content for offline access.

This project offers a foundational tool for those interested in web scraping and data collection. It offers opportunities for further customization, such as downloading images in additional formats, adding multi-threading for faster downloads, or integrating a graphical user interface (GUI).
