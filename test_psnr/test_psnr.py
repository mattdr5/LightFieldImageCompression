from skimage.metrics import peak_signal_noise_ratio as psnr
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_psnr(img1, img2):
      # Converte le immagini in scala di grigi se necessario
    if img1.shape[-1] == 3:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        
    return psnr(img1, img2)
    

# Funzione per caricare le immagini da una cartella
def load_images(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        img = cv2.imread(os.path.join(folder_path, filename))
        if img is not None:
            images.append((img, filename))  # Includi il nome del file insieme all'immagine
    return images

# Cartella contenente le immagini originali (percorso relativo allo script)
original_folder = "./test_psnr/images/"

# Immagine originale (sostituisci 'original.jpg' con il nome effettivo)
original_image = cv2.imread(os.path.join(original_folder, "original.webp"))

# Carica tutte le immagini filtrate dalla cartella
filtered_images_list = load_images(original_folder)

# Valori PSNR di riferimento dallo studio
# Dati presi da https://www.ponomarenko.info/psnrhvsm.htm
reference_psnrs = {
    "original": float('inf'),
    "masked": 26.18
}

# Imposta la griglia per la visualizzazione
num_images = len(filtered_images_list)
num_cols = 2
num_rows = (num_images // num_cols) + (num_images % num_cols > 0)  # Calcola il numero di righe necessarie
fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 8))

# Appiattisci gli assi se ci sono più righe
axes = axes.flatten()

errors = []
# Confronta l'immagine originale con tutte le immagini filtrate
for idx, (filtered_img, filename) in enumerate(filtered_images_list):

    # Calcola l'indice PSNR
    psnr_value = calculate_psnr(original_image, filtered_img)
    print(filename, "- ", psnr_value)

    reference_psnr = reference_psnrs.get(filename.split('.')[0], 0.0)  # 0.0 se il nome del file non è presente nei riferimenti

    # Escludi l'immagine originale dal calcolo dell'errore
    if filename.split('.')[0] == 'original':
        relative_error = 0.0
    else:
        relative_error = np.abs(psnr_value - reference_psnr) / reference_psnr

    print(filename, "-", relative_error)
    errors.append(relative_error)

    axes[idx].imshow(cv2.cvtColor(filtered_img, cv2.COLOR_BGR2RGB))
    axes[idx].set_title(f"{filename}\nPSNR: {psnr_value:.3f}")
    axes[idx].axis('off')

# Rimuovi gli assi delle immagini inutilizzati
for idx in range(num_images, len(axes)):
    fig.delaxes(axes[idx])

plt.tight_layout()
plt.show()

average_psnr_mre = np.mean(errors)
print(f"---> Errore relativo medio PSNR (MRE): {average_psnr_mre:.3f}")