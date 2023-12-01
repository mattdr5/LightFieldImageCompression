from skimage.metrics import structural_similarity as ssim
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_ssim(img1, img2):
    # Converte le immagini in scala di grigi se necessario
    if img1.shape[-1] == 3:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Assicurati che le immagini abbiano le stesse dimensioni
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Calcola l'indice SSIM
    index, _ = ssim(img1, img2, full=True)
    return index

# Funzione per caricare le immagini da una cartella
def load_images(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        img = cv2.imread(os.path.join(folder_path, filename))
        if img is not None:
            images.append((img, filename))  # Includi il nome del file insieme all'immagine
    return images

# Cartella contenente le immagini (percorso relativo allo script)
images_folder = "test_ssim/images/"

# Immagine originale (sostituisci 'original.jpg' con il nome effettivo)
original_image = cv2.imread(os.path.join(images_folder, "original.jpg"))

# Carica tutte le immagini dalla cartella
image_list = load_images(images_folder)

# Valori SSIM di riferimento dallo studio
# Valori di riferimento presi da: https://www.cns.nyu.edu/~lcv/ssim/#test
reference_ssims = {
    "original": 1,
    "meanshift": 0.988,
    "contrast": 0.913,
    "impulse": 0.840,
    "blur": 0.694,
    "rumor": 0.662
}

# Imposta la griglia per la visualizzazione
num_images = len(image_list)
num_cols = 3
num_rows = (num_images // num_cols) + (num_images % num_cols > 0)  # Calcola il numero di righe necessarie
fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 8))

# Appiattisci gli assi se ci sono più righe
axes = axes.flatten()

errors = []
# Confronto immagine originale con tutte le immagini di test
for idx, (img, filename) in enumerate(image_list):
    ssim_index = calculate_ssim(original_image, img)
    reference_ssim = reference_ssims.get(filename.split('.')[0], 0.0)  # 0.0 se il nome del file non è presente nei riferimenti
    relative_error = np.abs(ssim_index - reference_ssim) / reference_ssim
    errors.append(relative_error)

    axes[idx].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axes[idx].set_title(f"{filename}\nSSIM: {ssim_index:.3f}\nErrore relativo: {relative_error:.3f}")
    axes[idx].axis('off')

# Rimuovi gli assi delle immagini inutilizzati
for idx in range(num_images, len(axes)):
    fig.delaxes(axes[idx])

plt.tight_layout()
plt.show()

# Calcola il MRE medio
average_mre = np.mean(errors)

print(f"---> Errore relativo medio (MRE): {average_mre:.3f}")
