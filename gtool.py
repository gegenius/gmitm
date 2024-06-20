import os
import sys
import shutil

if sys.argv[1] == "help" and len(sys.argv) == 2:
    print("""help - stampa questo banner informativo
setscript [scriptpath] - imposta uno script main per l'esecuzione
enable - abilita l'esecuzione automatica
disable - disabilita l'esecuzione automatica
""")

elif sys.argv[1] == "enable" and len(sys.argv) == 2:
    os.system("systemctl enable gmitm.service")
    print("gmitm abilitato")

elif sys.argv[1] == "disable" and len(sys.argv) == 2:
    os.system("systemctl disable gmitm.service")
    print("gmitm disabilitato")

elif sys.argv[1] == "setscript" and len(sys.argv) == 3:
    try:
        shutil.copy(sys.argv[2], "/gmitm/main.py")
    except:
        print("impossibile trovare il file")
    else:
        print("script importato con successo")

else:
    print("sintassi errata. per visualizzare le opzioni 'python gtool.py help'")