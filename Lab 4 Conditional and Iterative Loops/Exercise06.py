# <Prog_No:6> <Ex_No:3> <Author: Purushottam Kumar>
# WAP to enter a binary number and convert it into a decimal equivalent.

print("\n Output of Prog_No:6 in Ex_No:3 implemented by Purushottam Kumar :\n")

n=int(input(" Enter A binary Number : "))
temp=n
Dec=i=flag=0
while(n>0):
    rem=n%10
    if(rem==0 or rem==1):
        Dec+=rem*(2**i)
        n//=10
        i+=1
    else:
        print("\n It is not a binary number")
        flag=1
        break
if(flag==0):
    print("\n Decimal Equivalent of ",temp,"=",Dec,"\n")



    


    

