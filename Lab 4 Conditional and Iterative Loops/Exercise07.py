# <Prog_No:7> <Ex_No:3> <Author: Purushottam Kumar>
# Write a program to calculate GCD of two numbers.

print("\n Output of Prog_No:7 in Ex_No:3 implemented by Purushottam Kumar :\n")

a,b=[int(x) for x in input(" Enter Two poitive Integers : ").split(',')]
if(a<b):
    a,b=b,a   #setting lowest = b & biggest = a
while(a>0):   
    if(b==0):
        print("\n GCD = ",a)
        break
    else:
        temp=a    
        a=b       
        b=temp%b  
       
