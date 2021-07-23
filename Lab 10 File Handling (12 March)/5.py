# <Prog_No:5> <Ex_No:10> <Author: Purushottam Kumar>

print("\n Output of Prog_No:5 in Ex_No:10 implemented by PURUSHOTTAM KUMAR :\n")

file1 = open("H:\PkFile.txt","r")
file2 = open("H:\\Newfile.txt","w+")
print("<----- BEFORE COPY ----->")
print("File 1 : \n",file1.read())
print("File 2 : \n",file2.read())
file1 = open("H:\PkFile.txt","r")
file2 = open("H:\\Newfile.txt","a")
while True: 
    char = file1.read(1)           
    if char:  
        file2.write(char)
    else:
        break
print("<----- AFTER COPY ----->")
file1 = open("H:\PkFile.txt","r")
file2 = open("H:\\Newfile.txt","r")
print("File 1 : \n",file1.read())
print("File 2 : \n",file2.read())
file2.close()
file1.close() 
