# <Prog_No:3> <Ex_No:3> <Author: Purushottam Kumar>
# Write a program to calculate the sum of numbers from m to n.
print("\n Output of Prog_No:3 in Ex_No:3 implemented by Purushottam Kumar :\n")
M,N = [int(k) for k in input(" Enter Starting & Ending Point : ").split(',')]
temp=M
sum=0
while M<=N:
    sum+=M
    M+=1
print("\n Sum of numbers between ",temp," & ",N," = ",sum)
    
    


    

