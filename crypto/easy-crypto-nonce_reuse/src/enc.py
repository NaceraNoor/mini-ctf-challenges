from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

M1 = "Never reuse a nonce with the same key"
M2 = "shellmates{3714c5dd98339b87646451e3}"

assert M1.isascii() and M2.isascii()
assert len(M1.encode()) >= len(M2.encode())
assert len("3714c5dd98339b87646451e3") >= 12

key = AESGCM.generate_key(bit_length=128)
nonce = os.urandom(12)
aes = AESGCM(key)

def enc(m):
    out = aes.encrypt(nonce, m.encode("utf-8"),None)
    return out[:-16].hex()

print(f"M1: {M1}")
print(f"C1: {enc(M1)}")
print(f"C2: {enc(M2)}")