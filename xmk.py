import requests
from bs4 import BeautifulSoup
import os

def download_image(url, save_path):
    if not os.path.isfile(save_path):  
        try:
            response = requests.get(url)
            response.raise_for_status()
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {url}: {e}")
    else:
        print(f"Image already exists: {save_path}")

def extract_image_links_from_url(xml_url, tag_names):
    try:
        response = requests.get(xml_url)
        response.raise_for_status()
        content = response.text
        soup = BeautifulSoup(content, 'lxml')
        image_links = []
        for tag_name in tag_names:
            for tag in soup.find_all(tag_name):
                if tag.text not in image_links:  
                    image_links.append(tag.text)
        return image_links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching XML: {e}")
        return []

def download_images_from_url(xml_url, download_folder, tag_names, max_images=3000):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    image_links = extract_image_links_from_url(xml_url, tag_names)
    total_images = min(max_images, len(image_links)) 
    for i in range(total_images):
        url = image_links[i]
        file_extension = url.split('.')[-1]
        save_path = os.path.join(download_folder, f'image_{i + 1}.{file_extension}')
        download_image(url, save_path)


xml_url = 'https://img-champion.mncdn.com/static/base/xmlfeeds/tr-TR/primewidget-240725090024172.xml'
project_folder = 'C:/Users/alisa/Desktop/webscrap'
download_folder = os.path.join(project_folder, 'championss')

tag_names = ['g:image_link1', 'g:image_link2']  


download_images_from_url(xml_url, download_folder, tag_names, max_images=3000)
