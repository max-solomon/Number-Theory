from residues import eulers_criterion

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



#a solution to x^2 congruent to -1 (modulo C) will be the value for A 
#in the equation A^2 + 1 = MC, where C is user_input and M=  
def quadratic_residue(user_input):
    print("we must compute a solution to x^2 congruent to -1 modulo "+ str(user_input) +" to use as our initial value for A")
    # if (user_input%4 != 1):
    #     print("However, "+str(user_input)+ " is not congruent to 1 mod 4")
    #     print("Therefore there are no integers such that x^2 is congruent to -1 modulo " + str(user_input))
    #     new_number = int(input("enter a number to compute via Fermat's Descent\n"))
    #     descent(new_number)
    
    # if not eulers_criterion(user_input):
    #     print("There are no integers such that x^2 is congruent to -1 modulo " + str(user_input))
    #     new_number = int(input("\nenter a number to compute via Fermat's Descent\n"))
    #     descent(new_number)
        
    for x in range(1, user_input):#iterate up until a quadratic residue is found, modulo user_input
        if (x**2)%user_input == (-1 + user_input):
        # if ((x**2)%user_input)-user_input == (-1):
            print(str(x)+"^2 is congruent to -1 modulo "+str(user_input))
            print("therefore "+ str(x) + " will be our value for A. we will use 1 as our initial value for B")
            return x

    print("There are no integers such that x^2 is congruent to -1 modulo " + str(user_input))
    new_number = int(input("enter a number to compute via Fermat's Descent\n"))
    descent(new_number)
    
# print(557,55,26,12049)
# print(recursive_descent(42,11,1,1885))
# print(259,1,34,1973) 
# print(recursive_descent(249,1,34,1973))
# print(261,947,10,96493)
# print(recursive_descent(261,947,10,96493))
print(recursive_descent(947,261,10,96493))

# print(descent(1189)) # 29929
# log_2(n) recursive calls
# print(descent(12050))
# print(quadratic_residue(12050))

# fun values to try
# 1028201
# 9649325
# 12049
# 88125  


##################### 12050 breaks the program?
# is there something numerically special about 12050? or is it just a programming error?
#i only picked it because 12049 works and i wanted to intentionally make it return26
# the last recursive call before crashing states:

# we calculate the following values:
# A = 0
# B = 0
# M = 0
# therefore 0^2 + 0^2 = 0 * 12050
# Traceback (most recent call last):
#   File "/mnt/c/Users/Max/Desktop/vscode/AMAT 425 Number Theory/fermats_descent.py", line 57, in <module>
#     solutions = descent(number)
#                 ^^^^^^^^^^^^^^^
#   File "/mnt/c/Users/Max/Desktop/vscode/AMAT 425 Number Theory/fermats_descent.py", line 14, in descent
#     recursive_descent(a, b, m, number)#
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/mnt/c/Users/Max/Desktop/vscode/AMAT 425 Number Theory/fermats_descent.py", line 30, in recursive_descent
#     recursive_descent(new_a, new_b, new_m, prime)
#   File "/mnt/c/Users/Max/Desktop/vscode/AMAT 425 Number Theory/fermats_descent.py", line 30, in recursive_descent
#     recursive_descent(new_a, new_b, new_m, prime)
#   File "/mnt/c/Users/Max/Desktop/vscode/AMAT 425 Number Theory/fermats_descent.py", line 30, in recursive_descent
#     recursive_descent(new_a, new_b, new_m, prime)
#   [Previous line repeated 1 more time]
#   File "/mnt/c/Users/Max/Desktop/vscode/AMAT 425 Number Theory/fermats_descent.py", line 23, in recursive_descent
#     u = A%M
#         ~^~
# ZeroDivisionError: integer modulo by zero
