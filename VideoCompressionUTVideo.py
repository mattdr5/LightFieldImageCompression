import cv2
import imageio
import imageio.v3 as iio
from pathlib import Path
import imageio.plugins.pyav as pyav
import av
from PIL import Image, ImageChops
import numpy as np
import os
import subprocess
import platform  # Import the platform module to check the operating system

def comp_UTVIDEO(input_path, output_path):
    # Set the input and output file names
    input_file = input_path
    output_file = output_path

    # Check the operating system and set the path to the FFmpeg executable accordingly
    if platform.system() == 'Windows':
        print("Windows")
        ffmpeg_executable = "./ffmpeg/bin/ffmpeg.exe "
    else:
        ffmpeg_executable = "ffmpeg "

    # Call ffmpeg to compress the video
    subprocess.run([ffmpeg_executable, "-framerate", "120", "-i", input_file, "-c:v", "utvideo", output_file])

    # Calcolo compress ratio
    size = 0
    Folderpath = os.path.abspath(os.path.dirname(input_path))
    for path, dirs, files in os.walk(Folderpath):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)

    videoSize = os.stat(os.path.abspath(output_path)).st_size
    print("Compression Ratio:" + str(size / videoSize))

