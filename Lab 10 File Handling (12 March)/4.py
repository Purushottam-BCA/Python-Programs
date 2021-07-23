# <Prog_No:4> <Ex_No:10> <Author: Purushottam Kumar>

print("\nOutput of Prog_No:4 in Ex_No:10 implemented by PURUSHOTTAM KUMAR :\n")

f1 = open("H:\PkFile.txt", "r")   
f2 = open("H:\File1.txt", "r")   
i = 0
for line1 in f1: 
    i = i + 1
    for line2 in f2: 
        if line1 == line2:   
            print("Line ", i, ": SAME")        
        else: 
            print("Line ", i, ": NOT SAME") 
            print("\tFile 1:", line1, end='') 
            print("\tFile 2:", line2, end='') 
        break
f1.close()                                        
f2.close()


