import os.path, sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


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

public_key_loc = sys.argv[1]
message = sys.argv[2]
encrypt_message = encrypt_RSA(public_key_loc, message)
print encrypt_message
