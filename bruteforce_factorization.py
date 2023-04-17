
# determines the unique factorization of a given integer.
# uses 4 nested brute force algorithms for determining order, primeness, and divisibility of n, 
# and generating a list of primes < n to factorize with

from util import is_prime, brute_force_primes

def factorize(number):
    # print("\ngiven a number "+ str(number) +", we determine the prime factorization to be")
    if is_prime(number):#if the number is prime, no factorization is possible
        return number #and we can simply return the given input
    else:
        unique_factors=[] #stores the prime factors of a given number
        if number < 0:
            unique_factors.append(-1)
            number = number*-1
        primes = [] #stores a generated list of primes
        primes = brute_force_primes(number)# any prime divisor is not greater than the original input 
        for i in range(len(primes)): #iterating thru the list of primes
            next_prime = primes[i] #select the next prime in the list
            factored = float(number/next_prime)#attempt division by the prime
            while (factored.is_integer()): #if the new number is a result of legal integer division
                unique_factors.append(next_prime)#store the newly discovered factor,
                factored = factored/next_prime# and keep dividing
                
                
    return unique_factors #return a list of prime factors of the given number
