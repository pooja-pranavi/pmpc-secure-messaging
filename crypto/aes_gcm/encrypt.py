from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import hashlib

def derive_key(key):
    return hashlib.sha256(key.encode()).digest()

def aes_gcm_encrypt(data, key):
    key = derive_key(key)
    aesgcm = AESGCM(key)

    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, data.encode(), None)

    return nonce + ciphertext

