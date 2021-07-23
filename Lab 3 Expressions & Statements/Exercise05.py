# <Prog_No : 5> <Ex_No : 2> <Author: Purushottam Kumar>
# Write a program to swap two numbers using a temporary variable.

print("\n Output of Prog_No:5 in Ex_No:2 implemented by Purushottam Kumar :\n")

x=int(input(" Enter First Number (A) : "))
y=int(input(" Enter Second Number (B) : "))
print("\n Before swapping ")
print(" A = "+str(x) + " and B = "+ str(y))
temp = x;
x = y;
y=temp;
print("\n After swapping ")
print(" A = "+str(x) + " and B = "+ str(y))
