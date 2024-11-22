import os
import requests
from concurrent.futures import ThreadPoolExecutor
API_KEY = "7UgYL8UGtK6Rmt7agCYbHH7AW5iboi8WbP7sp8bP"  
APOD_ENDPOINT = 'https://api.nasa.gov/planetary/apod'
OUTPUT_IMAGES = './output'
def get_apod_metadata(start_date: str, end_date: str, api_key: str) -> list:
    url = f"{APOD_ENDPOINT}?api_key={api_key}&start_date={start_date}&end_date={end_date}"
    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()
    
    return [item for item in data if item['media_type'] == 'image']
def download_image(image_data: dict):
    image_url = image_data['url']
    date = image_data['date']
    title = image_data['title'].replace(' ', '_').replace('/', '-')
    image_extension = image_url.split('.')[-1]
    image_filename = f"{date}_{title}.{image_extension}"
    image_path = os.path.join(OUTPUT_IMAGES, image_filename)

    print(f"Downloading {image_url}")
    response = requests.get(image_url)
    with open(image_path, 'wb') as file:
        file.write(response.content)
    print(f"Saved {image_filename}")
def download_apod_images(metadata: list):
    if not os.path.exists(OUTPUT_IMAGES):
        os.makedirs(OUTPUT_IMAGES)
    # Use ThreadPoolExecutor for concurrent downloads
    with ThreadPoolExecutor() as executor:
        executor.map(download_image, metadata)
def main():
    metadata = get_apod_metadata(
        start_date='2021-08-01',
        end_date='2021-09-30',
        api_key=API_KEY,
    )
    download_apod_images(metadata=metadata)
if __name__ == '__main__':
    main() 





