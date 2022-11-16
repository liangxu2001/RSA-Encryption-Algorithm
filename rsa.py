from math import gcd as bltin_gcd
import sys

def main():

    #Take the path towards the file
    args = sys.argv
    if len(args) != 2:
        print('Improper arguments given. Please check argument format and try again. Terminating program')
        return
    path = args[1]

    #Set Up the Primes and Payload
    p_value = 0
    q_value = 0
    message = 0 

    #Read the file
    with open(path) as f:
        #Grab all the lines from the text file
        lines = f.readlines()
        for line in lines:
            curline = line.split()

            #If the text line has two integers, then we have a new p and q values
            if len(curline) == 2: 
                p_value = int(curline[0])
                q_value = int(curline[1])

            #If the text line has 1 integer, we have a new message
            else:
                message = int(curline[0])

                #Using our current P and Q value, calculate some metrics
                n_value = p_value * q_value
                et_value = (p_value - 1) * (q_value - 1)
                e_value = threeCoprimes(et_value)
                d_value = pow(e_value, -1, et_value)

                #Generate a Pulbic and Private Key
                privateKey = [d_value, n_value]
                publicKey = [e_value, n_value]

                #Encrypt message then Decrypt the message
                cipherText = encrypt(message, publicKey)
                plainText = decrypt(cipherText, privateKey)

                #Print all of our data
                print('p:', p_value, end=', ')
                print('q:', q_value, end=', ')
                print('n:', n_value, end=', ')
                print('phi:', et_value, end=', ')
                print('e:', e_value, end=', ')
                print('d:', d_value, end=', ')
                print('message:', message, end=', ')
                print('encrypted:', cipherText, end=', ')
                print('decrypted:', plainText)
                
#Given number n, we will find the three smallest coprimes
def threeCoprimes(n):
    coprimeList = []
    for i in range(2, n):
        if coprime(i, n):
            coprimeList.append(i)
            #Once we get 3 coprimes we are all set, start to terminate
        if len(coprimeList) == 3:
            break
    return coprimeList[2]

#Fuction will encrypt our message given public key
def encrypt(plaintext, keypair):
    cipherText = pow(plaintext, keypair[0], keypair[1])
    return cipherText

#Function will decrypt our message given private key
def decrypt(ciphertext, keypair):
    plaintext = pow(ciphertext, keypair[0], keypair[1])
    return plaintext

#Will take two numbers a and b and return if they are coprimes 
def coprime(a, b):
    return bltin_gcd(a, b) == 1

if __name__ == "__main__":
    main()