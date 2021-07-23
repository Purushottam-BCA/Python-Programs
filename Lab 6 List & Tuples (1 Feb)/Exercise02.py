# <Prog_No:2> <Ex_No:6> <Author: Purushottam Kumar>
# Write a program to print the elements in a list using an iterator.

print("\n Output of Prog_No:2 in Ex_No:6 implemented by PURUSHOTTAM KUMAR :\n")

a = [n for n in input(" Enter elements in the list : ").split(',')]
print("\n List eLements are : ",end='')
for i in a:
    print(i,end=' ')
