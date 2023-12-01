import os
import pathlib
import csv

# Importa tutte le funzioni specifiche di compressione video
from codec.VideoCompressionHEVC import comp_HEVC
from codec.VideoCompressionHEVCvls import comp_HEVC_visuallyLS
from codec.VideoCompressionAV1 import comp_AV1
from codec.VideoCompressionAV1vls import comp_AV1_visuallyLS
from codec.VideoCompressionFFV1 import comp_FFV1
from codec.VideoCompressionHUFFYUV import comp_HUFFYUV
from codec.VideoCompressionUTVideo import comp_UTVIDEO
from codec.VideoCompressionVP9 import comp_VP9
from codec.VideoCompressionVP9vls import comp_VP9_visuallyLS
from codec.VideoCompressionMagicYUV import comp_MagicYUV
from codec.VideoCompressionDirac import comp_Dirac, comp_Dirac_Lossless
from codec.VideoCompressionFLV1 import comp_FLV1
from codec.VideoCompressionSNOW import comp_Snow, comp_Snow_Lossless
from codec.VideoCompressionJPEG2000 import comp_jpeg2000, comp_JPEG2000_Lossless
from codec.VideoCompressionMPEG4 import comp_MPEG4
from codec.VideoCompressionCirrusLogic import comp_cljr
from codec.VideoCompressionProres import comp_ProRes
from codec.VideoCompressionMJPEG import comp_MJPEG
from codec.VideoCompressionFFVHUFF import comp_FFVHUFF
from codec.VideoCompressionLCL import comp_LCL
from utils import datasets, get_valid_extension, compression_dir


def salva_risultati_compressione_csv(risultati, file_csv):
    """
    Scrive i risultati della compressione video in un file CSV.

    Parameters:
    - risultati (dict): Dizionario contenente i risultati della compressione video.
    - file_csv (str): Il percorso del file CSV in cui scrivere i risultati.

    Raises:
    - Exception: Lanciato se si verifica un errore durante la scrittura del file CSV.
    """
    try:
        with open(file_csv, 'w', newline='') as csvfile:
            # Definisci i nomi delle colonne
            fieldnames = ['Dataset', 'Algoritmo', 'Rapporto compressione', 'Tempo compressione', 'Dimensione iniziale', 'Dimensione finale']

            # Crea un writer CSV
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Scrivi l'intestazione
            writer.writeheader()

            for risultato in risultati:
                writer.writerow(risultato)

        print(f"I risultati sono stati scritti nel file CSV: {file_csv}")

    except Exception as e:
        raise Exception(f"Errore durante la scrittura del file CSV: {str(e)}")

#Inserire qui gli algoritmi di compressione video da analizzare
#algorithms = ["AV1", "FFV1", "HEVC", "HUFFYUV", "UTVIDEO", "VP9"]
algorithms = ["FLV1", "CLJR", "MPEG4", "MJPEG", "ProRes", "MagicYUV", "FFVHUFF", "LCL"] 

def run_video_compression(algo, input_path, output_extension, output_path):
    if output_extension is None:
        print(f"Algoritmo non supportato: {algo}")
        return

    # Modifica il blocco switch per gestire la compressione direttamente
    if algo == "HEVC":
        if pathlib.Path(output_path).suffix == ".mp4":
            return comp_HEVC(input_path, output_path)
        else:
            print("Per HEVC l'estensione del file in output deve essere .mp4")
    elif algo == "HEVC-VS":
        if pathlib.Path(output_path).suffix == ".mp4":
            return comp_HEVC_visuallyLS(input_path, output_path)
        else:
            print("Per HEVC-VS l'estensione del file in output deve essere .mp4")
    elif algo == "AV1":
        if pathlib.Path(output_path).suffix == ".mkv":
            return comp_AV1(input_path, output_path)
        else:
            print("Per AV1 l'estensione del file in output deve essere .mkv")
    elif algo == "AV1-VS":
        if pathlib.Path(output_path).suffix == ".mkv":
            return comp_AV1_visuallyLS(input_path, output_path)
        else:
            print("Per AV1-VS l'estensione del file in output deve essere .mkv")
    elif algo == "FFV1":
        if pathlib.Path(output_path).suffix == ".avi":
            return comp_FFV1(input_path, output_path)
        else:
            print("Per FFV1 l'estensione del file in output deve essere .avi")
    elif algo == "HUFFYUV":
        if pathlib.Path(output_path).suffix == ".avi":
            return comp_HUFFYUV(input_path, output_path)
        else:
            print("Per HUFFYUV l'estensione del file in output deve essere .avi")
    elif algo == "UTVIDEO":
        if pathlib.Path(output_path).suffix == ".avi":
            return comp_UTVIDEO(input_path, output_path)
        else:
            print("Per UTVIDEO l'estensione del file in output deve essere .avi")
    elif algo == "VP9":
        if pathlib.Path(output_path).suffix == ".webm":
            return comp_VP9(input_path, output_path)
        else:
            print("Per VP9 l'estensione del file in output deve essere .webm")
    elif algo == "VP9-VS":
        if pathlib.Path(output_path).suffix == ".webm":
            return comp_VP9_visuallyLS(input_path, output_path)
        else:
            print("Per VP9-VS l'estensione del file in output deve essere .webm")
    elif algo == "MagicYUV":
        if pathlib.Path(output_path).suffix == ".avi":
           return comp_MagicYUV(input_path, output_path)
        else:
            print("Estensione di output per MagicYUV deve essere .avi")
    elif algo == "FLV1":
        if pathlib.Path(output_path).suffix == ".flv":
           return comp_FLV1(input_path, output_path)
        else:
            print("Estensione di output per FLV1 deve essere .flv")
    elif algo == "JPEG2000":
        if pathlib.Path(output_path).suffix == ".mp4":
            return comp_jpeg2000(input_path, output_path)
        else:
            print("Estensione di output per JPEG2000 deve essere .mp4")
    elif algo == "JPEG2000-LS":
        if pathlib.Path(output_path).suffix == ".mp4":
            return comp_JPEG2000_Lossless(input_path, output_path)
        else:
            print("Estensione di output per JEPG2000-LS deve essere .mp4")
    elif algo == "MPEG4":
        if pathlib.Path(output_path).suffix == ".avi":
            return comp_MPEG4(input_path, output_path)
        else:
            print("Estensione di output per MPEG4 deve essere .avi")
    elif algo == "CLJR":
        if pathlib.Path(output_path).suffix == ".avi":
            return comp_cljr(input_path, output_path)
        else:
            print("Estensione di output per CLJR deve essere .avi")
    elif algo == "ProRes":
        if pathlib.Path(output_path).suffix == ".mov":
            return comp_ProRes(input_path, output_path)
        else:
            print("Estensione di output per ProRes deve essere .mov")
    elif algo == "MJPEG":
        if pathlib.Path(output_path).suffix == ".avi":
            return comp_MJPEG(input_path, output_path)
        else:
            print("Estensione di output per MJPEG deve essere .avi")
    elif algo == "FFVHUFF":
        if pathlib.Path(output_path).suffix == ".avi":
            return comp_FFVHUFF(input_path, output_path)
        else:
            print("Per FFVHUFF l'estensione del file in output deve essere .avi")
    elif algo == "LCL":
        if pathlib.Path(output_path).suffix == ".avi":
            return comp_LCL(input_path, output_path)
        else:
            print("Per LCL l'estensione del file in output deve essere .avi")
    else:
        print(f"Algoritmo non riconosciuto: {algo}")


def main():
    algorithms = ["FLV1", "CLJR", "MPEG4", "MJPEG", "ProRes", "MagicYUV", "FFVHUFF", "LCL"]

    output_dir = compression_dir
    print(output_dir)

    risultati = []

    for dataset, input_path in datasets.items():
        dataset_output_dir = os.path.join(output_dir, dataset)
        os.makedirs(dataset_output_dir, exist_ok=True)

        for algo in algorithms:
            output_extension = get_valid_extension(algo)
            output_path = os.path.join(dataset_output_dir, f"{algo}_output{output_extension}")

            dimensione_iniziale, dimensione_finale, rapporto_compressione, tempo_compressione = run_video_compression(algo, input_path, output_extension, output_path)

            print(f"Rapporto compressione {algo} su dataset {dataset}: {rapporto_compressione}")
            print(f"Tempo impiegato da {algo} per la compressione sul dataset {dataset}: {tempo_compressione} secondi")

            risultati.append({
                "Dataset": dataset,
                "Algoritmo": algo,
                "Rapporto compressione": rapporto_compressione,
                "Tempo compressione": tempo_compressione,
                "Dimensione iniziale": dimensione_iniziale,
                "Dimensione finale": dimensione_finale
            })

    salva_risultati_compressione_csv(risultati=risultati, file_csv="risultati_compressione.csv")

if __name__ == "__main__":
    main()