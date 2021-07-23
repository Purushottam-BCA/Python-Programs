# <Prog_No:8> <Ex_No:6> <Author: Purushottam Kumar>
# WAP to add two matrices (using nested list)..

print("\nOutput of Prog_No:8 in Ex_No:6 implemented by PURUSHOTTAM KUMAR :\n")

X = [[12,7,3],[4 ,5,6],[7 ,8,9]]
Y = [[5,8,1],[6,7,3],[4,5,9]]
Sum=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(X)):
    for j in range(len(Y)):
        Sum[i][j] = X[i][j] + Y[i][j]
print("1st Matrix : ")
for m in X:
    print(m)
print("\n2nd Matrix : ")
for m in Y:
    print(m)
print("\nSUM of MATRIX")
for m in Sum:
    print(m)


