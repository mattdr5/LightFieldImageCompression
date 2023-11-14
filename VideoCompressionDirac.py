import os
import platform
import subprocess

def comp_Dirac(input_path, output_path):
    # Set the input and output file names
    input_file = input_path
    output_file = output_path

    # Check the operating system and set the path to the FFmpeg executable accordingly
    if platform.system() == 'Windows':
        ffmpeg_executable = "./ffmpeg/bin/ffmpeg.exe "
    else:
        ffmpeg_executable = "ffmpeg"

    # Call ffmpeg to compress the video with Dirac codec
    subprocess.run([ffmpeg_executable, "-i", input_file, "-c:v", "dirac", output_file])

    # Calculate compression ratio
    size = 0
    folder_path = os.path.abspath(os.path.dirname(input_path))
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)

    video_size = os.stat(os.path.abspath(output_path)).st_size
    print("Compression Ratio: " + str(size / video_size))
