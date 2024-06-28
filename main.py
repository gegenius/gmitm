from gmitm import *
import time

def elab(surceiface, packet):
    return FORWARD, packet, True

try:
    g = gmitm(elab, "eth0", "eth1")
    g.start()
    print("script avviato con successo")
    while True:
        time.sleep(10000)
except KeyboardInterrupt:
    g.stop()
    print("script stoppato con successo")
