#!/usr/bin/env python3

import secure_smtpd
import json
import urllib2
from secure_smtpd import SMTPServer, LOG_NAME, FakeCredentialValidator

class SMTPServer(SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, message_data):
	if (mailfrom.startswith("christophe.safra@hotmail.com") and rcpttos[0]=="sonnette@ollioules.hopto.org"):
        	data = {}
        	data['peer'] = peer
        	data['mailfrom'] = mailfrom
        	data['rcpttos'] = rcpttos
        	data['bell'] = 'on'
        	json_data = json.dumps(data)
        	#print (json_data)
                request = urllib2.Request("http://192.168.1.32:5665/json.htm?type=command&param=switchlight&idx=228&switchcmd=On&level=0")
                response = urllib2.urlopen(request)
	else:
		print "Do nothing"

fake_val = FakeCredentialValidator()

server = SMTPServer(
    ('0.0.0.0', 1125),
    None,
    require_authentication=True,
    credential_validator=fake_val,
    ssl=False
)

#print('server run')
server.run()
