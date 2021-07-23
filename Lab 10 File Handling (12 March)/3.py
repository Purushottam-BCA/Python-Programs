# <Prog_No:3> <Ex_No:10> <Author: Purushottam Kumar>

print("\n Output of Prog_No:3 in Ex_No:10 implemented by PURUSHOTTAM KUMAR :\n")

file=open("H:\PkFile.txt","r")
file2=open("H:\\Newfile.txt","w")
for line in file.read():
    file2.write(line[2:])
file2.close()
file.close()
file=open("H:\PkFile.txt","r")
print("File 1 \n",file.read())
file2=open("H:\\Newfile.txt","r")
print("File 2 ",file.read())
file.close()
file2.close()
