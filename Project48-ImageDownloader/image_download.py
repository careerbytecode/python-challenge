import os
import requests
from bs4 import BeautifulSoup

URL = "https://unsplash.com/s/photos/nature?orientation=landscape"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}
SAVE_DIR = "downloaded_images"
MIN_SIZE = 20 * 1024

os.makedirs(SAVE_DIR, exist_ok=True)

def download_images(url=URL, headers=HEADERS, save_dir=SAVE_DIR, min_size=MIN_SIZE, max_images=20):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    image_tags = soup.find_all("img")

    downloaded = 0
    for i, img in enumerate(image_tags):
        src = img.get("src")
        if src and src.startswith("http") and downloaded < max_images:
            try:
                img_response = requests.get(src, stream=True)
                img_response.raise_for_status()
                img_data = img_response.content

                if len(img_data) >= min_size:
                    filename = os.path.join(save_dir, f"image_{downloaded}.jpg")
                    with open(filename, "wb") as f:
                        f.write(img_data)
                    print(f"Downloaded image_{downloaded}.jpg ({len(img_data)//1024} KB)")
                    downloaded += 1
                else:
                    print(f"Skipped: image too small ({len(img_data)//1024} KB)")

            except Exception as e:
                print(f"Failed to download: {src} | Error: {e}")

    print(f"\nSuccessfully downloaded {downloaded} images to '{save_dir}'")

if __name__ == "__main__":
    download_images()

