import os

# Definizione dei dataset e degli algoritmi
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

# Cartella di output per la decompressione
decompression_dir = "./decompressione_test"
# Cartella di output
compression_dir = "./compressione_test"
os.makedirs(decompression_dir, exist_ok=True)

for dataset, input_format in datasets.items():
    dataset_output_dir = os.path.join(decompression_dir, dataset)
    os.makedirs(dataset_output_dir, exist_ok=True)

    for algo in algorithms:
        input_extension = {
            "HEVC": "mp4",
            "AV1": "mkv",
            "FFV1": "avi",
            "HUFFYUV": "avi",
            "UTVIDEO": "avi",
            "VP9": "webm",
            "Theora": "ogv",
            "MagicYUV": "avi",
            "Dirac": "drc",
            "FLV1": "flv",
            "HAP": "mov",
            "Cinepak": "avi",
            "MPEG4": "avi",
            "CLJR": "avi"
        }.get(algo, "")

        if not input_extension:
            print(f"Algoritmo non supportato: {algo}")
            continue

        input_path = os.path.join(compression_dir, dataset, f"{algo}_output.{input_extension}")
        print(input_path)

        output_path = os.path.join(dataset_output_dir, algo)
        os.makedirs(output_path, exist_ok=True)

        output_path = os.path.join(output_path, "Frame_%d.png")
        print(output_path)

        cmd = f"python video_decompression.py {input_path} {output_path}"
        os.system(cmd)
