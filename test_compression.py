import os
import subprocess
import pathlib

# Definizione dei dataset e degli algoritmi
datasets = {
    "ArtGallery2": "./dataset/ArtGallery2/Frame_%3d.png",
    "Dragons": "./dataset/Dragons/dragons-%2d.png",
    "11px_linear": "./dataset/11px_linear/%d.png",
    "Fish":"./dataset/Fish/fishi-%2d.png",
    "Dice":"./dataset/Dice/dice-%2d.png",
    "Messerschmitt":"./dataset/Messerschmitt/messerschmitt-%2d.png",
    "Shrubbery":"./dataset/Shrubbery/shrubbery-%2d.png"
}

algorithms = ["Theora"]

# Cartella di output
output_dir = "./compressione_test"
os.makedirs(output_dir, exist_ok=True)

def run_video_compression(algo, input_path, output_extension, output_path):
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
        "Theora": ".ogv",
        "MagicYUV": ".avi",
        "Lagarith": ".avi"
    }

    if algo not in valid_extensions:
        print(f"Algoritmo non supportato: {algo}")
        return

    expected_extension = valid_extensions[algo]

    if output_extension != expected_extension:
        print(f"Per {algo} l'estensione del file in output deve essere {expected_extension}")
        return

    cmd = f"python video_compression.py {algo} {input_path} {output_path}"
    subprocess.run(cmd, shell=True)

for dataset, input_path in datasets.items():
    dataset_output_dir = os.path.join(output_dir, dataset)
    os.makedirs(dataset_output_dir, exist_ok=True)

    for algo in algorithms:
        if algo in ["HEVC", "HEVC-VS"]:
            output_extension = ".mp4"
        elif algo in ["AV1", "AV1-VS"]:
            output_extension = ".mkv"
        elif algo in ["FFV1", "HUFFYUV", "UTVIDEO", "MagicYUV", "Lagarith"]:
            output_extension = ".avi"
        elif algo in ["VP9", "VP9-VS"]:
            output_extension = ".webm"
        elif algo in ["Theora"]:
            output_extension = ".ogv"
        else:
            print(f"Algoritmo non supportato: {algo}")
            continue

        output_path = os.path.join(dataset_output_dir, f"{algo}_output{output_extension}")
        run_video_compression(algo, input_path, output_extension, output_path)