# <Prog_No:2> <Ex_No:4> <Author: Purushottam Kumar>
# Write a program to calculate the roots of a quadratic equation.
from math import sqrt
print("\n Output of Prog_No:2 in Ex_No:4 implemented by Purushottam Kumar :\n")
a,b,c = [int(n) for n in input(" Enter Cofficient of X^2,X & Constant : ").split(',')]
if a!=0:
    D=(b*b)-(4*a*c)
    if D>0:
        X=(-b +sqrt(D))/(a*2)
        Y=(-b -sqrt(D))/(a*2)
        print("\n Roots are real and unequal.")
        print("\n Root 1 = ",X,"\n Root 2 = ",Y)
    elif D==0:
        X=(-b+sqrt(D))/(2*a)
        print("\n Roots are real and equal.")
        print("\n Root 1 = ",X,"\n Root 2 = ",X)
    else:
        print("\n Roots are Imaginary.\n")
else:
    print("\n Cofficient of x^2 Can't be Zero.")
    
    


    

