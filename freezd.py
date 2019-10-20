import sys
import time
import subprocess
import os
import signal
wait = False
timeout = 0
srvfil = open("./antifreeze/time_" + sys.argv[1] +".txt", "r")
while (True):
	srvtime = 0
	time.sleep(1)
	srvfil.seek(0)
	try:
		srvtime=int(srvfil.readlines()[0])
	except IndexError as e:
		print(e)
		continue
	
	systime=round(time.time())
#	print ("srvtime: " + str(srvtime))
#	print ("systime: " + str(systime))
	if(srvtime >= systime-2):
		if not(timeout == 0):
			wait = False
			print("Server caught back up!")

		timeout=0
	else:
		if(wait == False):
			timeout=timeout+1
			print("Server is behind! (" + str(timeout) + ")")
			if(timeout == 120):
				PID = int(subprocess.Popen("PID= ps -x | grep -v grep | grep \"srcds_linux -game garrysmod +hostport " + sys.argv[1] +"\" | awk '{print $1}'",shell = True,stdout=subprocess.PIPE).stdout.read().strip().decode())
				print ("Server Frozen! killing process...")
				os.kill(PID, signal.SIGTERM)
				wait = True
				print ("Process Killed! waiting for server to catch back up...")
