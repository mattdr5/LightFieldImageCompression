import os
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


algorithms = ["FLV1"]

# Cartella di output per la decompressione
decompression_dir = "./decompression_test"
# Cartella di output
compression_dir = "./compressione_test"
os.makedirs(decompression_dir, exist_ok=True)

for dataset, input_format in datasets.items():
    dataset_output_dir = os.path.join(decompression_dir, dataset)
    os.makedirs(dataset_output_dir, exist_ok=True)
    output_path = ""
    for algo in algorithms:
        if algo in ["HEVC", "HEVC-VS"]:
            input_extension = "mp4"
        elif algo in ["AV1", "AV1-VS"]:
            input_extension = "mkv"
        elif algo in ["FFV1", "HUFFYUV", "UTVIDEO"]:
            input_extension = "avi"
        elif algo in ["VP9", "VP9-VS"]:
            input_extension = "webm"
        elif algo in ["Theora"]:
            input_extension = "ogv"
        elif algo in ["MagicYUV"]:
            input_extension = "avi"
        elif algo in ["Dirac"]:
            input_extension = "drc"
        elif algo in ["FLV1"]:
            input_extension = "flv"
        elif algo in ["SNOW"]:
            input_extension = "avi"
        elif algo in ["HAP"]:
            input_extension = "mov"
        else:
            input_extension = ""  # Estensione predefinita


        input_path = os.path.join(compression_dir, f"{dataset}/{algo}_output.{input_extension}")
        print(input_path)


        output_path = os.path.join(dataset_output_dir, f"./{algo}")
        os.makedirs(output_path, exist_ok=True)

        output_path = os.path.join(output_path, "Frame_%d.png")
        print(output_path)
        cmd = f"python video_decompression.py {input_path} {output_path}"
        os.system(cmd)
