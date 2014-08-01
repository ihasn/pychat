import zmq
import os.path, sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode

def encrypt_RSA(public_key_loc, message):
    key = open(public_key_loc, "r").read()
    rsakey = RSA.importKey(key)
    rsakey = PKCS1_OAEP.new(rsakey)
    encrypted = rsakey.encrypt(message)
    return encrypted.encode('base64')

def decrypt_RSA(public_key_loc, encrypt_message):
    key = open(public_key_loc, "r").read()
    rsakey = RSA.importKey(key)
    rsakey = PKCS1_OAEP.new(rsakey)
    decrypted = rsakey.decrypt(b64decode(encrypt_message))
    return decrypted

public_key_loc = sys.argv[1]

port = "5556"

context = zmq.Context()
print "Connecting to server..."
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)

#  Do 10 requests, waiting each time for a response
for request in range (1,10):
    print "Sending request ", request,"..."
    message = raw_input("Message: ")
    encrypt_message = encrypt_RSA(public_key_loc, message)
    socket.send (encrypt_message)
    #  Get the reply.
    encrypt_message_return = socket.recv()
    print "Received reply ", request, "[", encrypt_message_return, "]"
    decrypted_message = decrypt_RSA(public_key_loc, encrypt_message_return)
    print "Decrypted message: ", decrypted_message
