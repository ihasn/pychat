import zmq, os.path, sys, gnupg, getpass

homedir_loc = raw_input('Type gpg home dir: ')
gpg = gnupg.GPG(binary='/usr/bin/gpg2', homedir=homedir_loc)

print gpg.list_keys()

recip = raw_input('Type recipients key: ')
password = getpass.getpass()

port = "5556"

context = zmq.Context()
print "Connecting to server..."
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)

#  Do 10 requests, waiting each time for a response
for request in range (1,10):
    print "Sending request ", request,"..."
    message = raw_input("Message: ")
    encrypt_message = str(gpg.encrypt(message, recip))
    socket.send (encrypt_message)
    #  Get the reply.
    encrypt_message_return = socket.recv()
    print "Received reply ", request, "[", encrypt_message_return, "]"
    decrypted_message = str(gpg.decrypt(str(encrypt_message_return), passphrase=password))
    print "Decrypted message: ", decrypted_message
