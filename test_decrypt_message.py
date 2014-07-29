import os.path, sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode

def decrypt_RSA(public_key_loc, encrypt_message):
    key = open(public_key_loc, "r").read()
    rsakey = RSA.importKey(key)
    rsakey = PKCS1_OAEP.new(rsakey)
    decrypted = rsakey.decrypt(b64decode(encrypt_message))
    return decrypted

public_key_loc = sys.argv[1]
encrypt_message = sys.argv[2]
message = decrypt_RSA(public_key_loc, encrypt_message)
print message
