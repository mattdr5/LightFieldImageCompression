import sys
import VideoCompressionAV1
import VideoCompressionFFV1
import VideoCompressionHEVC
import VideoCompressionHUFFYUV
import VideoCompressionUTVideo
import VideoCompressionVP9
import VideoCompressionHEVCvls
import VideoCompressionVP9vls
import VideoCompressionAV1vls
import VideoCompressionTheora
import VideoCompressionMagicYUV
import VideoCompressionDirac
import VideoCompressionFLV1
import VideoCompressionSNOW
import VideoCompressionHAP
import pathlib
import time

algo=""
input_path=""
output_path=""
if(len(sys.argv[1:]) == 3):
    algo=sys.argv[1]
    input_path=sys.argv[2]
    output_path=sys.argv[3]
else:
    print("Specifica in sequenza: \n- ALGORITMO DI COMPRESSIONE(HEVC,HEVC-VS(Visually Lossless),AV1,AV1-VS(Visually Lossless),FFV1,HUFFYUV,UTVIDEO,VP9,VP9-VS(Visually Lossless))\n- INPUT_PATH (es. ./ArtGallery2/Frame_%3d.png)\n- OUTPUT_PATH (es. output.mp4)")
    exit()


startTime = time.time()
match algo:
    case "HEVC":
        if(pathlib.Path(output_path).suffix == ".mp4"):
            VideoCompressionHEVC.comp_HEVC(input_path,output_path)
        else:
            print("Per HEVC l'estensione del file in output deve essere .mp4")
    case "HEVC-VS":
        if(pathlib.Path(output_path).suffix == ".mp4"):
            VideoCompressionHEVCvls.comp_HEVC_visuallyLS(input_path,output_path)
        else:
            print("Per HEVC-VS l'estensione del file in output deve essere .mp4")
    case "AV1":
        if(pathlib.Path(output_path).suffix == ".mkv"):
            VideoCompressionAV1.comp_AV1(input_path,output_path)
        else:
            print("Per AV1 l'estensione del file in output deve essere .mkv")
    case "AV1-VS":
        if(pathlib.Path(output_path).suffix == ".mkv"):
            VideoCompressionAV1vls.comp_AV1_visuallyLS(input_path,output_path)
        else:
            print("Per AV1-VS l'estensione del file in output deve essere .mkv")
    case "FFV1":
        if(pathlib.Path(output_path).suffix == ".avi"):
            VideoCompressionFFV1.comp_FFV1(input_path,output_path)
        else:
            print("Per FFV1 l'estensione del file in output deve essere .avi")
    case "HUFFYUV":
        if(pathlib.Path(output_path).suffix == ".avi"):
            VideoCompressionHUFFYUV.comp_HUFFYUV(input_path,output_path)
        else:
            print("Per HUFFYUV l'estensione del file in output deve essere .avi")
    case "UTVIDEO":
        if(pathlib.Path(output_path).suffix == ".avi"):
            VideoCompressionUTVideo.comp_UTVIDEO(input_path, output_path)
        else:
            print("Per UTVIDEO l'estensione del file in output deve essere .avi")
    case "VP9":
        if(pathlib.Path(output_path).suffix == ".webm"):
            VideoCompressionVP9.comp_VP9(input_path,output_path)
        else:
            print("Per VP9 l'estensione del file in output deve essere .webm")
    case "VP9-VS":
        if(pathlib.Path(output_path).suffix == ".webm"):
            VideoCompressionVP9vls.comp_VP9_visuallyLS(input_path,output_path)
        else:
            print("Per VP9-VS l'estensione del file in output deve essere .webm")
    case "Theora":
        if(pathlib.Path(output_path).suffix == ".ogv"):
            VideoCompressionTheora.comp_Theora(input_path, output_path)
        else:
            print("Estensione di output per Theora deve essere .ogv")
    case "MagicYUV":
        if (pathlib.Path(output_path).suffix == ".avi"):
            VideoCompressionMagicYUV.comp_MagicYUV(input_path, output_path)
        else:
            print("Estensione di output per MagicYUV deve essere .avi")
    case "Dirac":
        if (pathlib.Path(output_path).suffix == ".drc"):
            VideoCompressionDirac.comp_Dirac(input_path, output_path)
        else:
            print("Estensione di output per Dirac deve essere .drc")
    case "FLV1":
        if (pathlib.Path(output_path).suffix == ".flv"):
            VideoCompressionFLV1.comp_FLV1(input_path, output_path)
        else:
            print("Estensione di output per FLV1 deve essere .flv")
    case "SNOW":
        if (pathlib.Path(output_path).suffix == ".avi"):
            VideoCompressionSNOW.comp_Snow(input_path, output_path)
        else:
            print("Estensione di output per SNOW deve essere .avi")
    case "HAP":
        if (pathlib.Path(output_path).suffix == ".mov"):
            VideoCompressionHAP.comp_Hap(input_path, output_path)
        else:
            print("Estensione di output per HAP deve essere .mov")



print("Tempo impiegato: " + str(time.time() - startTime) + " secondi")