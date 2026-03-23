A=[ [11,22,33],[10,20,30], [44,55,66]]
B=[ [1,2,3],[4,5,6], [7,8,9]]
print("================A matrix elements are==================")
for i in range(0,len(A)):
    for j in range(0,len(A[i])):
        print(f'{A[i][j]}',end="\t")
    print("\n")
print("================B matrix elements are==================")
for i in range(0,len(B)):
    for j in range(0,len(B[i])):
        print(f'{B[i][j]}',end="\t")
    print("\n")
print("================Sum of A and B matrix elements are==================")
for i in range(0,len(B)):
    for j in range(0,len(B[i])):
        print(f'{A[i][j]+B[i][j]}',end="\t")
    print("\n")
print("================Sum of A and B matrix elements are==================")
for i in range(0,len(B)):
    for j in range(0,len(B[i])):
        print(f'{A[i][j]-B[i][j]}',end="\t")
    print("\n")