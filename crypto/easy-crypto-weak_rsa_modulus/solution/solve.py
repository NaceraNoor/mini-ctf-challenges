from Crypto.Cipher import AES 
from Crypto.Util.number import long_to_bytes

n = 78705278030404924634912600185866646679004457193466472214316647853522651019927
e = 887
encrypted_AES_key = 29021373072573645935406915010682199808577197864101685347262047836783578350850
nonce =  "504795ac7501946a"
encrypted_data = "03e8a7855182168b5a2fe31b0bebf95fe949ce9694cce6df68ce50fff8296e2af266fd82302ca145ec9d93bb"

p = 280497256406280882057179964443699601601
q = 280591970983152046113830578173751056727
phi = (p-1)*(q-1)
d = pow(e, -1, phi)
plain_aes_key = long_to_bytes(pow(encrypted_AES_key, d, n)).rjust(16, b"\x00")

cipher = AES.new(plain_aes_key, AES.MODE_CTR, nonce = bytes.fromhex(nonce))
plain_data = cipher.decrypt(bytes.fromhex(encrypted_data))

print(plain_data.decode('utf-8'))

