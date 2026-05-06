from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import hashlib

def derive_key(key):
    return hashlib.sha256(key.encode()).digest()

def aes_gcm_decrypt(data, key):
    key = derive_key(key)
    aesgcm = AESGCM(key)

    nonce = data[:12]
    ciphertext = data[12:]

    decrypted = aesgcm.decrypt(nonce, ciphertext, None)
    return decrypted.decode()
