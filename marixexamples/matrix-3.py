A = [[10,11,12], # 0 0 => 10  0 1 = 11  0 2 = 12
     [70,20,30],# 1 0 => 70   1 1 = 20  1,2 = 30
     [40,50,60] # 2 , 0=>40   2,1 = 50  2,2 =60
    ]

for i in range(0,len(A)):
    for j in range(0,len(A[i])):
        print(f'{A[i][j]}',end="\t")
    print("\n")
    
print("Diagonal elements in the matrix")

for i in range(0,len(A)): # i = 0   i = 1  i = 2
    for j in range(0,len(A[i])): # j = 0  1  2
        if i==j or i+j ==2:
            print(f'{A[i][j]}',end="\t")
        else:
            print(end="\t")
    print("\n")