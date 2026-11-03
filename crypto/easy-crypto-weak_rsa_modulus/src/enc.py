from Crypto.Cipher import AES 
from Crypto.Util.number import getPrime
from Crypto.Random import get_random_bytes
from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import isPrime
from math import gcd

flag = "shellmates{4026bf0d37f12ea1a2de147a4e3b2f0a}"

p = 280497256406280882057179964443699601601
q = 280591970983152046113830578173751056727
assert isPrime(p) and isPrime(q)

n = p * q 
phi = (p-1)*(q-1)

while True: 
    e = getPrime(10)
    if gcd(e, phi) == 1:
        break

d = pow(e, -1, phi)

aes_key = get_random_bytes(16)

encrypted_aes_key = pow(bytes_to_long(aes_key), e, n)

print('n =', n)
print('e =', e) 
print('key =', encrypted_aes_key)

cipher = AES.new(aes_key, AES.MODE_CTR)

encrypted_data = cipher.encrypt(flag.encode())

print('nonce= ', cipher.nonce.hex())
print('ciphertext=', encrypted_data.hex())


