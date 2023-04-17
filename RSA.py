#prime modulus must exceed 126 to avoid cancelling out letters
from util import brute_force_primes, is_coprime
from eulers_totient import phi
import secrets

def random_encrypt(message, n = 300):
    primes = []
    primes = brute_force_primes(n+n, n)
    # random_prime = primes[random(1,len(primes))]
    random_prime = secrets.choice(primes)
    phi_prime = phi(random_prime)
    coprime_exponents = []
    i=2#so we never have 2 as our prime
    for i in range(n+n):
        if is_coprime(i, phi_prime):
            coprime_exponents.append(i)
    # random_exponent = coprime_exponents[random(1,len(coprime_exponents))]
    random_exponent = secrets.choice(coprime_exponents)
    print("random_exponent: "+ str(random_exponent))
    print("random prime: "+ str(random_prime))
    return encrypt(message, random_prime, random_exponent), random_prime, random_exponent
            
# we encrypt  numeric data by raising it to an exponent, then reducing it mod m
def encrypt(message, prime, exponent):
    if not is_coprime(exponent, phi(prime)):
        print("select a new exponent that is coprime to phi(m)")
        return
    letters = []
    letters = split(message)
    for i in range(len(letters)):
        letters[i] = ord(letters[i])#unicode conversion
    print("\noriginal message: " + str(message)+"\ninitial 'encoding' exponent: "+ str(exponent)+"\nmodulus: "+ str(prime))
    print("\nthe message is numerically encoded via their unicode values to: \n"+ str(letters))
    primes = []
    primes = brute_force_primes(len(message))
    encrypted = []
    for x in range(len(message)):
        encrypted.append((letters[x]**exponent)%prime)
    print("\nwe raise each numeric value to the power of "+ str(exponent)+", and reduce each value modulo "+ str(prime) + ".\nthis will encrypt our numeric values to: \n" + str(encrypted))
    # print()
    return encrypted, prime, exponent
    # e must be coprime to phi(m)
    
def decrypt(message, prime, exponent):
    # message = str(message_)
    # message = list(message)
    # # message = ([x for x in message_])
    d = inverse(exponent, prime)
    print("\nby raising each encrypted number to the power of "+ str(d)+" (the inverse of "+ str(exponent) +" modulo "+str(prime)+", or 'the decoding exponent'), and reducing the new result modulo "+ str(prime)+",")
    print("we will be decrypt/decode this to read as:")
    decrypted = []
    i = message[0]
    for x in range(len(i)):
        # j = (message[x]**d)%prime
        # TODO rename every variable lmao
        t = i[x]
        
        j = (t**d)%prime

        decrypted.append(chr(j))
        
    return "".join(decrypted)

# calculating the nth prime takes forever. what about just retrieving it?

def inverse(e, moduli):
    d = 1
    for d in range(moduli):
        if (d*e)%phi(moduli) == 1:
            return d
    print(str(e)+ "is not invertible, modulo "+ str(moduli))

def split(word):
    return list(word)

def tuple_to_list(t):
    return [*t]


# m, p , e = random_encrypt("python is weird")    
# print(decrypt(m,p,e))


