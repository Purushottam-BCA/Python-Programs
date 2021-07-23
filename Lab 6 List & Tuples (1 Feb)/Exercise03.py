# <Prog_No:3> <Ex_No:6> <Author: Purushottam Kumar>
# Write a program to add 2 to every value in a list using for loop.

print("\n Output of Prog_No:3 in Ex_No:6 implemented by PURUSHOTTAM KUMAR :\n")

l = [int(k) for k in input(" Enter Integer in List : ").split(' ')]
print("\n OLD LIST ELEMENT : ",l)
for i in range(len(l)):
    l[i]+=2
print("\n NEW LIST ELEMENT [+2] : ",l)
    
    


    

