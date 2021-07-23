f2 = open("H:\\Newfile.txt","r+")
data1 = f2.read()
data2 = data1[::-1]
f2.close()
print("File 2 Data : \n",data1)

