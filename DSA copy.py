from math import gcd as bltin_gcd
import math
import random
import os.path

def main():
    #Public Parameters
    p_value = 23
    q_value = 11
    y_value = 8

    #Hashed Message
    h_m = 3

    #Signed Signature
    r_value = 1
    s_value = 2
    givenSig = [r_value, s_value]

    #Given From RSA
    h_value = 4 

    #Fill in the blanks:
    g_value = findGVal(q_value, p_value)

    x_value = findValidPow(y_value, g_value, p_value, q_value)

    public_key = [p_value, q_value, g_value, y_value]
    private_key = [p_value, q_value, g_value, x_value]

    #print(getDigitalSig(h_value, private_key))
    
    print(verifySig(h_m, givenSig, public_key))

def findGVal(q_value, p_value):
    for i in range(2, p_value):
        if pow(i, q_value, p_value) == 1:
            return i

#Will find a value y that satisfies val = pow(x, y, z) will pause once we hit the given upperbound
def findValidPow(val, x, z, upperbound):
    for y in range(upperbound):
        if val == pow(x, y, z):
            return y
    return -1 

def getDigitalSig(message, key):
    p_value = key[0]
    q_value = key[1]
    g_value = key[2]
    x_value = key[3]

    h_value = message
    k_value = 300
    r_value = pow(g_value, k_value, p_value)
    i_value = pow(k_value, -1, q_value)
    s_value = i_value * (h_value + r_value * x_value) % q_value

    return [r_value, s_value]

def verifySig(message, signature, key):
    h_value = message

    p_value = key[0]
    q_value = key[1]
    g_value = key[2]
    y_value = key[3]

    r_value = signature[0]
    s_value = signature[1]

    w_value = pow(s_value, -1, q_value)

    u1_value = pow(h_value * w_value, 1, q_value)
    u2_value = pow(r_value * w_value, 1, q_value)


    v_value =  (((pow(g_value, u1_value))*(pow(y_value, u2_value))) % p_value) % q_value

    print(key)
    print(v_value)
    if v_value == r_value:
        return True
    
    return False




if __name__ == "__main__":
    main()