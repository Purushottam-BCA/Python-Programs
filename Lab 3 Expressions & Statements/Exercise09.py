# <Prog_No:9> <Ex_No:2> <Author: Purushottam Kumar>
# Write a program to calculate the distance between two points.

print("\n Output of Prog_No:9 in Ex_No:2 implemented by Purushottam Kumar :\n")

x1=int(input(" Enter x-cordinate of first point (A) : "))
y1=int(input(" Enter y-cordinate of first point (A) : "))
print("\n First Point is A("+ str(x1)+","+str(y1)+")\n")
x2=int(input(" Enter x-cordinate of second point (B) : "))
y2=int(input(" Enter y-cordinate of second point (B) : "))
print("\n Second Point is B("+ str(x2)+","+str(y2)+")")

distance=((x2-x1)**2 + (y2-y1)**2)**0.5
print("\n Distance between points A("+ str(x1) +","+str(y1)+") & B("+ str(x2) +","+str(y2)+") = "+ str(distance))
