# <Prog_No:1> <Ex_No:3> <Author: Purushottam Kumar>
# Write a program to find whether a given year is a leap year or not.

print("\n Output of Prog_No:1 in Ex_No:3 implemented by Purushottam Kumar :\n")
year = int(input(" Enter a Year : "))
if year%4==0:
    if(year%100 == 0 and year%400 != 0):
        print("\n",year," is not a leap year\n")
    else:
        print("\n",year," is a leap year\n")
else:
    print("\n",year," is not a leap year\n")

