# gmitm
tool per l'esecuzione di attacchi mitm a Layer 2 su cavo ethernet
# installazione
per eseguire l'installazione sarà sufficente eseguire i seguenti comando:

$git clone https://github.com/gegenius/gmitm.git

$cd gmitm

$sudo python setup.py

ATTENZIONE
quando eseguirete il setup lo script verrà eseguito automaticamente e disabiliterà i NIC Ethernet.
di conseguenza appena avrai eseguito il setup, se necessiti di accedere al dispositivo via ssh, esegui il comando

$python gtool.py disable

SCRIPT PERSONALIZZATI
per fare un propio script è sufficente importare tutte le dipendenze dal file gmitm.py e chiamare la funzione gmitm passandogli come parametri la funzione per elaborare i pacchetti, il nome della prima interfaccai e il nome della seconda.
la funzione deve prendere come parametri il nome dell'interfaccia da dove viene il pacchetto e il pacchetto vero e propio.
IMPORTANTE: la funzione deve sempre tornare tre parametriche corrispondono all operazione(FORWARD, IGNORE, RESPOND), il pacchetto elaborato e il parametro di salvataggio(variabile booleana che indica se il pacchetto verrà salvato nel loot)
