# <Prog_No:10> <Ex_No:9> <Author: Purushottam Kumar>

from math import sqrt as root,log10 as log
print("\n Output of Prog_No:10 in Ex_No:9 implemented by PURUSHOTTAM KUMAR :\n")

x=float(input(" Enter First Number : "))
y=float(input(" Enter Second Number : "))
summ = x+y
diff = x-y
product = x*y
div = x/y
intdiv = x//y
log1=log(x)
Sqrt = root(x)
print("\n Sum : ("+str(x) + " + " + str(y) +") = " + str(summ))
print("\n Difference : ("+str(x) + " - " + str(y) +") = " + str(diff))
print("\n Product : ("+str(x) + " x " + str(y) +") = " + str(product))
print("\n Division : ("+str(x) + "/" + str(y) +") = " + str(div))
print("\n Integer Division : ("+str(x) + "//" + str(y) +") = " + str(intdiv))
print("\n Exponent : ("+str(x) + "^"+ str(y) +") = " + str(x**y))
print("\n Modulus : ("+str(x) + " % " + str(y) +") = " + str(x%y))
print("\n Log of : ("+str(x) + ") = " + str(log1))
print("\n Square Root of : ("+str(x) + ") = " + str(Sqrt))
