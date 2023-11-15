import os
import random
import shutil
import glob

def randomizza_e_copia_files(cartella_origine, cartella_destinazione, pattern):
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
            nome_file = 'Frame_00'+str(i)+'.jpg'
            percorso_destinazione = os.path.join(cartella_destinazione, nome_file)
            shutil.copy(file_origine, percorso_destinazione)
        if(i >= 10 and i < 100):
            nome_file = 'Frame_0'+str(i)+'.jpg'
            percorso_destinazione = os.path.join(cartella_destinazione, nome_file)
            shutil.copy(file_origine, percorso_destinazione)
        if( i == 100):
            nome_file = 'Frame_'+str(i)+'.jpg'
            percorso_destinazione = os.path.join(cartella_destinazione, nome_file)
            shutil.copy(file_origine, percorso_destinazione)
        i+=1
        

    return lista_files

# Specifica il percorso della tua cartella origine, cartella destinazione e il pattern dei file
cartella_origine = './dataset/ArtGallery2'
cartella_destinazione = './dataset/ArtGallery2_random'
pattern = 'Frame_*.png'

# Ottieni la lista randomizzata dei file e copiali nella nuova cartella
lista_randomizzata = randomizza_e_copia_files(cartella_origine, cartella_destinazione, pattern)

# Stampa la lista randomizzata
print("Lista randomizzata dei file copiati nella nuova cartella:")
for file in lista_randomizzata:
    print(file)
