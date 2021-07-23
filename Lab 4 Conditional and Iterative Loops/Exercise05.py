# <Prog_No:5> <Ex_No:3> <Author: Purushottam Kumar>
# WAP to enter a decimal number and convert it into a binary equivalent.

print("\n Output of Prog_No:5 in Ex_No:3 implemented by Purushottam Kumar :\n")

n=int(input(" Enter A Decimal Number : "))
temp=n
sum=i=0
while(n>0):
    rem=n%2
    sum+=rem*(10**i)
    n//=2
    i=i+1
print("\n Binary Equivalent of ",temp,"=",sum)



    


    

