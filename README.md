Image Downloader
This project is designed to download images from a specified XML file containing image links. The XML file is parsed to extract image URLs from specific tags, and the images are downloaded to a specified folder.

Features
Extracts image links from an XML file using specified tag names.
Downloads images only if they do not already exist in the specified folder.
Handles HTTP request errors gracefully.
Can limit the number of images downloaded.

Prerequisites
Python 3.x
requests library
beautifulsoup4 library
lxml library

Installation
Clone this repository or download the script files.
Install the required libraries using pip:

pip install requests beautifulsoup4 lxml

Usage
Set the XML URL, project folder, download folder, and tag names in the script.

xml_url = 'https://img-champion.mncdn.com/static/base/xmlfeeds/tr-TR/primewidget-240725090024172.xml'
project_folder = 'C:/Users/alisa/Desktop/webscrap'
download_folder = os.path.join(project_folder, 'championss')
tag_names = ['g:image_link1', 'g:image_link2']
Run the script to start downloading images.

python download_images.py

Code Overview
download_image(url, save_path): Downloads an image from the given URL and saves it to the specified path if it does not already exist.
extract_image_links_from_url(xml_url, tag_names): Extracts image links from the XML file using the specified tag names.
download_images_from_url(xml_url, download_folder, tag_names, max_images=3000): Orchestrates the downloading of images, ensuring the maximum number of images does not exceed the specified limit.

Example
To download images from the specified XML URL and save them to the 'championss' folder within the 'webscrap' project folder, make sure to set the parameters correctly in the script:

xml_url = 'https://img-champion.mncdn.com/static/base/xmlfeeds/tr-TR/primewidget-240725090024172.xml'
project_folder = 'C:/Users/alisa/Desktop/webscrap'
download_folder = os.path.join(project_folder, 'championss')
tag_names = ['g:image_link1', 'g:image_link2']
download_images_from_url(xml_url, download_folder, tag_names, max_images=3000)
Run the script, and the images will be downloaded to the specified folder.
