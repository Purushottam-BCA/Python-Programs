nm=int(input("Enter a 5 digit Number : "))
if(len(str(nm))==5):
    sum=0
    for i in range(5):
        last=nm%10
        sum+=last
        nm//=10
    else:
        print("\nSum of digit : ",sum)
else: print("\nEnter a valid 5 digit number")
