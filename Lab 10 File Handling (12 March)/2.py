# <Prog_No:2> <Ex_No:10> <Author: Purushottam Kumar>

print("\n Output of Prog_No:2 in Ex_No:10 implemented by PURUSHOTTAM KUMAR :\n")

f2 = open("H:\PkFile.txt","r")
data = f2.readlines()
print("<---- All Lines ----->\n")
for line in data:
    print("Line : ",line)
f2.close()
print("<----- Lines with 'THE' ------>\n")
f2 = open("H:\PkFile.txt","r")
for line in data:
    if 'the' in line:
        print("Line : ",line)
f2.close()
