# <Prog_No:8> <Ex_No:2> <Author: Purushottam Kumar>
# Write a program to calculate area of circle and triangle.

print("\n Output of Prog_No:8 in Ex_No:2 implemented by Purushottam Kumar :\n")

radius=float(input(" Enter radius of circle ('r') : "))
area_circle = 22/7 * (radius**2);
print("\n Area of Circle (radius = "+ str(radius) + " ) is "+ str(area_circle)+" sq. unit")
s1=int(input("\n Enter 1st side of triangle ('a') : "))
s2=int(input("\n Enter 2nd side of triangle ('b') : "))
s3=int(input("\n Enter 3rd side of triangle ('c') : "))
s_peri = (s1+s2+s3)/2
area_triangle=(s_peri*(s_peri-s1)*(s_peri-s2)*(s_peri-s3))**0.5
print("\n Area of triangle is " + str(area_triangle)+" sq. unit")
