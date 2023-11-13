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


def comp_FFV1(input_path,output_path):
    # Set the input and output file names
    input_file = input_path
    output_file = output_path

    # Call ffmpeg to compress the video
    #versione 3 con coder Range Coder
    subprocess.run(["./ffmpeg/bin/ffmpeg","-framerate", "120","-i", input_file,"-level","3","-coder","2","-c:v", "ffv1",output_file])

    #calcolo compress ratio
    size = 0
    Folderpath = os.path.abspath(os.path.dirname(input_path))
    for path, dirs, files in os.walk(Folderpath):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)

    videoSize=os.stat(os.path.abspath(output_path)).st_size
    print("Compression Ratio:" +str(size/videoSize))