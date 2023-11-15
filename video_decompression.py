import av
from PIL import Image
import os
import sys

# Definizione dei dataset e degli algoritmi
datasets = {
    "ArtGallery2": "./dataset/ArtGallery2/Frame_%3d.png",
    "ArtGallery2_random": "./dataset/ArtGallery2_random/Frame_%3d.png",
    "Dragons": "./dataset/Dragons/dragons-%2d.png",
    "Dragons_random": "./dataset/Dragons_random/Frame_%3d.png",
    "OpEX": "./dataset/OpEx/%d.png",
    "OpEX_random": "./dataset/OpEx_random/Frame_%3d.png",
    "Fish": "./dataset/Fish/fishi-%2d.png",
    "Fish_random": "./dataset/Fish_random/Frame_%3d.png",
    "Dice": "./dataset/Dice/dice-%2d.png",
    "Dice_random": "./dataset/Dice_random/Frame_%3d.png",
    "Messerschmitt": "./dataset/Messerschmitt/messerschmitt-%2d.png",
    "Messerschmitt_random": "./dataset/Messerschmitt_random/Frame_%3d.png",
    "Shrubbery": "./dataset/Shrubbery/shrubbery-%2d.png",
    "Shrubbery_random": "./dataset/Shrubbery_random/Frame_%3d.png"
}



def compare_images(image_path1, image_path2):
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

    width1, height1 = image1.size
    width2, height2 = image2.size

    if (width1 != width2) or (height1 != height2):
        print("Error: Images have different sizes")
        return None

    different_pixels = 0
    total_pixels = width1 * height1
    for x in range(width1):
        for y in range(height1):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            if pixel1 != pixel2:
                different_pixels += 1

    percentage = (total_pixels - different_pixels) / total_pixels * 100
    return percentage

def get_dataset_path(input_path):
    # Divide il percorso in parti usando lo slash o il backslash come separatore
    parts = input_path.split("/") + input_path.split("\\")

    # Cerca il nome del dataset nelle parti del percorso
    for part in parts:
        if part in datasets:
            return datasets[part]

    # Se non trova corrispondenze, restituisci None
    return None


def decompress_video(input_path, output_path):
    img_dec = ""
    container = None
    try:
        container = av.open(input_path, mode="r")
    except av.AVError as e:
        print("Error opening the video file:", e)
        return None

    stream = container.streams.video[0]
    count = 0

    try:
        for frame in container.decode(stream):
            if count == 0:
                img_dec = frame.to_image()

            frame.to_image().save(output_path % count)
            count += 1
    except av.AVError as e:
        print("Error decoding the video:", e)
        return None

    return img_dec


# Handling command line arguments
input_path = ""
output_path = ""

if len(sys.argv[1:]) == 2:
    input_path = sys.argv[1]
    output_path = sys.argv[2]
else:
    print("Specify in sequence:\n- INPUT_PATH (e.g., output.mp4)\n- OUTPUT_PATH (e.g., result/frame%d.png)")
    exit()

decompress_video(input_path , output_path)

