import os.path, sys
from Crypto.PublicKey import RSA

if(len(sys.argv) < 3) :
  print 'Usage : python client_gencert.py filename key_size'
  sys.exit()


PATH = sys.argv[1]

if os.path.isfile(PATH):
  print PATH + " exists"
else:
  rsa_key_file = PATH
  rsa_key = RSA.generate(int(sys.argv[2]))
  rsa_file = open(rsa_key_file, 'w')
  rsa_file.write(rsa_key.exportKey())
  rsa_file.close()

