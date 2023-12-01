

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
        "VP9-VSy": ".webm",
        "Theora": ".ogv",
        "MagicYUV": ".avi",
        "Dirac": ".drc",
        "Dirac-LS": ".drc",
        "FLV1": ".flv",
        "SNOW": ".avi",
        "SNOW-LS": ".avi",
        "JPEG2000": ".mp4",
        "JPEG2000-LS": ".mp4",
        "Cinepak": ".avi",
        "MPEG4": ".avi",
        "CLJR": ".avi",

    }

    return valid_extensions.get(algo)

#Inserire il dataset da utilizzare, in particolare specificare i nomi delle immagini
datasets = {
    "ArtGallery2": "./dataset/ArtGallery2/Frame_%3d.png",
    "ArtGallery2_random": "./dataset/ArtGallery2_random/Frame_%3d.png",
    "Dragons": "./dataset/Dragons/dragons-%2d.png",
    "Dragons_random": "./dataset/Dragons_random/Frame_%3d.png",
    "OpEX": "./dataset/OpEx/%d.png",
    "OpEX_random": "./dataset/OpEx_random/Frame_%3d.png",
    "Fish": "./dataset/Fish/fishi-%2d.png",
    "Fish_random": "./dataset/Fish_random/Frame_%3d.png",
    "Dice": "./dataset/Dice/dice-%2d.png",
    "Dice_random": "./dataset/Dice_random/Frame_%3d.png",
    "Messerschmitt": "./dataset/Messerschmitt/messerschmitt-%2d.png",
    "Messerschmitt_random": "./dataset/Messerschmitt_random/Frame_%3d.png",
    "Shrubbery": "./dataset/Shrubbery/shrubbery-%2d.png",
    "Shrubbery_random": "./dataset/Shrubbery_random/Frame_%3d.png"
}