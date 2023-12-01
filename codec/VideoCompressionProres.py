import os
import subprocess
import platform
import time

def calcola_rapporto_compressione(input_path, output_path):
    # Calcola la dimensione del file originale
    size_before = 0
    folder_path = os.path.abspath(os.path.dirname(input_path))
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(path, f)
            size_before += os.path.getsize(fp)

    # Calcola la dimensione del file compresso
    size_after = os.stat(os.path.abspath(output_path)).st_size

    # Calcola e restituisci il rapporto di compressione e altri dettagli
    return size_before, size_after, size_before / size_after if size_after != 0 else 0

def comp_ProRes(input_path, output_path):        #Support only Lossy compression

    input_file = input_path
    output_file = output_path

    # Check the operating system and set the path to the FFmpeg executable accordingly
    if platform.system() == 'Windows':
        print("Windows")
        ffmpeg_executable = "./ffmpeg/bin/ffmpeg.exe "
    else:
        ffmpeg_executable = "ffmpeg"

    # Record start time
    start_time = time.time()

    # Call ffmpeg to compress the video with ProRes codec
    subprocess.run([ffmpeg_executable, "-framerate", "120","-i", input_file, "-c:v", "prores_ks", "-profile:v", "3", output_file])

    # Record end time
    end_time = time.time()

    # Calcola il rapporto di compressione utilizzando la funzione creata
    dimensione_iniziale, dimensione_finale, rapporto_compressione = calcola_rapporto_compressione(input_path, output_path)
    tempo_compressione = end_time - start_time

    return dimensione_iniziale, dimensione_finale, rapporto_compressione, tempo_compressione


