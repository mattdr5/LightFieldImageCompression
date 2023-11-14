import imageio.v3 as iio
from pathlib import Path
import imageio.plugins.pyav as pyav
import av
from PIL import Image,ImageChops
import numpy as np
import sys

input_path=""
output_path=""
if(len(sys.argv[1:]) == 2):
    input_path=sys.argv[1]
    output_path=sys.argv[2]
else:
    print("Specifica in sequenza: \n- INPUT_PATH (es. output.mp4)\n- OUTPUT_PATH (es. result/frame%d.png)")
    exit()

imgDec=""
container = av.open(input_path,mode="r") 
stream= container.streams.video[0]
count=0
for frame in container.decode(stream):
    if(count==0):
        imgDec=frame.to_image()
    frame.to_image().save(output_path % count)
    count+=1
    


#DIFFERENZA PIXEL PER PIXEL A COLORI
# Open both images
image1 = Image.open("./dataset/ArtGallery2/Frame_000.png ")
image2 = Image.open(output_path.replace("%d","0"))


# Get the width and height of both images
width1, height1 = image1.size
width2, height2 = image2.size

# Check if the images have the same size
if (width1 != width2) or (height1 != height2):
    print("Error: Images have different sizes")
else:
    # Compare the pixels of both images
    different_pixels = 0
    total_pixels = width1 * height1
    for x in range(width1):
        for y in range(height1):
            # Get the pixel values of both images at position (x, y)
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            # Compare the pixel values
            if pixel1 != pixel2:
                different_pixels += 1

    # Calculate the percentage of equality
    percentage = (total_pixels - different_pixels) / total_pixels * 100
    print("Percentage of equality: {:.2f}%".format(percentage))


"""
#DIFFERENZA IN SCALA DI GRIGI

i1 = Image.open("./ArtGallery2/Frame_000.png")
i2 = Image.open("./result/frame0.png")
assert i1.mode == i2.mode, "Different kinds of images."
assert i1.size == i2.size, "Different sizes."

pairs = zip(i1.getdata(), i2.getdata())
if len(i1.getbands()) == 1:
    # for gray-scale jpegs
    dif = sum(abs(p1-p2) for p1,p2 in pairs)
else:
    dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

ncomponents = i1.size[0] * i1.size[1] * 3
print ("Difference (percentage):", (dif / 255.0 * 100) / ncomponents)
"""