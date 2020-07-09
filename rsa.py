"""
TODO Divide in separate files accordingly to function (constant generators, encryption utilities, interactive version)
TODO File handling and support
TODO String encryption

"""


import math
import os

keys = {}

def gen_N(p , q):
    return p * q

def gen_phi_N(p, q):
    return (p-1) * (q-1)

def gen_e(phi_N, N):
    possibilities = list(range(2, phi_N))
    for i in range(phi_N - 1, 1, -1):
        for j in range(i, 1, -1):
            if(i % j == 0 and phi_N % j == 0):
                possibilities.remove(i)
                break
    toRemove = []
    for i in possibilities:
        for j in range(i, 1, -1):
            if(i % j == 0 and N % j == 0):
                toRemove.append(i)
                break
    
    for i in toRemove:
        possibilities.remove(i)

    return possibilities[0]

def gen_d(phi_N, e):
    found_match = False
    d = 1
    while(not(found_match)):
        found_match = True if ((e*d % phi_N) == 1) else False
        d += 1
    return d-1

def gen_keys(p, q):

    N = gen_N(p,q)
    phi_N = gen_phi_N(p,q)
    e = gen_e(phi_N, N)
    d = gen_d(phi_N, e)

    keys['public'] = (e, N) 
    keys['private'] = (d, N)

def encrypt_message(m, public_key):
    if(not public_key):
        return 0
    return pow(m, public_key[0]) % public_key[1]

def decrypt_message(c, private_key):
    if(not private_key):
        return 0
    return pow(c, private_key[0]) % private_key[1]



def main():
    
    while(True):
        print("-- Choose one of the following --")
        option = int(input("[1] - Setup RSA variables\n[2] - Encrypt a message\n[3] - Decrypt a message\n[0] - Exit"))

        if(option == 1):
            os.system("clear")
            
            print("-- Setup RSA Variables -- ")
            
            p = int(input("Insert the value for the first prime p: "))
            q = int(input("Insert the value for the second prime q: "))
        
            gen_keys(p, q)

        elif(option == 2):
            os.system("clear")
            
            print("-- Message encryption -- ")

            m = int(input("Insert a message to encrypt: "))
            
            if(keys):

                c = encrypt_message(m, keys["public"])

            else:

                e = int(input("Insert the encryption key 'e': "))
                N = int(input("Insert the public key 'N': "))

                c = encrypt_message(m, (e, N))

            print("The encrypted message is: {}".format(c))

        elif(option == 3):

            c = int(input("Insert a message do decrypt: "))

            if(keys):
                
                m = decrypt_message(c, keys["private"])
                
            else:

                d = int(input("Insert the decryption key 'd': "))
                N = int(input("Insert the public key 'N': "))

                m = decrypt_message(c, (d, N))

            print("Decrypting to... {}".format(m))
            
        elif(option == 0):
            break
        else:
            print("Invalid Option!")
            os.system("clear")
            continue


if __name__ == "__main__":
    main()