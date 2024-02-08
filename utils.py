#File che contiene tutti i codec e i dataset disponibili per la comparazione
#
#Per inserire nuovi codec e dataset basta inserirli qui di seguito
#

def get_valid_extension(algo):
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
        "MagicYUV": ".avi",
        "FLV1": ".flv",
        "MPEG4": ".avi",
        "CLJR": ".avi",
        "ProRes": ".mov",
        "MJPEG": ".avi",
        "FFVHUFF": ".avi",
        "LCL": ".avi"
    }

    return valid_extensions.get(algo, "")

#Inserire il dataset da utilizzare, in particolare specificare i nomi delle immagini
# Definizione dei dataset e degli algoritmi
datasets = {
    "ArtGallery2": "./dataset/ArtGallery2/Frame_%3d.png",
    "ArtGallery2_random": "./dataset/ArtGallery2_random/Frame_%3d.png",
    "Blob": "./dataset/Blob/Frame_%3d.png",
    "Blob_random": "./dataset/Blob_random/Frame_%3d.png",
    "Car": "./dataset/Car/Frame_%3d.png",
    "Car_random": "./dataset/Car_random/Frame_%3d.png",
    "Cobblestone": "./dataset/Cobblestone/Frame_%3d.png",
    "Cobblestone_random": "./dataset/Cobblestone_random/Frame_%3d.png",
    "Dice": "./dataset/Dice/dice-%2d.png",
    "Dice_random": "./dataset/Dice_random/Frame_%3d.png",
    "Dragons": "./dataset/Dragons/dragons-%2d.png",
    "Dragons_random": "./dataset/Dragons_random/Frame_%3d.png",
    "Fish": "./dataset/Fish/fishi-%2d.png",
    "Fish_random": "./dataset/Fish_random/Frame_%3d.png",
    "Mannequin": "./dataset/Mannequin/Frame_%3d.png",
    "Mannequin_random": "./dataset/Mannequin_random/Frame_%3d.png",
    "Messerschmitt": "./dataset/Messerschmitt/messerschmitt-%2d.png",
    "Messerschmitt_random": "./dataset/Messerschmitt_random/Frame_%3d.png",
    "OpEx": "./dataset/OpEx/%d.png",
    "OpEx_random": "./dataset/OpEx_random/Frame_%3d.png"
}

decompression_dir = "./decompressione_test"
compression_dir = "./compressione_test"
algorithms = ["HEVC", "HEVC-VS", "AV1", "AV1-VS", "FFV1", "HUFFYUV", "UTVIDEO", "VP9", "VP9-VS", "MagicYUV", "FLV1", "MPEG4", "CLJR", "ProRes", "MJPEG", "FFVHUFF", "LCL"]
