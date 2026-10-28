# easy-crypto-small_modulus

**Category:** Crypto | **Difficulty:** Easy
**Flag:** `shellmates{4026bf0d37f12ea1a2de147a4e3b2f0a}`

## Challenge
An AES key was encrypted with RSA, and the flag was encrypted with that AES
key. Recover the RSA private key to get the AES key, then decrypt the flag.

## Vulnerability
The RSA modulus `n` is only 130 bits (two 65-bit primes), so it can be
factored with common tools in a reasonable time. Once `n = p * q` is known,
the private exponent can be computed and the encrypted AES key recovered.

## Requirements
    pip install pycryptodome

## Solution
1. Factor `n` to get `p` and `q` (https://www.alpertron.com.ar/ECM.HTM).
2. Compute `phi = (p - 1) * (q - 1)`.
3. Compute the private exponent: `d = pow(e, -1, phi)`.
4. Decrypt the AES key: `m = pow(c, d, n)`, then convert it to 16 bytes
   with `long_to_bytes(m).rjust(16, b"\x00")`.
5. Decrypt the ciphertext with AES-CTR using that key and the given nonce
   (`bytes.fromhex(...)` for the nonce and ciphertext).
6. Decode the result to get the flag.

## Solve script
See `solution/solve.py`.