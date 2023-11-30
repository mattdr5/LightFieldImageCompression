import os

# Definizione dei dataset e degli algoritmi
datasets = {
    "ArtGallery2": "./dataset/ArtGallery2/Frame_%3d.png"
}

#Inserire qui gli algoritmi di compressione video da analizzare

algorithms = ["FFV1", "HEVC", "HUFFYUV", "UTVIDEO", "VP9", "AV1", "HEVC-VS", "VP9-VS", "FLV1", "CLJR", "MPEG4", "MJPEG", "ProRes", "MagicYUV", "FFVHUFF", "LCL"] 
algorithms = ["FLV1"]

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
            "HEVC-VS": "mp4",
            "AV1": "mkv",
            "AV1-VS": "mkv",
            "FFV1": "avi",
            "HUFFYUV": "avi",
            "UTVIDEO": "avi",
            "VP9": "webm",
            "VP9-VS": "webm",
            "MagicYUV": "avi",
            "Dirac": "drc",
            "Dirac-LS": "drc",
            "FLV1": "flv",
            "JPEG2000": "mp4",
            "JPEG2000-LS": "mp4",
            "SNOW": "avi",
            "SNOW-LS": "avi",
            "MPEG4": "avi",
            "CLJR": "avi",
            "ProRes": "mov",
            "MJPEG": "avi",
            "FFVHUFF": "avi",
            "LCL": "avi"
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
