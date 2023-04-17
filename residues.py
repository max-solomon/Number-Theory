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

# determines if there exists a quadratic residue (modulo p) for some given number p with Eulers criterion
def eulers_criterion(p):
    if ((-1)**((p-1)/2)) == (-1 + p):
        print("by Eulers Criterion, there exists a quadratic residue mod " + str(p))
        return True
    else:
        return False #TODO test this more

# computes the jacobi symbol of params (a/b)
def jacobi(a,b):
    if b%2 == 0 or b < 0:
        print("b must be an odd positive integer")
        return
    symbols = []
    while b > 1:
        #if the number is negative
        if a < 0:
            if b%4 == 3:
                # symbols.append(-1)
                a=a*-1
            else:
                symbols.append(1)
        a = abs(a)# otherwise (-1/b) = 1, and the negative is seamlessly handled
      #even numbers are now handled
        twos = 0
        while a%2 == 0:
            a = a/2
            twos = twos+1
        if twos > 0:
            if b%8 == 3 or 5:
                symbols.append(-1)
                a=a*-1
            else:
                symbols.append(1)
                
        temp = a
        a = b%a
        b = temp  
        if b%4 and a%4 == 3:
            symbols.append(-1)
            a=a*-1
        else:
            symbols.append(1)
            # a = a*-1
    # print(symbols)
    # print(a)
    return prod(symbols)
    

    




#     # factors = []
#     if (a%2 or b%2 == 1) or (a or b < 0):
#         return
#     if a < 0 and b%4 == 3:
#         symbol = symbol * -1
#     a = abs(a)# otherwise (-1/b) = 1, and the negative is seamlessly handled
#     twos = 0
#     while a%2 == 0:
#         a = a/2
#         twos = twos+1
#     # factors = factorize(a)
#     b_mod_8 = b%8
#     if twos > 0 and b_mod_8 == 3 or 5:
#         symbol = symbol*(-1*twos)
#         # symbol = symbol*(-1**factors.count(2))
#         a = a - 2**twos#all factors of 2 removed, all that are left are positive prime factors

#         # while factors.count(2)>0:
#         #     factors.remove(2)
#     #at this point,a and b are both odd positive integers
#     # for i in range(len(factors)): this would be legendre factorization
#     # a = prod(factors)
#     temp = 0
#     while a>1:
#         temp = a
#         a = b%a
#         b = temp  
#         if b%4 and a%4 == 3:
#             symbol = symbol * -1
#     print(symbol) 
#     return symbol

# jacobi(5,13)

            
        
    
    
        
    
# print(quadratic_residue(787))
# def legendre(a, p):
#     if (is_prime(p)==False or p == 2 or is_coprime(a,p)==False):
#         return
#     else:
#         factors = []
#         factors = factorize(a)
#         legendre_symbol = 1
#         # factor out -1
#         if factors.index(0) == -1:
#             legendre_symbol = (-1)**((p-1)/2)
#         #factor out squares
#         for a in range(len(factors)):
#             if factors.count(a)%2 == 0:
#                 while factors.count(a)>0:
#                     factors.remove(a)
        
                
            