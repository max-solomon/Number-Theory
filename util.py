#various utitity functions for more complex processes/algorithms

#determines if a given number n is prime by iteratively calculating if any number x such that 
# x < n, and the order of x (modulo n) == n-1, then n is prime
def is_prime(n):
    if n == 1:
        return True
    for x in range(1, n):
        if order(x, n) == (n-1):
            return True
    
    return False

# iteratively calculates and returns the order of a given integer/modulus pair
def order(a, modulus):#TODO: this is so inefficient and incredibly helpful
    for x in range(1, modulus):
        if ((a**x)%modulus == 1):
            return int(x)

def primitive_roots(modulo):
    roots = []
    primitive_roots = []
    print("all orders modulo "+str(modulo))
    for a in range(1,modulo):
        order_a = order(a, modulo)
        # roots.append(order(a,modulo))
        roots.append(order_a)
        print(str(a)+"^"+str(order_a)+ " is congruent to 1 modulo "+ str(modulo))
    max_order = max(roots)
    for i in range (len(roots)):
        if roots[i]==max_order:
            primitive_roots.append(i+1)
        
    return primitive_roots
    
        


#a primality test? that uses Fermat's little theorem
# def fermats_little_theorem(a, n):
#     if not is_coprime(a,n):
#         return False
    
#     if (a**(n-1))%n == 1:
#         return True
#     else:
#         return False
 
 #setting a lower bound may offer you what a sieve cannot       
# returns a list of primes less than the upper bound argument by checking if each odd number is prime or not        # 
def brute_force_primes(upperbound, lowerbound=3):
    primes = [2]
    if (upperbound == 3):
        primes.append(3)
        # print("\n"+str(primes))
        return primes
    if (lowerbound%2 == 0):
        lowerbound=lowerbound-1
    for x in range (lowerbound, upperbound, 2):
        if (is_prime(x)):
            # print(x, end=" ")
            primes.append(x)
    # print("\n"+str(primes))
    return primes

def brute_force_nth_prime(upperbound):
    primes = [2]
    if (upperbound == 3):
        primes.append(3)
        # print("\n"+str(primes))
        return primes
    while len(primes)<upperbound:
        x = 0
        if (is_prime(x)):
            # print(x, end=" ")
            primes.append(x)
    x=x+1
            
    # print("\n"+str(primes))
    return primes.pop

# returns a list of primes less than a given number using the Sieve of Eratosthenes algorithm
def sieve_of_eratosthenes(number):#this is wrong lol
    # consecutive_nums = [x for x in range(0,number,)]
    primes = []
    primes = brute_force_primes(int(number/2))
    consecutive_nums =[2]
    for x in range (3, number,2):
        consecutive_nums.append(x)# create list of potential prime/composite numbers
    # x = 0
    # while len(primes) != 0: #iterateuntil 
    for x in range(primes[x]+1, len(consecutive_nums)):
        if x % primes[x] == 0:
            consecutive_nums.remove(x)
    
    return consecutive_nums             
        
            
        
            
    # p = 2 #we start at the only even prime, 2
    # for y in range(2*p, number):
    #     consecutive_nums.remove(y)#remove all multiples of p from the list
    
#determines if the greatest common denominator of 2 numbers is 1        
def is_coprime(a, b):
    if (gcd(a, b) == 1):
        return True
    else:
        return False

#recursively determines the greatest common denominator of 2 numbers with Euclids algorithm
def gcd(a, b):
    if (a == 0 or b == 0):
        return 0
    if (a == b):
        return a
    if (a > b):
        return gcd(a - b, b)

    return gcd(a, b - a)

#returns the size of the string of repeating decimals in an infinite fraction (the period of the fraction)    
def period(numerator, denominator):
   # TODO: implement factorization to determine reduced fractions if needed
    if(is_coprime(denominator,10)== False or is_coprime(numerator,denominator)==False):
        return
    period = order(10, denominator)
    print(str(numerator/denominator))
    print(str(period))
    return period

#returns a list of primes, reduced modulo 3
# def primes_mod_three(n):#this doesnt work for some reason 
#     mod_three = []
#     primes = [] 
#     primes = brute_force_primes(n)
#     for x in range(n):
#         if (primes.index(x))%3==1:
#             mod_three.append(x)
            
#     return mod_three    

def x_mod_y_primes(num, x, y):
    print(str(x)+"mod "+ str(y))
    primes = []
    x_mod_y = []
    primes = brute_force_primes(num)
    for i in range(len(primes)):
        if primes[i]%y == x:
            x_mod_y.append(primes[i])
    
    return x_mod_y

# def foo():
#     primes = []
#     primes = x_mod_y_primes(300,5,8)
#     sol1 = []
#     sol2 = []
#     i = 1
#     k=2
#     for i in range(10):
#         sol1.append((primes[i]+3)/8)
#     for k in range(10):
#         sol2.append((2*k)*((4*k)**((primes[k]-5)/8)))
#     return sol1, sol2
        


# print(foo(90))

            
# def fermats_last_theorem(a, p):
#     if (not is_prime(p)):
#         print(str(p)+ "is not a prime")
#         return
#     elif(not is_coprime(p,a)):
#         print(str(p)+" and "+str(a) +" are not coprime")
#         return 
#     else:
#         print("a^p-1 congruent to 1 mod "+ str(p))
#         return [a, a**(p-1), 1, p]
#        
# def flt(a,m):
#     if 