n=int(input("Enter value of n : "))
if(n>0 and n<=10):
    for i in range(1,11):
        print("\n",n," x ",i," = ",n*i)
else:
    print("\nCorrect n value")
