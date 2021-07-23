# <Prog_No:9> <Ex_No:3> <Author: Purushottam Kumar>
# Write a program to sum the series : 
    # (i) 1 + 1/2 + 1/3 +......+ 1/n
    # (ii) 1/1^2 + 1/2^2 + 1/3^2 + .... + 1/n^2

print("\n Output of Prog_No:9 in Ex_No:3 implemented by Purushottam Kumar :\n")

n=int(input(" Enter value of n : "))
if(n>0):
    sum1=0  #for 1st series
    sum2=0  #for 2nd series
    for i in range(1,n+1):
        sum1+=(1/i)
        sum2+=(1/(i*i))
    print("\n Sum of Series 1 : %.2f" % sum1)
    print("\n Sum of Series 2 : %.2f" % sum2)
else:
    print("\n only positive number allowed !!\n")

