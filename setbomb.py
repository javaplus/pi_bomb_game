import json
import urllib2
import os

serverIP = os.environ['pi_server_ip']

def submitTime():
	data = {
 "minutes":"5",
"speaktime":[{"time":"4:57", "say":"Bomb has been planted! Bomb has been planted!", "parms" : "-s 140 -ven-us+f3"},{"time":"4", "say":"4 minutes remaining, 4 minutes." , "parms": "-s 160"},{"time":"3", "say":"3 minutes remaining, 3 minutes", "parms": "-s 160"}, {"time":"2", "say":"2 minutes remaining, 2 minutes", "parms": "-s 160t"}, {"time":"1","say":"1 minute remaining, 1 minute", "parms": "-s 160"},{"time":"0:10","say":"10, 9, 8, 7, 6, 5, 4, 3, 2, 1", "parms": "-s 110"},{"time":"0:01","say":"", "file": "/home/pi/grenade.wav"},{"time":"0:00","say":"Stop, Stop, Stop, Stop, Stop, Stop","parms": "-s 160"}],
        "speakinterval":[{"interval":"5", "say":"%min% Minutes Remaining, %min% Minutes."}]
	}
        


	req = urllib2.Request('http://' + serverIP + ':5000/timer')
	req.add_header('Content-Type', 'application/json')

	response = urllib2.urlopen(req, json.dumps(data))

