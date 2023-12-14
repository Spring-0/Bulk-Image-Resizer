import os
from PIL import Image


def resize_images(directory, width, height, maintain_ratio, quality=95):
    try:
        # Check if directory exists
        if not os.path.isdir(directory):
            print("The directory does not exist.")
            return

        # Validate width and height values
        if width <= 0 or height <= 0:
            print("Width and height must be greater than zero.")
            return
        
        files = os.listdir(directory)
        images = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

        if not images:
            print("No images found in the directory.")
            return

        # Resize images
        for image_name in images:
            image_path = os.path.join(directory, image_name)
            with Image.open(image_path) as img:
                if maintain_ratio:
                    img.thumbnail((width, height))
                else:
                    img = img.resize((width, height))
                img.save(image_path, quality=quality)

        print(f"Successfully resized {len(images)} images.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    try:
        directory = input("Enter the directory path: ")
        width = int(input("Enter the new width: "))
        height = int(input("Enter the new height: "))
        maintain_ratio = input("Maintain aspect ratio? (Y/N): ").lower() == 'y'
        quality = int(input("Enter the image quality (1-100): "))
        
        resize_images(directory, width, height, maintain_ratio, quality)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
    