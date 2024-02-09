import subprocess
import os

def run_ffmpeg_command(dataset, codec, output_folder, get_naming_patterns):
    
    dataset_naming_patterns = get_naming_patterns()
    input_folder = f"decompressione_test/{dataset}/{codec}/Frame_%d.png"
    dataset_folder = f"dataset/{dataset}/{dataset_naming_patterns.get(dataset, 'default_naming_pattern')}"
    stats_filename = f"{output_folder}/ssim_{dataset}_{codec}.txt"
    command = f"ffmpeg -i {input_folder} -i {dataset_folder} -lavfi ssim=stats_file={stats_filename} -f null -"
    subprocess.run(command, shell=True)

def generate_dataset_naming_patterns():
    return {
        'ArtGallery2': 'Frame_%3d.png',
        "Dragons": "dragons-%2d.png",
        #"OpEx": '%d.png',
    }

def main():
    codecs = ['HEVC-VS', 'AV1-VS', 'VP9-VS']
    output_folder = 'ssim_2022'

    os.makedirs(output_folder, exist_ok=True)

    for dataset in generate_dataset_naming_patterns().keys():
        for codec in codecs:
            run_ffmpeg_command(dataset, codec, output_folder, generate_dataset_naming_patterns)

if __name__ == "__main__":
    main()
