year = int(input(" Enter a Year : "))
if year%4==0:
    if(year%100 == 0 and year%400 != 0):
        print("\n",year," is not a leap year\n")
    else:
        print("\n",year," is a leap year\n")
else:
    print("\n",year," is not a leap year\n")
