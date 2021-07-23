nm=input("Enter Name : ")
roll=int(input("ENter Roll Number : "))
if(len(str(roll))==5):
    s1=float(input("Enter marks of subject 1 : "))
    s2=float(input("Enter marks of subject 2 : "))
    s3=float(input("Enter marks of subject 3 : "))
    s4=float(input("Enter marks of subject 4 : "))
    s5=float(input("Enter marks of subject 5 : "))
    avg=(s1+s2+s3+s4+s5)/5
    print("\nRoll_No : ",roll,"\tName : ",nm,"\t Percentage : %.2f"%avg)
