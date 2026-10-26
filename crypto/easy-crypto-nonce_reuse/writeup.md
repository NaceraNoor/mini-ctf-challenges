# crypto-easy-reuse

**Category:** Crypto | **Difficulty:** easy
**Flag:** `shellmates{...}`

## Challenge
Two messages were encrypted with AES-GCM using the same key and the same
nonce. M1 leaked, and we are given C1 and C2 (hex-encoded).

## Vulnerability
AES-GCM encrypts in CTR mode: the ciphertext is the plaintext XORed with a
keystream that depends only on the (key, nonce) pair. Reusing the same pair
produces the same keystream for both messages:

    C1 = M1 XOR keystream
    C2 = M2 XOR keystream

## Solution
1. Convert the data to bytes: encode M1 as UTF-8 bytes, and decode the hex
   strings C1 and C2 into bytes.
2. XOR the two ciphertexts. The keystream cancels out, because a XOR a = 0:

       C1 XOR C2 = (M1 XOR keystream) XOR (M2 XOR keystream)
                 = M1 XOR M2 XOR (keystream XOR keystream)
                 = M1 XOR M2

   (this uses the associativity and commutativity of XOR)
3. XOR with the known M1 to isolate M2, since a XOR a = 0 and a XOR 0 = a:

       M2 = C1 XOR C2 XOR M1

4. Decode the resulting bytes from UTF-8 to get the flag.

Note: the result has the length of the shortest input (C2 here), which is
exactly the length of the flag.

## Solve script
The solution script can be found at solution/solve.py