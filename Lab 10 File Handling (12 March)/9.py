# <Prog_No:9> <Ex_No:10> <Author: Purushottam Kumar>

print("\nOutput of Prog_No:9 in Ex_No:10 implemented by PURUSHOTTAM KUMAR :\n")

f1 = open("H:\Employee.txt","r") 
Count = 0
for line in f1:
    Count += 1
    print("Line ",Count,":",line)
print("\nTotal Lines : ",Count)
