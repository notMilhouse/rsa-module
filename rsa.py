import math

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

def encrypt_message(m, e, N):
    return pow(m, e) % N

def decrypt_message(c, d, N):
    return pow(c, d) % N

def main():
    
    #leitura dos primos
    p = int(input("Insira o valor de p: "))

    q = int(input("Insira o valor de q: "))

    #definicao das constantes
    N = gen_N(p,q)
    phi_N = gen_phi_N(p,q)
    e = gen_e(phi_N, N)
    d = gen_d(phi_N, e)

    print("N={}\nPhi(N)={}\ne={}\nd={}".format(N,phi_N,e,d))

    m = int(input("Insira a mensagem para encriptar: "))
    c = pow(m,e) % N

    print("A mensagem encriptada eh: {}".format(c))

    print("Decriptando... {}".format(decrypt_message(c,d,N)))


if __name__ == "__main__":
    main()