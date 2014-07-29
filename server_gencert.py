from OpenSSL import crypto, SSL
from socket import gethostname
from pprint import pprint
from time import gmtime, mktime
 
CERT_FILE = "server.crt"
KEY_FILE = "server.key"
 
def create_self_signed_cert():
             
        # create a key pair
        k = crypto.PKey()
        try:
    	    key_size=int(raw_input('Input key size (4096 prefered):'))
        except ValueError:
            print "Not a number"
        k.generate_key(crypto.TYPE_RSA, key_size)
 
        # create a self-signed cert
        cert = crypto.X509()
        country = str(raw_input('Input Country Code (US default):'))
        cert.get_subject().C = country
        state = str(raw_input('Input State:'))
        cert.get_subject().ST = state
        city = str(raw_input('Inpute City:'))
        cert.get_subject().L = city
        cert.get_subject().O = "Dummy Company Ltd"
        cert.get_subject().OU = "Dummy Company Ltd"
        cert.get_subject().CN = gethostname()
        key_serial_number = int(raw_input('Input key serial number:'))
        cert.set_serial_number(key_serial_number)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(10*365*24*60*60)
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(k, 'sha1')
 
        open(CERT_FILE, "wt").write(
            crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
        open(KEY_FILE, "wt").write(
            crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
 
create_self_signed_cert()
