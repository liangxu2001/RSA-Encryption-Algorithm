from math import gcd as bltin_gcd
import math
import random
import os.path

def main():
    #Public Parameters
    p_value = 26557
    q_value = 2213
    y_value = 4563

    #Hashed Message
    h_m = 1433481460655447667453059555690580347961767007610

    #Signed Signature
    r_value = 1185
    s_value = 1326
    givenSig = [r_value, s_value]

    #Given From RSA
    h_value = 19463 

    #Fill in the blanks:
    g_value = g_value = pow(h_value, int((p_value - 1) / q_value), p_value)
    x_value = findValidPow(y_value, g_value, p_value, q_value)

    public_key = [p_value, q_value, g_value, y_value]
    private_key = [p_value, q_value, g_value, x_value]

    newSig = getDigitalSig(h_m, private_key, public_key)
    print(newSig)

    print(verifySig(h_m, newSig, public_key))
    print('x', x_value)

#Will find a value y that satisfies val = pow(x, y, z) will pause once we hit the given upperbound
def findValidPow(val, x, z, upperbound):
    for y in range(upperbound):
        if val == pow(x, y, z):
            return y
    return -1 

def getDigitalSig(message, privateKey, publicKey):
    p_value = privateKey[0]
    q_value = privateKey[1]
    g_value = privateKey[2]
    x_value = privateKey[3]

    for possible_k in range(1, q_value):
        h_value = message
        k_value = possible_k
        r_value = pow(g_value, k_value, p_value)
        i_value = pow(k_value, -1, q_value)
        s_value = i_value * (h_value + r_value * x_value) % q_value
        possible_sig = [r_value, s_value]

        if verifySig(h_value, possible_sig, publicKey):
            print(possible_sig)
            return possible_sig

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

    v_value =  (((pow(g_value,u1_value))*(pow(y_value,u2_value))) % p_value) % q_value

    if v_value == r_value:
        return True
    
    return False


if __name__ == "__main__":
    main()