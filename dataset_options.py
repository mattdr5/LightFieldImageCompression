# dataset_options.py
# Aumento q_v diminuisce SSIM

DATASET_OPTIONS = {
    'artgallery2': {
        'FLV1': ["-q:v", "10"],
        'MJPEG': ["-q:v", "10"],
        'ProRes': ["-q:v", "64"],
        'MPEG4': ["-q:v", "10"],
    },
    'artgallery2_random': {
        'FLV1': ["-q:v", "15"],
        'MJPEG': ["-q:v", "15"],
        'ProRes': ["-q:v", "64"],
        'MPEG4': ["-q:v", "10"],
    },
    'blob': {  #0,93
        'FLV1': ["-q:v", "15"],
        'MJPEG': ["-q:v", "20"],
        'ProRes': ["-q:v", "64"],
        'MPEG4': ["-q:v", "12"],
    },
    'blob_random': {  #0,93
        'FLV1': ["-q:v", "12"],
        'MJPEG': ["-q:v", "20"],
        'ProRes': ["-q:v", "64"],
        'MPEG4': ["-q:v", "10"],
    },
    'car': {   #0,94
        'FLV1': ["-q:v", "16"],
        'MJPEG': ["-q:v", "20"],
        'ProRes': ["-q:v", "64"],
        'MPEG4': ["-q:v", "16"],
    },
    'car_random': {   #0,94
        'FLV1': ["-q:v", "16"],
        'MJPEG': ["-q:v", "20"],
        'ProRes': ["-q:v", "64"],
        'MPEG4': ["-q:v", "13"],
    },
    'cobblestone': {    #0,90
        'FLV1': ["-q:v", "10"],
        'MJPEG': ["-q:v", "13"],
        'ProRes': ["-q:v", "36"],
        'MPEG4': ["-q:v", "10"],
    },
    'cobblestone_random': {
        'FLV1': ["-q:v", "10"],
        'MJPEG': ["-q:v", "13"],
        'ProRes': ["-q:v", "36"],
        'MPEG4': ["-q:v", "10"],
    },
    'dice': {
        'FLV1': ["-q:v", "10"],
        'MJPEG': ["-q:v", "10"],
        'ProRes': ["-q:v", "64"],
        'MPEG4': ["-q:v", "5"],
    },
    'dice_random': {
        'FLV1': ["-q:v", "10"],
        'MJPEG': ["-q:v", "10"],
        'ProRes': ["-q:v", "10"],
        'MPEG4': ["-q:v", "5"],
    },
    'dragons': {
        'FLV1': ["-q:v", "10"],
        'MJPEG': ["-q:v", "10"],
        'ProRes': ["-q:v", "10"],
        'MPEG4': ["-q:v", "5"],
    },
    'dragons_random': {
        'FLV1': ["-q:v", "10"],
        'MJPEG': ["-q:v", "10"],
        'ProRes': ["-q:v", "10"],
        'MPEG4': ["-q:v", "5"],
    },
    'fish': {
        'FLV1': ["-q:v", "10"],
        'MJPEG': ["-q:v", "10"],
        'ProRes': ["-q:v", "10"],
        'MPEG4': ["-q:v", "5"],
    },
    'fish_random': {
        'FLV1': ["-q:v", "10"],
        'MJPEG': ["-q:v", "10"],
        'ProRes': ["-q:v", "10"],
        'MPEG4': ["-q:v", "5"],
    },
    'mannequin': {
        'FLV1': ["-q:v", "10"],
        'MJPEG': ["-q:v", "10"],
        'ProRes': ["-q:v", "10"],
        'MPEG4': ["-q:v", "5"],
    },
    'mannequin_random': {
        'FLV1': ["-q:v", "10"],
        'MJPEG': ["-q:v", "10"],
        'ProRes': ["-q:v", "10"],
        'MPEG4': ["-q:v", "5"],
    },
    'messerschmitt': {
        'FLV1': ["-q:v", "5"],
        'MJPEG': ["-q:v", "10"],
        'ProRes': ["-q:v", "10"],
        'MPEG4': ["-q:v", "5"],
    },
    'messerschmitt_random': {
        'FLV1': ["-q:v", "5"],
        'MJPEG': ["-q:v", "10"],
        'ProRes': ["-q:v", "10"],
        'MPEG4': ["-q:v", "5"],
    },

    # Altri dataset con le relative opzioni
}