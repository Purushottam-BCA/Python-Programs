# <Prog_No:10> <Ex_No:10> <Author: Purushottam Kumar>

print("\nOutput of Prog_No:10 in Ex_No:10 implemented by PURUSHOTTAM KUMAR :\n")

alphabet=0
number=0
symbol=0
file1 = open("H:\PkFile.txt","r")
while True: 
    char = file1.read(1)
    if not char:
        break
    if (char>='a' and char<='z')or (char>='A' and char <='Z'):
        alphabet+=1
    elif(char>='0' and char<='9'):
        number+=1
    else:
        symbol+=1
file1.close()
file2 = open("H:\\Newfile.txt","w")
file = open("H:\PkFile.txt","rt")
data = file.read()
words = data.split()
for i in words:
    ch=i+"\n"
    file2.write(i+"\n")
file.close()
file2.close()

file1 = open("H:\PkFile.txt","r")
file2 = open("H:\\Newfile.txt","r")
print("File 1 Content : ",file1.read())
print('Total Words :', len(words)," Alphabet : ",alphabet," Number : ",number," Symbol : ",symbol)
print("\nFile 2 Content : \n",file2.read())
file2.close()
file1.close() 
