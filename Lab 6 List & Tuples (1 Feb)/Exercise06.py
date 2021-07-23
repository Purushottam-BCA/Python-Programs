# <Prog_No:6> <Ex_No:6> <Author: Purushottam Kumar>
# WAP to create a list of numbers in the range 1 to 10.
# Then delete all the even numbers from the list and print the final list.

print("\n Output of Prog_No:5 in Ex_No:6 implemented by PURUSHOTTAM KUMAR :\n")

L = [1,2,3,4,5,6,7,8,9,10]
print("\n LIST BEFORE DELETION : ",L)
for i in L:
    if(i & 1==0): # if True then Odd else Even
        L.remove(i)
print("\n LIST AFTER DELETION : ",L)        
