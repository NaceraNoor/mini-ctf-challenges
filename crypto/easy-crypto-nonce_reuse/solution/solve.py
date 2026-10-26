M1 = "Never reuse a nonce with the same key"
C1 = "ec5e4da3154a58a6d9503f452713bb968d5a69ea32323bf288604d35012bf4694a023a2b33"
C2 = "d1535eaa0b074bb7c95021567102e19ad65d68f37d687ca3ca2c1266156ea1311e476233"

def xor(a: bytes, b: bytes, c: bytes) -> bytes:
    temp = bytes(x ^ y for x, y in zip(a, b))
    return bytes(x ^ y for x,y in zip(temp, c))

flag_bytes = xor(M1.encode(), bytes.fromhex(C1), bytes.fromhex(C2))
flag = flag_bytes.decode("utf-8") 

print(flag)