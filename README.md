# Compressione Video per Light Field - Compressione Dati 2023/24

## Descrizione del Progetto

Questo progetto del corso di Compressione Dati 2023/24 della magistrale di Informatica presso l'Università degli Studi di Salerno, si propone di condurre una valutazione comparativa tra diversi algoritmi di compressione video. Particolare attenzione sarà dedicata alla valutazione della loro efficacia nella compressione di Light Field. 

## Obiettivo progetto
L'obiettivo principale è analizzare le prestazioni di tali algoritmi in termini di qualità della compressione, velocità di codifica/decodifica e efficienza complessiva nella gestione di dati di tipo Light Field.

## Valutazione delle Prestazioni

I risultati ottenuti includono metriche di qualità della compressione, tempi di codifica/decodifica e altri parametri rilevanti.

## Contributi e Feedback

Siete invitati a contribuire a questo progetto aprendo issue, inviando pull request o fornendo feedback sulla valutazione comparativa degli algoritmi di compressione video per Light Field. Le vostre contribuzioni sono preziose per migliorare la comprensione e l'efficacia di tali algoritmi.

## Avvio dell'Esperimento

Per avviare l'esperimento, segui i seguenti passaggi:

1. Assicurati di avere Python installato sul tuo sistema (Versione usata - 3.11.6).
2. Assicurati di avere le librerie necessarie installate eseguendo il comando seguente:
```
pip install -r requirements.txt
```
Questo comando installerà tutte le librerie elencate nel file `requirements.txt`, assicurando che il tuo ambiente sia correttamente configurato per eseguire l'esperimento.
3. Apri un terminale o prompt dei comandi nella directory del progetto.
4. Esegui il comando `python test_compression.py` per avviare la prima fase dell'esperimento (la compressione). Lo script utilizzerà gli algoritmi di compressione specificati nella lista `algorithms` nel file `utils.py`. Assicurati che questa lista includa tutti gli algoritmi utilizzati durante la fase di compressione.
5. Al termine (e unicamente al termine di questa fase) della fase di compressione, esegui il comando `python test_decompression.py` per avviare la seconda fase dell'esperimento (la decompressione).
Durante questa fase, lo script decomprimerà i video compressi utilizzando gli stessi algoritmi e dataset utilizzati nella fase di compressione. I risultati della decompressione saranno registrati e comparati con i video originali per valutare la qualità della decompressione. Per eseguire la decompressione, lo script utilizzerà gli algoritmi di compressione specificati nella lista `algorithms` nel file `utils.py`. Assicurati che questa lista includa tutti gli algoritmi utilizzati durante la fase di compressione. Dopo aver eseguito lo script, troverai i risultati della decompressione nella directory specificata dal parametro `decompression_dir`. Ogni dataset avrà una directory separata all'interno della directory di decompressione, contenente i video decompressi utilizzando gli algoritmi specificati.

## Avvio dell'Esperimento

Per avviare l'esperimento, segui i seguenti passaggi:

1. Assicurati di avere Python installato sul tuo sistema (Versione usata - 3.11.6).
2. Assicurati di avere le librerie necessarie installate eseguendo il comando seguente:
```
pip install -r requirements.txt
```
Questo comando installerà tutte le librerie elencate nel file `requirements.txt`, assicurando che il tuo ambiente sia correttamente configurato per eseguire l'esperimento.
3. Apri un terminale o prompt dei comandi nella directory del progetto.
4. Esegui il comando `python test_compression.py` per avviare la prima fase dell'esperimento (la compressione). Lo script utilizzerà gli algoritmi di compressione specificati nella lista `algorithms` nel file `utils.py`. Assicurati che questa lista includa tutti gli algoritmi utilizzati durante la fase di compressione.
5. Al termine (e unicamente al termine di questa fase) della fase di compressione, esegui il comando `python test_decompression.py` per avviare la seconda fase dell'esperimento (la decompressione).
Durante questa fase, lo script decomprimerà i video compressi utilizzando gli stessi algoritmi e dataset utilizzati nella fase di compressione. I risultati della decompressione saranno registrati e comparati con i video originali per valutare la qualità della decompressione. Per eseguire la decompressione, lo script utilizzerà gli algoritmi di compressione specificati nella lista `algorithms` nel file `utils.py`. Assicurati che questa lista includa tutti gli algoritmi utilizzati durante la fase di compressione. Dopo aver eseguito lo script, troverai i risultati della decompressione nella directory specificata dal parametro `decompression_dir`. Ogni dataset avrà una directory separata all'interno della directory di decompressione, contenente i video decompressi utilizzando gli algoritmi specificati.


## Espansione del Progetto

Se desideri espandere il progetto aggiungendo nuovi codec o dataset per la comparazione, segui questi passaggi:

### Aggiunta di Nuovi Codec

Se vuoi aggiungere nuovi codec per la comparazione, segui questi passaggi:

1. Apri il file `utils.py` all'interno del progetto.
2. Trova la funzione `get_valid_extension` e aggiungi il nuovo codec insieme alla sua estensione valida. Ad esempio:
   
   ```python
   valid_extensions = {
       ...
       "NUOVO_CODEC": ".formato",
       ...
   }
   ```
3. Assicurati di specificare correttamente il formato dell'estensione del nuovo codec.

### Aggiunta di Nuovi Dataset
Se vuoi aggiungere nuovi dataset per la comparazione, segui questi passaggi:

1. Sempre nel file utils.py, trova la definizione dei dataset e degli algoritmi.

2. Aggiungi il nuovo dataset specificando il nome e il percorso delle immagini. Ad esempio:

```python
datasets = {
    ...
    "NUOVO_DATASET": "./percorso/

```
## Formato dei nomi dei file delle immagini nei Dataset

Il formato dei nomi dei file delle immagini nei dataset può variare leggermente da un dataset all'altro. Tuttavia, ci sono alcune linee guida generali da seguire:

- **Numerazione Sequenziale**: Molti dataset utilizzano una numerazione sequenziale per le immagini. In questi casi, il nome del file dovrebbe includere un numero di sequenza univoco. Utilizza il placeholder `%3d` per formattare i numeri su tre cifre con zero padding se necessario. Ad esempio, `Frame_%3d.png` produrrà nomi file come `Frame_001.png`, `Frame_002.png`, ..., `Frame_999.png`, `Frame_1000.png`.

- **Formato Specifico**: Alcuni dataset possono utilizzare un formato specifico per i nomi dei file delle immagini. Ad esempio, `dice-%2d.png` indica che il numero di sequenza è incluso nel nome del file preceduto da un prefisso (`dice-`) e seguito da un numero a due cifre. Assicurati di seguire il formato specifico indicato per ogni dataset.

Assicurati di controllare attentamente il formato dei nomi dei file delle immagini per ciascun dataset e seguire le indicazioni fornite per garantire una corretta elaborazione da parte del programma.


## Licenza

Questo progetto è distribuito con licenza [MIT](LICENSE), che consente un uso libero e aperto dei materiali inclusi.



