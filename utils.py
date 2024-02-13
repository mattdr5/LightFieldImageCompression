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
    "Cobblestone": "./dataset/Cobblestone/Frame_%3d.png",
}

decompression_dir = "./decompressione_test"
compression_dir = "./compressione_test"
algorithms = ["FLV1", "MJPEG", "ProRes", "MPEG4"]
