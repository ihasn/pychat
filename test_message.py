import os.path, sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode

public_key_loc = sys.argv[1]
message = sys.argv[2]

def decrypt_RSA(public_key_loc, encrypt_message):
    key = open(public_key_loc, "r").read()
    rsakey = RSA.importKey(key)
    rsakey = PKCS1_OAEP.new(rsakey)
    decrypted = rsakey.decrypt(b64decode(encrypt_message))
    return decrypted

def encrypt_RSA(public_key_loc, message):
    '''
    param: public_key_loc Path to public key
    param: message String to be encrypted
    return base64 encoded encrypted string
    '''
    key = open(public_key_loc, "r").read()
    rsakey = RSA.importKey(key)
    rsakey = PKCS1_OAEP.new(rsakey)
    encrypted = rsakey.encrypt(message)
    return encrypted.encode('base64')


encrypt_message = encrypt_RSA(public_key_loc, message)
print 'Encrypted: ' + encrypt_message

message = decrypt_RSA(public_key_loc, encrypt_message)
print 'Un-encrypted: ' + message

