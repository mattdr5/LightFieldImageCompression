import os
import platform
import subprocess
import time
from dataset_options import DATASET_OPTIONS
import re

def calcola_rapporto_compressione(input_path, output_path):
    """
    Calcola il rapporto di compressione tra la dimensione del file
    originale e quella del file compresso.

    Parameters:
    - input_path (str): Il percorso del file video originale.
    - output_path (str): Il percorso del file video compresso.

    Returns:
    - float: Il rapporto di compressione (dimensione originale / dimensione compressa).
    """
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

def comp_MPEG4(input_path, output_path):          #Support only Lossy compression
    dataset = None

# Cerca il nome del dataset nel file dataset_options.py
    for dataset_name, options in DATASET_OPTIONS.items():
    # Utilizza un'espressione regolare per cercare il nome del dataset nel percorso del file di input
        if re.search(rf'\b{re.escape(dataset_name.lower())}\b', input_path.lower()):
            dataset = dataset_name.lower()
            break

    # Set the input and output file names
    input_file = input_path
    output_file = output_path

    # Check the operating system and set the path to the FFmpeg executable accordingly
    if platform.system() == 'Windows':
        ffmpeg_executable = "./ffmpeg/bin/ffmpeg.exe "
    else:
        ffmpeg_executable = "ffmpeg"


     # Registra il tempo di inizio
    start_time = time.time()

    # Get the dataset-specific options for FLV1 from the DATASET_OPTIONS dictionary
    dataset_options = DATASET_OPTIONS.get(dataset, {}).get('MPEG4', [])

    # Call ffmpeg to compress the video with MPEG-4 Part 2 codec (libxvid)
    subprocess.run([ffmpeg_executable, "-framerate", "120", "-i", input_file, "-c:v", "mpeg4"] + dataset_options + [output_file])

    # Registra il tempo di fine
    end_time = time.time()
    
    # Calcola il rapporto di compressione utilizzando la funzione creata
    dimensione_iniziale, dimensione_finale, rapporto_compressione = calcola_rapporto_compressione(input_path, output_path)
    tempo_compressione = end_time - start_time

    return dimensione_iniziale, dimensione_finale, rapporto_compressione, tempo_compressione
    
