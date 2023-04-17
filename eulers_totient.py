from util import is_prime, is_coprime
from bruteforce_factorization import factorize
import math

def phi(n):
    if is_prime(n):
        return n-1
    else:
        product = []
        prime_factors = factorize(n)
        
        while len(prime_factors) != 0: # iterate thru all needed primes
            next_prime = prime_factors[0]
            exponent_count = prime_factors.count(next_prime)
            
            if exponent_count == 1:
                product.append(next_prime-1) #unique factorize, then apply phi again
                prime_factors.pop(0) #remove single prime from the list
            else: # if there are primes raised by an exponent > 1
                product.append(next_prime**(exponent_count-1)*(next_prime-1))
                while prime_factors.count(next_prime) > 0:
                    prime_factors.pop(0)
            
    return math.prod(product)

#TODO fix this, define it better
# returns a list of integers congruent to 1 mod m for some composite number m
def eulers_theorem(m): # for every a coprime to m, a^phi(n) = 1 modulo m
    results = []
    for a in range(m):
        if is_coprime(a, m):
            results.append(a**phi(m))
    
    return results
    

# print(phi(4))