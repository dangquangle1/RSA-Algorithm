import sys
import math
from typing import Tuple

# This program takes in the inputs of a public key and a plaintext message
# and calculates the private key and the ciphertext message.

# Run this program by running the script in the terminal with the parameters in
# the following order: e, n, plaintext message
# Example: python RSA.py 7 77 100
# e=7, n=77, plaintext message=100

#extended euclidian algorithm
def extended_euclidian_algorithm(a: int, b: int) -> Tuple[int, int, int]:
    if a == 0:
        return (b, 0, 1)
    else:
        b_div_a, b_mod_a = divmod(b, a)
        g, x, y = extended_euclidian_algorithm(b_mod_a, a)
        return (g, y - b_div_a * x, x)

#modular inverse
def modinv(a: int, b: int) -> int:
    g, x, _ = extended_euclidian_algorithm(a, b)
    if g != 1:
        print("The gcd of a,b != 1")
    return x % b

#ecnrypts a message using the public key <e,n> (RSA algorithm)
def encrypt_message(plaintext, e, n):
    encrypted_message = (math.pow(plaintext, e)) % n
    return encrypted_message

#main
def main():
    arg = sys.argv[0:]

    #gets the 3 inputs from the command line when running
    e = int(arg[1])
    n = int(arg[2])
    plaintext = int(arg[3])

    #finds p and q given n
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i = i+1
        else:
            n = n//i
            factors.append(i)
    if n > 1:
        factors.append(n)
    p = factors[0]
    q = factors[1]

    n = int(arg[2]) #set n back to original input

    phi = (p-1) * (q-1) #calculates phi
    d = modinv(e, phi) #calculates d, the private key

    print("The public key <e,n> is: <" + str(e) + ", " + str(n) + ">") #prints public key
    print("The private key <d,n> is: <" + str(d) + ", " + str(n) + ">") #prints private key
    encrypted_message = encrypt_message(plaintext, e, n) #encrypts the plaintext into a ciphertex
    print ("Given the plaintext message: '" + str(plaintext) + "'. The cipertext message is: '" + str(int(encrypted_message)) +"'") #prints encrypted ciphertext

#runs program
if __name__ == "__main__":
    main()
