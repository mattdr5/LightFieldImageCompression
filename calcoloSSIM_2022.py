import subprocess
import os

def run_ffmpeg_command(dataset, codec, output_folder):
    input_folder = f"decompressione_test/{dataset}/{codec}/Frame_%d.png"
    
    if dataset == 'ArtGallery2':
        dataset_folder = f"dataset/{dataset}/Frame_%3d.png"
    elif dataset == 'Dragons':
        dataset_folder = f"dataset/{dataset}/dragons-%2d.png"
    elif dataset == 'OpEx':
        dataset_folder = f"dataset/{dataset}/%d.png"

    stats_filename = f"{output_folder}/ssim_{dataset}_{codec}.txt"
    command = f"ffmpeg -i {input_folder} -i {dataset_folder} -lavfi ssim=stats_file={stats_filename} -f null -"
    subprocess.run(command, shell=True)

def main():
    datasets = ['OpEx', 'ArtGallery2', 'Dragons']
    codecs = ['CLJR', 'FLV1', 'MJPEG', 'MPEG4', 'ProRes', 'HEVC-VS', 'AV1-VS', 'VP9-VS']
    output_folder = 'ssim_2022'

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    for dataset in datasets:
        for codec in codecs:
            run_ffmpeg_command(dataset, codec, output_folder)

if __name__ == "__main__":
    main()
