import time
import  sys
import signal
import os
import webbrowser

def happybirthday():
	print("************** Boldog Születésnapot! ***************** \n" +
    "Adj rá hangot!")
	time.sleep(3)
	webbrowser.open("http://taroldagumim.hu/juhiszulinap/happybirthday.html", new=2)
	os.kill(os.getppid(), signal.SIGHUP)

happybirthday()
