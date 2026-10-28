from Crypto.Util.number import getPrime

p = getPrime(128)
q = getPrime(128)

n = p*q

print(p)
print(q)
print(n)