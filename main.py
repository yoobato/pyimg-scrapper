from bs4 import *
from pathlib import Path
import requests


def find_all_images(urL):
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.findAll('img')    # Find all img tag

    return images


def download_images(images, save_path):
    print(f'# of images: {len(images)}')

    if len(images) > 0:
        for i, image in enumerate(images):
            image_url = image['src']
            response = requests.get(image_url)

            with open(f'{save_path}/image_{i + 1}.jpg', 'wb+') as f:
                f.write(response.content)
            
            print(f'{i + 1} / {len(images)} downloaded.')
        
        print('All images have been downloaded.')


if __name__ == '__main__':
    url = input('(1) Enter the URL: ')

    # Create new directory if not exists
    download_dir_name = input('(2) Enter the name of directory save images: ')
    download_dir_path = f'./{download_dir_name}'
    Path(download_dir_path).mkdir(parents=True, exist_ok=True)

    images = find_all_images(url)
    download_images(images, download_dir_path)
 