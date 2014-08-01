This is just me testing a chat/file transfer app via python. Looking into making it use GnuPG

To operate use the follow:

python client_gencert.py test.key 1024 # generates a small test key

python reqrep_server.py # starts the server side

python reqrep_client.py test.key # starts the client side

Type message to send encrypted to server.  Server will print encrypted message and reply with encrypted message.  Client will print encrypted message, decrypt message and print decrypted message.

