from math import gcd as bltin_gcd
import math
import os.path

def main():

    #Take the path towards the file
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "Test Files\\testfile1.txt")

    #Set Up the Primes and Payload
    p_value = 0
    q_value = 0
    payload = [] 

    #Read the file
    with open(path) as f:
        line1 = f.readline().split()
        p_value = int(line1[0])
        q_value = int(line1[1])
        lines = f.readlines()
        for line in lines:
            payload.append(int(line))
        
        n_value = p_value * q_value
    et_value = (p_value - 1) * (q_value - 1)

    #Generate Public and Private Key
    e_value = threeCoprimes(et_value)
    d_value = pow(e_value, -1, et_value)

    print(d_value * e_value)
   
    privateKey = [d_value, n_value]
    publicKey = [e_value, n_value]

    cipherText = encrypt(payload, publicKey)
    plainText = decrypt(cipherText, privateKey)

    print(plainText)
   

#Given number n, we will find the three smallest coprimes
def threeCoprimes(n):
    coprimeList = []
    for i in range(2, n):
        if coprime(i, n):
            coprimeList.append(i)
        if len(coprimeList) == 3:
            break
    return coprimeList[2]

def encrypt(plaintext, keypair):
    cipherText = []
    for item in plaintext:
        raisePower = math.pow(item, keypair[0]) 
        cipherText.append(int(raisePower % keypair[1]))
    
    return cipherText

def decrypt(ciphertext, keypair):
    plaintext = []
    print(keypair, ciphertext)
    for item in ciphertext:
        raisePower = pow(item, keypair[0], keypair[1])
        plaintext.append(raisePower)
    return plaintext

#Will take two numbers a and b and return if they are coprimes 
def coprime(a, b):
    return bltin_gcd(a, b) == 1

if __name__ == "__main__":
    main()