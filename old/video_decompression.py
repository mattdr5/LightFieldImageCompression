import av
from PIL import Image
import time
import os
import sys
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage import io
import numpy as np
import cv2
import csv

# Definizione dei dataset e degli algoritmi
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


def get_dataset_path(input_path):
    # Divide il percorso in parti usando lo slash o il backslash come separatore
    parts = input_path.split("/") + input_path.split("\\")

    # Cerca il nome del dataset nelle parti del percorso
    for part in parts:
        if part in datasets:
            return part

    # Se non trova corrispondenze, restituisci None
    return None

def extract_algorithm_name(file_path):
    # Ottieni il nome del file dalla directory
    file_name = os.path.basename(file_path)

    # Dividi il nome del file in base al separatore ('_')
    parts = file_name.split('_')

    # Se il file ha almeno due parti, la prima sarà il nome dell'algoritmo
    if len(parts) >= 2:
        algorithm_name = parts[0]
        return algorithm_name
    else:
        # Se non è possibile estrarre il nome dell'algoritmo, restituisci None o gestisci l'errore secondo necessità
        return None


def decompress_video(input_path, output_path):
    img_dec = ""
    container = None
    try:
        container = av.open(input_path, mode="r")
    except av.AVError as e:
        print("Errore nell'apertura del video:", e)
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
        print("Errore nella decodifica del video:", e)
        return None

    return img_dec


def calculate_ssim(img1, img2):
    # Converte le immagini in scala di grigi se necessario
    if img1.shape[-1] == 3:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Calcola l'indice SSIM
    index, diff = ssim(img1, img2, full=True)
    return index, diff

def numerical_sort(value):
    # Estrai il numero dalla stringa del file
    return int(''.join(filter(str.isdigit, value)))

def calculate_ssim_between_datasets(dataset1_path, dataset2_path):
    print("-> Apro: ", dataset1_path)
    # Ottieni la lista di file nelle directory dei dataset
    dataset1_files = sorted(os.listdir(dataset1_path), key=numerical_sort)
    
    print("-> Apro: ", dataset2_path)
    dataset2_files = sorted(os.listdir(dataset2_path), key=numerical_sort)

    # Assicurati che entrambi i dataset abbiano lo stesso numero di immagini
    assert len(dataset1_files) == len(dataset2_files), "I dataset devono avere lo stesso numero di immagini"
    

    ssim_values = []

    # Calcola l'indice SSIM per ogni coppia di immagini
    for file1, file2 in zip(dataset1_files, dataset2_files):
        print("--->confronto FILE 1: ", file1, " con FILE2: ", file2)
        img1 = io.imread(os.path.join(dataset1_path, file1))
        img2 = io.imread(os.path.join(dataset2_path, file2))

        assert img1.shape == img2.shape, f"Le dimensioni delle immagini {file1} e {file2} devono essere uguali"

        ssim_index, _ = calculate_ssim(img1, img2)
        ssim_values.append(ssim_index)

    return ssim_values

def calculate_psnr(img1, img2):
      # Converte le immagini in scala di grigi se necessario
    if img1.shape[-1] == 3:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        
    return psnr(img1, img2)

def calculate_psnr_between_datasets(dataset1_path, dataset2_path):
    # Ottieni la lista di file nelle directory dei dataset
    dataset1_files = sorted(os.listdir(dataset1_path), key=numerical_sort)
    
    print("-> Apro: ", dataset2_path)
    dataset2_files = sorted(os.listdir(dataset2_path), key=numerical_sort)

    # Assicurati che entrambi i dataset abbiano lo stesso numero di immagini
    assert len(dataset1_files) == len(dataset2_files), "I dataset devono avere lo stesso numero di immagini"

    psnr_values = []

    # Calcola l'indice PSNR per ogni coppia di immagini
    for file1, file2 in zip(dataset1_files, dataset2_files):
        print("confronto FILE 1: ", file1, " con FILE2: ", file2)
        img1 = io.imread(os.path.join(dataset1_path, file1))
        img2 = io.imread(os.path.join(dataset2_path, file2))

        assert img1.shape == img2.shape, f"Le dimensioni delle immagini {file1} e {file2} devono essere uguali"

        psnr_value = calculate_psnr(img1, img2)
        psnr_values.append(psnr_value)

    return psnr_values

def calculate_metrics(dataset_path, output_path):
    path_reference_dataset = datasets[dataset_name]

    # Calcola SSIM
    print("---> Differenza tra ", os.path.dirname(path_reference_dataset) , " e ", os.path.dirname(output_path))
    ssim_values = calculate_ssim_between_datasets(os.path.dirname(path_reference_dataset), os.path.dirname(output_path))
    average_ssim = np.mean(ssim_values)

    # Calcola PSNR
    psnr_values = calculate_psnr_between_datasets(os.path.dirname(path_reference_dataset), os.path.dirname(output_path))
    average_psnr = np.mean(psnr_values)

    return {
        "Dataset": dataset_name,
        "Algoritmo": extract_algorithm_name(dataset_path),
        "Average SSIM": average_ssim,
        "Average PSNR": average_psnr
    }

def save_results_to_csv(results, csv_file_path):

    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Dataset", "Algoritmo", "Average SSIM", "Average PSNR"])
        writer.writeheader()

        for riga in results:
            writer.writerow(riga)

    print(f"I risultati sono stati aggiunti a {csv_file_path}")

# Handling command line arguments
input_path = ""
output_path = ""

if len(sys.argv[1:]) == 2:
    input_path = sys.argv[1]
    output_path = sys.argv[2]
else:
    print("Specify in sequence:\n- INPUT_PATH (e.g., output.mp4)\n- OUTPUT_PATH (e.g., result/frame%d.png)")
    exit()

print("Input path: ", input_path)
print("Output path: ", output_path)

decompress_video(input_path , output_path)

# Trova il nome del dataset nel percorso dell'input
dataset_name = get_dataset_path(input_path)

# Lista per archiviare i risultati
risultati = []
# Se il nome del dataset è valido, calcola le metriche e salva i risultati in un dizionario
if dataset_name:
    metrics_results = calculate_metrics(input_path, output_path)
    risultati.append(metrics_results) 
    print(f"Valori SSIM e PSNR:\n{metrics_results}")
else:
    print("Nome del dataset non riconosciuto nel percorso dell'input.")


