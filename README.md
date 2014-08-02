This is just me testing a chat/file transfer app via python. Looking into making it use GnuPG

Additional python modules needed are pyzmq and gnupg.  pip install pyzmq and pip install gnupg to set them up.

To operate use the follow:

python server.py # starts the server side

python client.py # starts the client side

The following is the initial interaction with the client.py

Type gpg home dir: /home/user/.gnupg

[{'dummy': u'', 'keyid': u'598D88714AB0262C', 'expires': u'', 'subkeys': [[u'FA5DDB35296966E1', u'e']], 'length': u'2048', 'ownertrust': u'-', 'algo': u'1', 'fingerprint': u'9BB5DF4DF416D160C966CE3C598D88714AB0262C', 'date': u'1406814964', 'trust': u'-', 'type': u'pub', 'uids': [u'Patrick Pierson <*****>']}]

Type recipients key: 4AB0262C

Password: **********

Connecting to server...

Sending request  1 ...

Message: Enter your message

The typed message will get sent encrypted to server.  Server will print encrypted message to console  and reply with same encrypted message.  Client will print encrypted message, decrypt message and print decrypted message to console.

