# <Prog_No:7> <Ex_No:2> <Author: Purushottam Kumar>
# Write a program to calculate SIMPLE  INTEREST & COMPOUND  INTEREST.

print("\n Output of Prog_No:7 in Ex_No:2 implemented by Purushottam Kumar :\n")

P=float(input(" Enter Principal (P) : "))
R=float(input(" Enter Rate% per annum (R) : "))
T=float(input(" Enter Time (in years) (T) : "))
Simple =(P*R*T)/100
Compound=P*(((1+R/100)**T)-1)
print("\n Principal : "+ str(P) + "\n Rate : "+str(R) + "\n Time : "+str(T))
print("\n Simple Interest : "+ str(Simple) + "\n Compound Interest : "+ str(Compound))
