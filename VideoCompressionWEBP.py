import cv2
import imageio
import imageio.v3 as iio
from pathlib import Path
import imageio.plugins.pyav as pyav
import av
from PIL import Image,ImageChops
import numpy as np
import os
import subprocess

# Set the input and output file names
input_file = "./ArtGallery2/Frame_%3d.png"
output_file = "./compressedWEBP/outputWEBP%d.webp"

# Call ffmpeg to compress the video
subprocess.run(["./ffmpeg/bin/ffmpeg","-i", input_file,"-c:v", "libwebp","-lossless","1",output_file])

#calcolo compress ratio
size = 0
Folderpath = r'C:\Users\vinny\Desktop\Desktop\Uni\CompressioneDati\Progetto_Compressione_Dati-master\ArtGallery2'
for path, dirs, files in os.walk(Folderpath):
    for f in files:
        fp = os.path.join(path, f)
        size += os.path.getsize(fp)

sizeComp=0
Folderpath = r'C:\Users\vinny\Desktop\Desktop\Uni\CompressioneDati\Progetto_Compressione_Dati-master\compressedWEBP'
for path, dirs, files in os.walk(Folderpath):
    for f in files:
        fp = os.path.join(path, f)
        sizeComp += os.path.getsize(fp)

print("Compression Ratio:" +str(size/sizeComp))