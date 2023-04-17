from util import is_prime, is_coprime
from bruteforce_factorization import factorize
from math import prod
# iteratively determines the quadratic residues of a given modulus
def quadratic_residue(modulus):
    qr=[]
    for x in range(1, int((modulus)/2)+1):#iterate up until a quadratic residue is found, modulo user_input
        qr.append(int((x**2)%modulus))
    print(str(qr.sort))
    return qr                

# iteratively determines the cubic residues of a given modulus
def cubic_residue(number, modulus):
    cr = []
    for x in range(1, modulus):#iterate up until a quadratic residue is found, modulo user_input
        if (x**3)%modulus == (number%modulus):
            cr.append(int(x))   
    return cr
