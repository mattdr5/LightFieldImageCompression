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
        'ArtGallery2_random': 'Frame_%3d.png',
        'Blob': 'Frame_%3d.png',
        'Blob_random': 'Frame_%3d.png',
        'Car': 'Frame_%3d.png',
        'Car_random': 'Frame_%3d.png',
        'Cobblestone': 'Frame_%3d.png',
        'Cobblestone_random': 'Frame_%3d.png',
        'Dice': 'dice-%2d.png',
        'Dice_random': 'Frame_%3d.png',
        "Dragons": "dragons-%2d.png",
        "Dragons_random": 'Frame_%3d.png',
        "Fish": 'fishi-%2d.png',
        "Fish_random": 'Frame_%3d.png',
        "Mannequin": 'Frame_%3d.png',
        "Mannequin_random": 'Frame_%3d.png',
        "Messerschmitt": 'messerschmitt-%2d.png',
        "Messerschmitt_random": 'Frame_%3d.png',
        #"OpEx": '%d.png',
        #"OpEx_random": 'Frame_%3d.png',
    }

def main():
    codecs = ['CLJR', 'FLV1', 'MJPEG', 'MPEG4', 'ProRes']
    output_folder = 'ssim_2023'

    os.makedirs(output_folder, exist_ok=True)

    for dataset in generate_dataset_naming_patterns().keys():
        for codec in codecs:
            run_ffmpeg_command(dataset, codec, output_folder, generate_dataset_naming_patterns)

if __name__ == "__main__":
    main()
