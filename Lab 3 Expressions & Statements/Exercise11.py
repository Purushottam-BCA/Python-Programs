# <Prog_No:11> <Ex_No:2> <Author: Purushottam Kumar>
#   Write a program to calculate the total amount of money given the denominations of
''' Rs. 1, Rs. 2, Rs. 5, Rs. 10, Rs. 20, Rs. 50, Rs. 100, Rs. 200, Rs. 500 & Rs. 2000.

( hint: Output must be

Enter the number of 1 rupees: 10
Enter the number of 2 rupees: 0
Enter the number of 5 rupees: 5
Enter the number of 10 rupees: 2
----------------------------------
Total amount is = Rs. 55 '''

print("\n Output of Prog_No:11 in Ex_No:2 implemented by Purushottam Kumar :\n")

R1=int(input(" Enter the number of 1 rupees : "))
R2=int(input(" Enter the number of 2 rupees : "))
R5=int(input(" Enter the number of 5 rupees : "))
R10=int(input(" Enter the number of 10 rupees : "))
R20=int(input(" Enter the number of 20 rupees : "))
R50=int(input(" Enter the number of 50 rupees : "))
R100=int(input(" Enter the number of 100 rupees : "))
R200=int(input(" Enter the number of 200 rupees : "))
R500=int(input(" Enter the number of 500 rupees : "))
R2000=int(input(" Enter the number of 2000 rupees : "))

Tot_amt =(R1)+(2*R2)+(5*R5)+(10*R10)+(20*R20)+(50*R50)+(100*R100)+(500*R500)+(2000*R2000)
print("\n Total amount is : "+ str(Tot_amt))
