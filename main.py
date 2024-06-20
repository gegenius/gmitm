from gmitm import *

def elab(surceiface, packet):
    return FORWARD, packet, True

try:
    gmitm(elab, "eth0", "eth1")
    gmitm.start()
    print("script avviato con successo")
except KeyboardInterrupt:
    gmitm.stop()
    print("script stoppato con successo")
