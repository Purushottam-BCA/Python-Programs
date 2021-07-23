# <Prog_No:7> <Ex_No:6> <Author: Purushottam Kumar>
# WAP to remove all duplicates from a list.

print("\n Output of Prog_No:7 in Ex_No:6 implemented by PURUSHOTTAM KUMAR :\n")

List = [d for d in input(" ENTER VALUE SEPERATED BY COMMA : ").split(',')]
print("\n LIST WITH DUPLICATE ", List)
temp= []
for i in List:
    if i not in temp:
        temp.append(i)
List = temp[::]  #Moving DISTINCT NUMBERS ONLY
del temp     #Deleting Temperory List
print("\n LIST AFTER REMOVING DUPLICATES : ", List)

