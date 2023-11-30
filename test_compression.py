import os
import subprocess
import sys
import pathlib
import time

# Importa tutte le funzioni specifiche di compressione video
from VideoCompressionHEVC import comp_HEVC
from VideoCompressionHEVCvls import comp_HEVC_visuallyLS
from VideoCompressionAV1 import comp_AV1
from VideoCompressionAV1vls import comp_AV1_visuallyLS
from VideoCompressionFFV1 import comp_FFV1
from VideoCompressionHUFFYUV import comp_HUFFYUV
from VideoCompressionUTVideo import comp_UTVIDEO
from VideoCompressionVP9 import comp_VP9
from VideoCompressionVP9vls import comp_VP9_visuallyLS
from VideoCompressionMagicYUV import comp_MagicYUV
from VideoCompressionDirac import comp_Dirac, comp_Dirac_Lossless
from VideoCompressionFLV1 import comp_FLV1
from VideoCompressionSNOW import comp_Snow, comp_Snow_Lossless
from VideoCompressionJPEG2000 import comp_jpeg2000, comp_JPEG2000_Lossless
from VideoCompressionMPEG4 import comp_MPEG4
from VideoCompressionCirrusLogic import comp_cljr
from VideoCompressionProres import comp_ProRes
from VideoCompressionMJPEG import comp_MJPEG
from VideoCompressionFFVHUFF import comp_FFVHUFF
from VideoCompressionLCL import comp_LCL

from random_dataset import randomizza_e_copia_files

import csv
import os


def salva_risultati_compressione_csv(risultati, file_csv):
    """
    Scrive i risultati della compressione video in un file CSV.

    Parameters:
    - risultati (dict): Dizionario contenente i risultati della compressione video.
    - file_csv (str): Il percorso del file CSV in cui scrivere i risultati.

    Raises:
    - Exception: Lanciato se si verifica un errore durante la scrittura del file CSV.
    """
    try:
        with open(file_csv, 'w', newline='') as csvfile:
            # Definisci i nomi delle colonne
            fieldnames = ['Dataset', 'Algoritmo', 'Rapporto compressione', 'Tempo compressione', 'Dimensione iniziale', 'Dimensione finale']

            # Crea un writer CSV
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Scrivi l'intestazione
            writer.writeheader()

            for risultato in risultati:
                writer.writerow(risultato)

        print(f"I risultati sono stati scritti nel file CSV: {file_csv}")

    except Exception as e:
        raise Exception(f"Errore durante la scrittura del file CSV: {str(e)}")


def get_valid_extension(algo):
    valid_extensions = {
        "HEVC": ".mp4",
        "HEVC-VS": ".mp4",
        "AV1": ".mkv",
        "AV1-VS": ".mkv",
        "FFV1": ".avi",
        "HUFFYUV": ".avi",
        "UTVIDEO": ".avi",
        "VP9": ".webm",
        "VP9-VS": ".webm",
        "MagicYUV": ".avi",
        "Dirac": ".drc",
        "Dirac-LS": ".drc",
        "FLV1": ".flv",
        "SNOW": ".avi",
        "SNOW-LS": ".avi",
        "JPEG2000": ".mp4",
        "JPEG2000-LS": ".mp4",
        "MPEG4": ".avi",
        "CLJR": ".avi",
        "ProRes": ".mov",
        "MJPEG": ".avi",
        "FFVHUFF": ".avi",
        "LCL": ".avi"

    }

    return valid_extensions.get(algo)

#Inserire il dataset da utilizzare, in particolare specificare i nomi delle immagini
datasets = {
    "ArtGallery2": "./dataset/ArtGallery2/Frame_%3d.png",
    "ArtGallery2_random": "./dataset/ArtGallery2_random/Frame_%3d.png",
    "Dragons": "./dataset/Dragons/dragons-%2d.png",
    "Dragons_random": "./dataset/Dragons_random/Frame_%3d.png",
    "Fish": "./dataset/Fish/fishi-%2d.png",
    "Fish_random": "./dataset/Fish_random/Frame_%3d.png",
    "Dice": "./dataset/Dice/dice-%2d.png",
    "Dice_random": "./dataset/Dice_random/Frame_%3d.png",
    "Messerschmitt": "./dataset/Messerschmitt/messerschmitt-%2d.png",
    "Messerschmitt_random": "./dataset/Messerschmitt_random/Frame_%3d.png",
    "Shrubbery": "./dataset/Shrubbery/shrubbery-%2d.png",
    "Shrubbery_random": "./dataset/Shrubbery_random/Frame_%3d.png",
    "bicycle": "./dataset/bicycle/input_Cam%3d.png",
    "herbs": "./dataset/herbs/input_Cam%3d.png",
    "bicycle_random": "./dataset/bicycle_random/Frame_%3d.png",
    "herbs_random": "./dataset/herbs_random/Frame_%3d.png"
}

#Inserire qui gli algoritmi di compressione video da analizzare

algorithms = ["FFV1", "HEVC", "HUFFYUV", "UTVIDEO", "VP9", "HEVC-VS", "VP9-VS", "FLV1", "CLJR", "MPEG4", "MJPEG", "ProRes", "MagicYUV", "FFVHUFF", "LCL"] 


#Definire la cartella di output per la compressione
output_dir = "./compressione_test"
os.makedirs(output_dir, exist_ok=True)

def run_video_compression(algo, input_path, output_extension, output_path):
    if output_extension is None:
        print(f"Algoritmo non supportato: {algo}")
        return

    # Modifica il blocco switch per gestire la compressione direttamente
    if algo == "HEVC":
        if pathlib.Path(output_path).suffix == ".mp4":
            return comp_HEVC(input_path, output_path)
        else:
            print("Per HEVC l'estensione del file in output deve essere .mp4")
    elif algo == "HEVC-VS":
        if pathlib.Path(output_path).suffix == ".mp4":
            return comp_HEVC_visuallyLS(input_path, output_path)
        else:
            print("Per HEVC-VS l'estensione del file in output deve essere .mp4")
    elif algo == "AV1":
        if pathlib.Path(output_path).suffix == ".mkv":
            return comp_AV1(input_path, output_path)
        else:
            print("Per AV1 l'estensione del file in output deve essere .mkv")
    elif algo == "AV1-VS":
        if pathlib.Path(output_path).suffix == ".mkv":
            return comp_AV1_visuallyLS(input_path, output_path)
        else:
            print("Per AV1-VS l'estensione del file in output deve essere .mkv")
    elif algo == "FFV1":
        if pathlib.Path(output_path).suffix == ".avi":
            return comp_FFV1(input_path, output_path)
        else:
            print("Per FFV1 l'estensione del file in output deve essere .avi")
    elif algo == "HUFFYUV":
        if pathlib.Path(output_path).suffix == ".avi":
            return comp_HUFFYUV(input_path, output_path)
        else:
            print("Per HUFFYUV l'estensione del file in output deve essere .avi")
    elif algo == "UTVIDEO":
        if pathlib.Path(output_path).suffix == ".avi":
            return comp_UTVIDEO(input_path, output_path)
        else:
            print("Per UTVIDEO l'estensione del file in output deve essere .avi")
    elif algo == "VP9":
        if pathlib.Path(output_path).suffix == ".webm":
            return comp_VP9(input_path, output_path)
        else:
            print("Per VP9 l'estensione del file in output deve essere .webm")
    elif algo == "VP9-VS":
        if pathlib.Path(output_path).suffix == ".webm":
            return comp_VP9_visuallyLS(input_path, output_path)
        else:
            print("Per VP9-VS l'estensione del file in output deve essere .webm")
    elif algo == "MagicYUV":
        if pathlib.Path(output_path).suffix == ".avi":
           return comp_MagicYUV(input_path, output_path)
        else:
            print("Estensione di output per MagicYUV deve essere .avi")
    elif algo == "Dirac":
        if pathlib.Path(output_path).suffix == ".drc":
            return comp_Dirac(input_path, output_path)
        else:
            print("Estensione di output per Dirac deve essere .drc")
    elif algo == "Dirac-LS":
        if pathlib.Path(output_path).suffix == ".drc":
            return comp_Dirac_Lossless(input_path, output_path)
        else:
            print("Estensione di output per Dirac-LS deve essere .drc")
    elif algo == "FLV1":
        if pathlib.Path(output_path).suffix == ".flv":
           return comp_FLV1(input_path, output_path)
        else:
            print("Estensione di output per FLV1 deve essere .flv")
    elif algo == "SNOW":
        if pathlib.Path(output_path).suffix == ".avi":
            return comp_Snow(input_path, output_path)
        else:
            print("Estensione di output per SNOW deve essere .avi")
    elif algo == "SNOW-LS":
        if pathlib.Path(output_path).suffix == ".avi":
            return comp_Snow_Lossless(input_path, output_path)
        else:
            print("Estensione di output per SNOW-LS deve essere .avi")
    elif algo == "JPEG2000":
        if pathlib.Path(output_path).suffix == ".mp4":
            return comp_jpeg2000(input_path, output_path)
        else:
            print("Estensione di output per JPEG2000 deve essere .mp4")
    elif algo == "JPEG2000-LS":
        if pathlib.Path(output_path).suffix == ".mp4":
            return comp_JPEG2000_Lossless(input_path, output_path)
        else:
            print("Estensione di output per JEPG2000-LS deve essere .mp4")
    elif algo == "MPEG4":
        if pathlib.Path(output_path).suffix == ".avi":
            return comp_MPEG4(input_path, output_path)
        else:
            print("Estensione di output per MPEG4 deve essere .avi")
    elif algo == "CLJR":
        if pathlib.Path(output_path).suffix == ".avi":
            return comp_cljr(input_path, output_path)
        else:
            print("Estensione di output per CLJR deve essere .avi")
    elif algo == "ProRes":
        if pathlib.Path(output_path).suffix == ".mov":
            return comp_ProRes(input_path, output_path)
        else:
            print("Estensione di output per ProRes deve essere .mov")
    elif algo == "MJPEG":
        if pathlib.Path(output_path).suffix == ".avi":
            return comp_MJPEG(input_path, output_path)
        else:
            print("Estensione di output per MJPEG deve essere .avi")
    elif algo == "FFVHUFF":
        if pathlib.Path(output_path).suffix == ".avi":
            return comp_FFVHUFF(input_path, output_path)
        else:
            print("Per FFVHUFF l'estensione del file in output deve essere .avi")
    elif algo == "LCL":
        if pathlib.Path(output_path).suffix == ".avi":
            return comp_LCL(input_path, output_path)
        else:
            print("Per LCL l'estensione del file in output deve essere .avi")
    else:
        print(f"Algoritmo non riconosciuto: {algo}")


# Lista per archiviare i risultati
risultati = []
# Itera sui dataset e algoritmi
for dataset, input_path in datasets.items():
    dataset_output_dir = os.path.join(output_dir, dataset)
    os.makedirs(dataset_output_dir, exist_ok=True)

    for algo in algorithms:
        # Ottenere l'estensione valida per l'algoritmo corrente
        output_extension = get_valid_extension(algo)

        # Creare il percorso completo per il file di output
        output_path = os.path.join(dataset_output_dir, f"{algo}_output{output_extension}")

    
        dimensione_iniziale, dimensione_finale, rapporto_compressione, tempo_compressione = run_video_compression(algo, input_path, output_extension, output_path)
        print(f"Rapporto compressione {algo} su dataset {dataset}: {rapporto_compressione}")
        print(f"Tempo impiegato da {algo} per la compressione sul dataset {dataset}: {tempo_compressione} secondi")

         # Salvare i risultati nella lista
        risultati.append({
            "Dataset": dataset,
            "Algoritmo": algo,
            "Rapporto compressione": rapporto_compressione,
            "Tempo compressione": tempo_compressione,
            "Dimensione iniziale": dimensione_iniziale,
            "Dimensione finale": dimensione_finale
        })

        salva_risultati_compressione_csv(risultati=risultati, file_csv="risultati_compressione.csv")