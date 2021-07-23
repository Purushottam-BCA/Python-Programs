# <Prog_No:6> <Ex_No:10> <Author: Purushottam Kumar>

print("\n Output of Prog_No:6 in Ex_No:10 implemented by PURUSHOTTAM KUMAR :\n")

file1=open("H:\PkFile.txt","r+")
ch=input("Enter Student Name : ")
file1.write("Name : "+ ch)
ch=input("Enter Class : ")
file1.write("\nClass : "+ ch)
ch=input("Enter Roll : ")
file1.write("\nRoll no : "+ch)
ch=input("Total marks : ")
file1.write("\nTotal Marks : "+ch)
ch=input("Obtained Marks : ")
file1.write("\nObtained Marks : "+ch)
file1.close()
file1=open("H:\PkFile.txt","r")
print(file1.readlines())
