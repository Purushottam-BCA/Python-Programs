# <Prog_No:10> <Ex_No:3> <Author: Purushottam Kumar>
# WAP to calculate square root of any number less than 1000 and not equal to and less than 0.
# (use break if number greater than 1000 and continue if number less than 0)

print("\n Output of Prog_No:10 in Ex_No:3 implemented by Purushottam Kumar :\n")

while True:
    n=int(input("\n Enter value of n : "))
    if(n>1000):
        break
    elif(n<=0):
        continue
    elif(n<1000):
        print("\n Square Root of ",n," = %.1f"%(n**0.5))

        
