
# we must first solve A^2 + B^2 = MC, where A is determined via the quadratic_residue function, M depends on A's value, and B = 1
def descent(number):
    # recursively solving the equation a**2 + b**2 = cm, given c, until m = 1 and a,b are as small as possible
    a = quadratic_residue(number)
    if (a == None):
        return
    b = 1  
    m = int(a**2 + b)/number
    print ("we calculate M to be (A^2 + B^2)/p, therefore (" + str(int(a^2)) +""+ str(int(b^2))+ ")/2 = " + str(int(m)))
    print("\nwe calculate the following values:\nA = "+str(a) +"\nB = 1" + "\nM = "+str(int(m))+
          "\ntherefore "+str(a)+"^2 + 1^2 = " +str(int(m))+" * " + str(number))
    recursive_descent(a, b, m, number)#
    return

def recursive_descent(A, B, M, prime):
    if (M == 1):
        # sol = [int(A), int(B)]
        print("\nthe solution is "+str(int(A)) +"^2 + "+str(int(B))+"^2 = "+str(prime))
        return
    u = A%M
    v = B%M
    new_a = int(((u*A + v*B)/M))
    new_b = int(((v*A - u*B)/M))
    new_m = int(((new_a**2) + (new_b**2))/prime) 
    print("\nwe calculate the following values:\nA = "+str(new_a) +"\nB = "+str(new_b)+"\nM = "+str(new_m)  +
          "\ntherefore "+str(new_a)+"^2 + "+str(new_b)+"^2 = " +str(new_m)+" * " + str(prime))
    recursive_descent(new_a, new_b, new_m, prime)

#a solution to x^2 congruent to -1 (modulo C) will be the value for A in the equation A^2 + 1 = MC, where C is user_input and M=  
def quadratic_residue(user_input):
    print("we must compute a solution to x^2 congruent to -1 modulo "+ str(user_input) +" to use as our initial value for A"     
    for x in range(1, user_input):#iterate up until a quadratic residue is found, modulo user_input
        if (x**2)%user_input == (-1 + user_input):
        # if ((x**2)%user_input)-user_input == (-1):
            print(str(x)+"^2 is congruent to -1 modulo "+str(user_input))
            print("therefore "+ str(x) + " will be our value for A. we will use 1 as our initial value for B")
            return x

    print("There are no integers such that x^2 is congruent to -1 modulo " + str(user_input))
    new_number = int(input("enter a number to compute via Fermat's Descent\n"))
    descent(new_number)
 


# log_2(n) recursive calls


# fun values to try
# 1028201
# 9649325
# 12049
# 88125  
