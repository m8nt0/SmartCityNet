from OpenSSL import crypto

def generate_key():
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)
    return key

def save_key(key, filename):
    with open(filename, "wb") as key_file:
        key_file.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))

def generate_certificate(key):
    cert = crypto.X509()
    cert.get_subject().CN = "SmartCityNet"
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10*365*24*60*60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, 'sha256')
    return cert

def save_certificate(cert, filename):
    with open(filename, "wb") as cert_file:
        cert_file.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

key = generate_key()
save_key(key, "private.key")

cert = generate_certificate(key)
save_certificate(cert, "certificate.crt")

