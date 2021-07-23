# <Prog_No:8> <Ex_No:3> <Author: Purushottam Kumar>
# WAP to find out whether a given number is prime or composite.

print("\n Output of Prog_No:8 in Ex_No:3 implemented by Purushottam Kumar :\n")

num=int(input(" Enter a poitive Integer : "))
if(num>0):
    if(num<2):   #Only For 0 & 1
        print("\n",num," is neither prime nor composite.\n")
    elif(num==2):
        print("2 is prime.\n")
    else:
        for i in range(2,int(num**0.5)):
            if(num%i==0):
                print("\n",num," is a composite number\n")
                break
        else:
            print("\n",num," is a prime number\n")
else:
    print("\n You have entered Negative number !!\n")

