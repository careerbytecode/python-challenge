from PIL import Image, ImageFilter
import os

IMAGE_PATH = "sample.jpg"
OUTPUT_DIR = "processed_images"

def ensure_output_dir(path):
    os.makedirs(path, exist_ok=True)

def process_image(image_path, output_dir):
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: File '{image_path}' not found.")
        return
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    resized = img.resize((300, 300))
    resized.save(os.path.join(output_dir, "resized.jpg"))
    print("Image resized to 300x300.")

    grayscale = img.convert("L")
    grayscale.save(os.path.join(output_dir, "grayscale.jpg"))
    print("Grayscale version saved.")

    blurred = img.filter(ImageFilter.BLUR)
    blurred.save(os.path.join(output_dir, "blurred.jpg"))
    print("Blur effect applied.")

def main():
    ensure_output_dir(OUTPUT_DIR)
    process_image(IMAGE_PATH, OUTPUT_DIR)

if __name__ == "__main__":
    main()

