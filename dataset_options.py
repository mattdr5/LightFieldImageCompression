# dataset_options.py
# Aumento q_v diminuisce SSIM

DATASET_OPTIONS = {
    'artgallery2': {      #0.93
       'FLV1': ["-q:v", "13"],
       'MJPEG': ["-q:v", "16"],
       'ProRes': ["-q:v", "62"],
       'MPEG4': ["-q:v", "12"],
    },
    'artgallery2_random': {      #0.93
        'FLV1': ["-q:v", "13"],
        'MJPEG': ["-q:v", "16"],
        'ProRes': ["-q:v", "62"],
        'MPEG4': ["-q:v", "12"],
    },
    'blob': {        #0,93     
        'FLV1': ["-q:v", "14"],
        'MJPEG': ["-q:v", "21"],
        'ProRes': ["-q:v", "64"],
        'MPEG4': ["-q:v", "12"],
    },
    'blob_random': {         #0,93
        'FLV1': ["-q:v", "11"],
        'MJPEG': ["-q:v", "21"],
        'ProRes': ["-q:v", "64"],
        'MPEG4': ["-q:v", "10"],
    },
    'car': {         #0,94
        'FLV1': ["-q:v", "16"],
        'MJPEG': ["-q:v", "20"],
        'ProRes': ["-q:v", "64"],
        'MPEG4': ["-q:v", "14"],
    },
    'car_random': {       #0,94
        'FLV1': ["-q:v", "16"],
        'MJPEG': ["-q:v", "20"],
        'ProRes': ["-q:v", "64"],
        'MPEG4': ["-q:v", "14"],
    },
    'cobblestone': {       #0,90      
        'FLV1': ["-q:v", "10"],
        'MJPEG': ["-q:v", "13"],
        'ProRes': ["-q:v", "36"],
        'MPEG4': ["-q:v", "10"],
    },
    'cobblestone_random': {        #0,90      
       'FLV1': ["-q:v", "10"],
        'MJPEG': ["-q:v", "13"],
        'ProRes': ["-q:v", "36"],
        'MPEG4': ["-q:v", "10"],
    },
    'dice': {         #0,95
        'FLV1': ["-q:v", "13"],
        'MJPEG': ["-q:v", "17"],
        'ProRes': ["-q:v", "64"],
        'MPEG4': ["-q:v", "12"],
    },
    'dice_random': {         #0,95
        'FLV1': ["-q:v", "13"],
        'MJPEG': ["-q:v", "17"],
        'ProRes': ["-q:v", "64"],
        'MPEG4': ["-q:v", "12"],
    },
    'dragons': {          #0.90
        'FLV1': ["-q:v", "13"],
        'MJPEG': ["-q:v", "19"],
        'ProRes': ["-q:v", "56"],
        'MPEG4': ["-q:v", "13"],
    },
    'dragons_random': {         #0.90
        'FLV1': ["-q:v", "13"],
        'MJPEG': ["-q:v", "19"],
        'ProRes': ["-q:v", "56"],
        'MPEG4': ["-q:v", "13"],
    },
    'fish': {          #0.95 
        'FLV1': ["-q:v", "16"],
        'MJPEG': ["-q:v", "23"],
        'ProRes': ["-q:v", "64"],
        'MPEG4': ["-q:v", "16"],
    },
    'fish_random': {         #0.95
        'FLV1': ["-q:v", "16"],
        'MJPEG': ["-q:v", "23"],
        'ProRes': ["-q:v", "64"],
        'MPEG4': ["-q:v", "16"],
    },
    'mannequin': {          #0.90
        'FLV1': ["-q:v", "13"],
        'MJPEG': ["-q:v", "18"],
        'ProRes': ["-q:v", "56"],
        'MPEG4': ["-q:v", "13"],
    },
    'mannequin_random': {    #0.90
        'FLV1': ["-q:v", "12"],
        'MJPEG': ["-q:v", "18"],
        'ProRes': ["-q:v", "56"],
        'MPEG4': ["-q:v", "11"],
    },
    'messerschmitt': {         #0.90            
        'FLV1': ["-q:v", "7"],
        'MJPEG': ["-q:v", "11"],
        'ProRes': ["-q:v", "34"],
        'MPEG4': ["-q:v", "7"],
    },
    'messerschmitt_random': {        #0.90           
        'FLV1': ["-q:v", "7"],
        'MJPEG': ["-q:v", "11"],
        'ProRes': ["-q:v", "34"],
        'MPEG4': ["-q:v", "7"],
    },
    'opex': {         #0.98
        'FLV1': ["-q:v", "10"],
        'MJPEG': ["-q:v", "12"],
        'ProRes': ["-q:v", "64"],
        'MPEG4': ["-q:v", "8"],
    },
    'opex_random': {         #0.98
        'FLV1': ["-q:v", "10"],
        'MJPEG': ["-q:v", "12"],
        'ProRes': ["-q:v", "64"],
        'MPEG4': ["-q:v", "8"],
    },
    #'cobblestone': {          # VERSIONE SSIM 0,85    
    #    'FLV1': ["-q:v", "16"],
    #    'MJPEG': ["-q:v", "21"],
    #    'ProRes': ["-q:v", "64"],
    #    'MPEG4': ["-q:v", "16"],
    #},
    #'cobblestone_random': {      # VERSIONE SSIM 0,85
    #    'FLV1': ["-q:v", "15"],
    #    'MJPEG': ["-q:v", "21"],
    #    'ProRes': ["-q:v", "64"],
    #    'MPEG4': ["-q:v", "14"],
    #},
    #'cobblestone': {          # VERSIONE SSIM 0,95   
    #    'FLV1': ["-q:v", "6"],
    #    'MJPEG': ["-q:v", "7"],
    #    'ProRes': ["-q:v", "17"],
    #    'MPEG4': ["-q:v", "6"],
    #},
    #'cobblestone_random': {         # VERSIONE SSIM 0,95 
    #    'FLV1': ["-q:v", "5"],
    #    'MJPEG': ["-q:v", "7"],
    #    'ProRes': ["-q:v", "17"],
    #    'MPEG4': ["-q:v", "5"],
    #},
    #'messerschmitt': {          # VERSIONE SSIM 0,85
    #    'FLV1': ["-q:v", "14"],
    #    'MJPEG': ["-q:v", "23"],
    #    'ProRes': ["-q:v", "64"],
    #    'MPEG4': ["-q:v", "13"],
    #},
    #'messerschmitt_random': {          # VERSIONE SSIM 0,85
    #    'FLV1': ["-q:v", "13"],
    #    'MJPEG': ["-q:v", "23"],
    #    'ProRes': ["-q:v", "64"],
    #    'MPEG4': ["-q:v", "12"],
    #},
    #'messerschmitt': {          # VERSIONE SSIM 0,95 
    #    'FLV1': ["-q:v", "3"],
    #    'MJPEG': ["-q:v", "5"],
    #    'ProRes': ["-q:v", "14"],
    #    'MPEG4': ["-q:v", "3"],
    #},
    #'messerschmitt_random': {          # VERSIONE SSIM 0,95 
    #    'FLV1': ["-q:v", "3"],
    #    'MJPEG': ["-q:v", "5"],
    #    'ProRes': ["-q:v", "14"],
    #    'MPEG4': ["-q:v", "3"],
    #},
    #'dragons': {       #VERSIONE SSIM 0,85
    #    'FLV1': ["-q:v", "25"],
    #    'MJPEG': ["-q:v", "33"],
    #    'MPEG4': ["-q:v", "24"],
    #},
    #'dragons': {       #VERSIONE SSIM 0,95
    #    'FLV1': ["-q:v", "5"],
    #    'MJPEG': ["-q:v", "7"],
    #    'MPEG4': ["-q:v", "5"],
    #},
    #'dragons_random': {       #VERSIONE SSIM 0,85
    #    'FLV1': ["-q:v", "25"],
    #    'MJPEG': ["-q:v", "33"],
    #    'MPEG4': ["-q:v", "24"],
    #},
    #'dragons_random': {       #VERSIONE SSIM 0,95
    #    'FLV1': ["-q:v", "5"],
    #    'MJPEG': ["-q:v", "7"],
    #    'MPEG4': ["-q:v", "5"],
    #},
    #'mannequin': {          #VERSIONE SSIM 0,85
    #    'FLV1': ["-q:v", "22"],
    #    'MJPEG': ["-q:v", "33"],
    #    'MPEG4': ["-q:v", "21"],
    #},
    #'mannequin': {          #VERSIONE SSIM 0,95
    #    'FLV1': ["-q:v", "6"],
    #    'MJPEG': ["-q:v", "8"],
    #    'MPEG4': ["-q:v", "6"],
    #},
    #'mannequin_random': {          #VERSIONE SSIM 0,85
    #    'FLV1': ["-q:v", "20"],
    #    'MJPEG': ["-q:v", "33"],
    #    'MPEG4': ["-q:v", "19"],
    #},
    #'mannequin_random': {          #VERSIONE SSIM 0,95
    #    'FLV1': ["-q:v", "5"],
    #    'MJPEG': ["-q:v", "8"],
    #    'MPEG4': ["-q:v", "5"],
    #},
    #'artgallery2': {      #VERSIONE SSIM 0,90
    #   'FLV1': ["-q:v", "30"],
    #   'MJPEG': ["-q:v", "32"],
    #   'MPEG4': ["-q:v", "26"],
    #},
    #'artgallery2': {      #VERSIONE SSIM 0,95
    #   'FLV1': ["-q:v", "5"],
    #   'MJPEG': ["-q:v", "7"],
    #   'MPEG4': ["-q:v", "5"],
    #},
    #'artgallery2_random': {      #VERSIONE SSIM 0,90
    #    'FLV1': ["-q:v", "30"],
    #    'MJPEG': ["-q:v", "32"],
    #    'MPEG4': ["-q:v", "26"],
    #},
    #'artgallery2_random': {      #VERSIONE SSIM 0,95
    #   'FLV1': ["-q:v", "5"],
    #   'MJPEG': ["-q:v", "7"],
    #   'MPEG4': ["-q:v", "5"],
    #},
    #'blob': {      #VERSIONE SSIM 0,90
    #   'FLV1': ["-q:v", "23"],
    #   'MJPEG': ["-q:v", "32"],
    #   'MPEG4': ["-q:v", "22"],
    #},
    #'blob': {      #VERSIONE SSIM 0,95
    #   'FLV1': ["-q:v", "9"],
    #   'MJPEG': ["-q:v", "13"],
    #   'MPEG4': ["-q:v", "8"],
    #},
    #'blob_random': {      #VERSIONE SSIM 0,90
    #   'FLV1': ["-q:v", "19"],
    #   'MJPEG': ["-q:v", "32"],
    #   'MPEG4': ["-q:v", "15"],
    #},
    #'blob_random': {      #VERSIONE SSIM 0,95
    #   'FLV1': ["-q:v", "7"],
    #   'MJPEG': ["-q:v", "12"],
    #   'MPEG4': ["-q:v", "6"],
    #}



}