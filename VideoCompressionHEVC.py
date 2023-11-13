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

"""
c = 0
writer = imageio.get_writer('video.avi', format='py', mode='I', fps=10, macro_block_size= 1 )
#for i in range(26):
for j in range(12):
    if(j<10):
        imgBGR = cv2.imread("rawSPCdata/focus_imgs/2__refocus_0"+str(j)+".jpg")
    else:
        imgBGR = cv2.imread("rawSPCdata/focus_imgs/2__refocus_"+str(j)+".jpg")
    if imgBGR is not None:
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
        writer.append_data(imgRGB)
        c = c+1
writer.close()
print(c)
"""

"""
c = 0
images = list()
with iio.imopen("video.265", "w", plugin="pyav") as file:
    file.init_video_stream("libx265",fps=10)
    for j in range(12):
        if(j<10):
            img = Path("rawSPCdata/focus_imgs/2__refocus_0"+str(j)+".jpg")
        else:
            img = Path("rawSPCdata/focus_imgs/2__refocus_"+str(j)+".jpg")  
        c = c+1
        file.write_frame(iio.imread(img))

file.close()
print(c)


with iio.imopen("video.265","r") as file:
    for c in range(1,12):
        frame = file.read(index=2,constant_framerate=True)
        iio.imwrite("result/frame%d.jpg" % c, frame)
"""


"""
image=""
container = av.open("videoLOSLESS.mp4",mode="w") 
stream = container.add_stream("libx265",rate=12)
stream.width=1080
stream.height=1080
for j in range(12):
        if(j<10):
            path = Path("rawSPCdata/focus_imgs/2__refocus_0"+str(j)+".jpg")
        else:
            path = Path("rawSPCdata/focus_imgs/2__refocus_"+str(j)+".jpg")
        img = Image.open(path)
        if(j==0):
            image = img
        frame = av.VideoFrame.from_image(img)
        for packet in stream.encode(frame):
            container.mux(packet)

for packet in stream.encode():
        container.mux(packet)
container.close()

"""

def comp_HEVC(input_path,output_path):
    # Set the input and output file names
    input_file = input_path
    output_file = output_path

    # Call ffmpeg to compress the video
    subprocess.run(["./ffmpeg/bin/ffmpeg","-framerate", "120","-i", input_file,"-c:v", "libx265","-x265-params","lossless=1",output_file])

    #calcolo compress ratio
    size = 0
    Folderpath = os.path.abspath(os.path.dirname(input_path))
    for path, dirs, files in os.walk(Folderpath):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)

    videoSize=os.stat(os.path.abspath(output_path)).st_size
    print("Compression Ratio:" +str(size/videoSize))