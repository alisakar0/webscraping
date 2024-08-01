#Image Downloader
This project is designed to download images from a specified XML file containing image links. The XML file is parsed to extract image URLs from specific tags, and the images are downloaded to a specified folder.

##Features
1.Extracts image links from an XML file using specified tag names.
2.Downloads images only if they do not already exist in the specified folder.
3.Handles HTTP request errors gracefully.
4.Can limit the number of images downloaded.

##Prerequisites
1.Python 3.x
2.requests library
3.beautifulsoup4 library
4.lxml library

##Installation
1.Clone this repository or download the script files.
2.Install the required libraries using pip:

---pip install requests beautifulsoup4 lxml

##Usage
1.Set the XML URL, project folder, download folder, and tag names in the script.

2.xml_url = 'https://img-champion.mncdn.com/static/base/xmlfeeds/tr-TR/primewidget-240725090024172.xml'
3.project_folder = 'C:/Users/alisa/Desktop/webscrap'
4.download_folder = os.path.join(project_folder, 'championss')
5.tag_names = ['g:image_link1', 'g:image_link2']
-Run the script to start downloading images.

--python download_images.py

##Code Overview
1.download_image(url, save_path): Downloads an image from the given URL and saves it to the specified path if it does not already exist.
2.extract_image_links_from_url(xml_url, tag_names): Extracts image links from the XML file using the specified tag names.
3.download_images_from_url(xml_url, download_folder, tag_names, max_images=3000): Orchestrates the downloading of images, ensuring the maximum number of images does not exceed the specified limit.

##$Example
1.To download images from the specified XML URL and save them to the 'championss' folder within the 'webscrap' project folder, make sure to set the parameters correctly in the script:

-xml_url = 'https://img-champion.mncdn.com/static/base/xmlfeeds/tr-TR/primewidget-240725090024172.xml'
-project_folder = 'C:/Users/alisa/Desktop/webscrap'
-download_folder = os.path.join(project_folder, 'championss')
-tag_names = ['g:image_link1', 'g:image_link2']
-download_images_from_url(xml_url, download_folder, tag_names, max_images=3000)
-Run the script, and the images will be downloaded to the specified folder.
