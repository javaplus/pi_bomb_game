import json
import urllib2
import os

serverIP = os.environ['pi_server_ip']

def submitTime():

	data = {
 "minutes":"0",
"speaktime":[],
        "speakinterval":[{"interval":"5", "say":"%min% Minutes Remaining, %min% Minutes."}]
	}   

	req = urllib2.Request('http://' + serverIP + ':5000/timer')
	req.add_header('Content-Type', 'application/json')

	response = urllib2.urlopen(req, json.dumps(data))

