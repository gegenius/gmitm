import os
import shutil
import sys

if os.getuid() == 1:
    print("AVVIA QUESTO SCRIPT DA AMMINISTRATORE")
    sys.exit()

if "gmitm.py" not in os.listdir() and "main.py" not in os.listdir():
    print("impossibile trovare i file necessari per l'installazione(questo script è dentro la repo?)")
    sys.exit()

os.system("apt get install pip")
os.system("pip install scapy")

try:
    os.mkdir("/gmitm")
except:
    print("CARTELLA /gmitm GIA ESISTENTE!!!!!\nDESIDERI SOVRASCRIVERE?")
    i = input("('y' or 'n')>. ")
    if i == "y":
        os.system("rm -r /gmitm")
    else:
        sys.exit()
shutil.move("gmitm.py", "/gmitm/gmitm.py")
shutil.move("main.py", "/gmitm/main.py")

file = open("/etc/systemd/system/gmitm.service", "w")
file.write("""[Unit]
Description=iface sniff service
Before=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/gmitm
ExecStart=python /gmitm/main.py

[Install]
WantedBy=multi-user.target""")
file.close()

os.system("systemctl daemon-reload")
os.system("systemctl enable gmitm.service")

print("INSTALLAZIONE COMPLETATA")
