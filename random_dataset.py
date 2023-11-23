import os
import random
import shutil
import glob

def randomizza_e_copia_files(cartella_origine, cartella_destinazione, pattern):

   if "random" not in str(cartella_origine): 
   
    # Costruisci il percorso completo usando il modulo glob
    percorso_completo_origine = os.path.join(cartella_origine, pattern)

    # Ottieni la lista dei file che corrispondono al pattern
    lista_files = glob.glob(percorso_completo_origine)

    # Mescola la lista in modo casuale
    random.shuffle(lista_files)

    # Crea la cartella destinazione se non esiste
    if not os.path.exists(cartella_destinazione):
        os.makedirs(cartella_destinazione)

    i=0
    # Copia i file nella nuova cartella
    for file_origine  in lista_files:
        if(i < 10):
            nome_file = 'Frame_00'+str(i)+'.png'
            percorso_destinazione = os.path.join(cartella_destinazione, nome_file)
            shutil.copy(file_origine, percorso_destinazione)
        if(i >= 10 and i < 100):
            nome_file = 'Frame_0'+str(i)+'.png'
            percorso_destinazione = os.path.join(cartella_destinazione, nome_file)
            shutil.copy(file_origine, percorso_destinazione)
        if( i == 100):
            nome_file = 'Frame_'+str(i)+'.png'
            percorso_destinazione = os.path.join(cartella_destinazione, nome_file)
            shutil.copy(file_origine, percorso_destinazione)
        i+=1
        
    return lista_files
