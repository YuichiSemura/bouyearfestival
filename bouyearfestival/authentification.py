import os

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

class Authentificater:
    def __init__(self, pub_file, sec_file):
        # declare
        self.sec_key = ""
        self.pub_key = ""
        # file not exist
        if not (os.path.exists(pub_file) and os.path.exists(sec_file)):
            key = RSA.generate(4096)
            with open(sec_file, "wb") as f:
                f.write(key.exportKey("PEM"))
            with open(pub_file, "wb") as f:
                f.write(key.publickey().exportKey("PEM"))
        # load key pair
        with open(sec_file, "r") as f:
            self.sec_key = RSA.importKey(f.read())
        with open(pub_file, "r") as f:
            self.pub_key = RSA.importKey(f.read())

    def make_sign(self, msg):
        hasher = SHA256.new(msg.encode())
        signer = PKCS1_v1_5.new(self.sec_key)
        sign = signer.sign(hasher)
        return sign

    def verify(self, msg, parity):
        hasher = SHA256.new(msg.encode())
        verifier = PKCS1_v1_5.new(self.pub_key)
        return verifier.verify(hasher, parity)
