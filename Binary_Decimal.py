def bin_dec(n):
    i=0
    sum=0
    while(n>0):
        last=n%10
        sum=sum+(last*(2**i))
        n//=10
        i+=1
    print(sum)
"""def dec_bin(n):
    if(n>1):
        dec_bin(n//2)
    print(int(n)%2,end=' ') """
n=int(input("Enter Binary Value : "))
dec_bin(n)
