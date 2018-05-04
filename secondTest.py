import time
import  sys
import signal
import os

def heee():
    print("Há ez üres")

def ya():
	print("Hát akkor a kúrva anyádat")
	while True:
		print("HA-HA")
		print("Bye-bye!")
		time.sleep(2)
		os.kill(os.getppid(), signal.SIGHUP)

heee()
ya()
