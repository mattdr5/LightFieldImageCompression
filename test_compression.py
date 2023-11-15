import os
import subprocess

def get_valid_extension(algo):
    # Mapping degli algoritmi alle rispettive estensioni valide
    valid_extensions = {
        "HEVC": ".mp4",
        "AV1": ".mkv",
        "FFV1": ".avi",
        "HUFFYUV": ".avi",
        "UTVIDEO": ".avi",
        "VP9": ".webm",
        "Theora": ".ogv",
        "MagicYUV": ".avi",
        "Dirac": ".drc",
        "FLV1": ".flv",
        "SNOW": ".avi",
        "HAP": ".mov",
        "Cinepak": ".avi",
        "MPEG4": ".avi",
        "CLJR": ".avi"
    }

    return valid_extensions.get(algo)

datasets = {
    "ArtGallery2": "./dataset/ArtGallery2/Frame_%3d.png",
    "Dragons": "./dataset/Dragons/dragons-%2d.png",
    "11px_linear": "./dataset/11px_linear/%d.png",
    "Fish": "./dataset/Fish/fishi-%2d.png",
    "Dice": "./dataset/Dice/dice-%2d.png",
    "Messerschmitt": "./dataset/Messerschmitt/messerschmitt-%2d.png",
    "Shrubbery": "./dataset/Shrubbery/shrubbery-%2d.png"
}

algorithms = ["CLJR"]

output_dir = "./compressione_test"
os.makedirs(output_dir, exist_ok=True)

def run_video_compression(algo, input_path, output_extension, output_path):
    if output_extension is None:
        print(f"Algoritmo non supportato: {algo}")
        return

    # Comando per eseguire la compressione video
    cmd = f"python video_compression.py {algo} {input_path} {output_path}"
    subprocess.run(cmd, shell=True)

for dataset, input_path in datasets.items():
    dataset_output_dir = os.path.join(output_dir, dataset)
    os.makedirs(dataset_output_dir, exist_ok=True)

    for algo in algorithms:
        # Ottenere l'estensione valida per l'algoritmo corrente
        output_extension = get_valid_extension(algo)

        # Creare il percorso completo per il file di output
        output_path = os.path.join(dataset_output_dir, f"{algo}_output{output_extension}")

        # Eseguire la compressione video
        run_video_compression(algo, input_path, output_extension, output_path)