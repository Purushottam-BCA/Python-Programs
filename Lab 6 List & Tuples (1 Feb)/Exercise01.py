# <Prog_No:1> <Ex_No:6> <Author: Purushottam Kumar>
# Write a Program to find the sum and mean of elements in a list.

print("\n Output of Prog_No:1 in Ex_No:6 implemented by PURUSHOTTAM KUMAR :\n")
total=0
l=[int(e) for e in input(" ENTER INTEGER SEPERATED BY COMMA : ").split(',')]
for i in l:
    total+=i
mean=total/len(l)

print("\n Sum of List element : ",l," : ",total)
print(" Mean of List element : ",l," : ",mean)


