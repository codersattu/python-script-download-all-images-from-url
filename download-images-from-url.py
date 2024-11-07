#!/usr/bin/env python
# coding: utf-8

# ## Python Script to download all images from a given url

# ### Author: Abhishek Satpathy (CoderSattu) -- https://abhisat.com

# In[ ]:


import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

def get_image_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        img_urls = []

        for img in img_tags:
            img_url = img.get('src')
            if img_url:
                # Make sure the URL is absolute
                img_url = urljoin(url, img_url)
                if img_url.lower().endswith(('.webp','.jpeg','.jpg','.png')):
                    img_urls.append(img_url)
        return img_urls
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return []

def get_unique_filename(folder_path, base_name):
    name, ext = os.path.splitext(base_name)
    counter = 1
    unique_name = base_name

    while os.path.exists(os.path.join(folder_path, unique_name)):
        unique_name = f"{name}_{counter}{ext}"
        counter += 1

    return unique_name

def download_image(url, folder_path='downloaded_images'):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        base_name = url.split('/')[-1]
        unique_name = get_unique_filename(folder_path, base_name)
        file_path = os.path.join(folder_path, unique_name)

        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        
        print(f"Downloaded {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

def download_all_images(base_url):
    image_links = get_image_links(base_url)
    if not image_links:
        print("No images found.")
        return

    for img_link in image_links:
        download_image(img_link)

if __name__ == "__main__":
    url = input("Enter the URL to scrape for images: ")
    download_all_images(url)

