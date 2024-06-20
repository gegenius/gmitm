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
