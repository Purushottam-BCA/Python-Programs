# <Prog_No:4> <Ex_No:3> <Author: Purushottam Kumar>
# Write a program to read the numbers until -1 is encountered.
# Also count the negative, positive and zeros entered by the user.

print("\n Output of Prog_No:4 in Ex_No:3 implemented by Purushottam Kumar :\n")

positive=negative=zeros=N=0
while(N!=-1):
    N=int(input(" Enter Number : "))
    if(N>0):
        positive+=1
    elif(N<0):
        negative+=1
    elif(N==0):
        zeros+=1
print("\n No. Of Zeros : ",zeros)
print("\n No. Of Negative : ",negative)
print("\n No. Of Positive : ",positive)


    


    

