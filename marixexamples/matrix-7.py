a = [[1,2],
     [3,4]
    ]
b = [
    [5,6],
    [7,8]
    ]
c = [[0,0],[0,0]]

print("A matrix elements are")
for i in range(0,2):
    for j in range(0,2):
        print(a[i][j],end="\t")
    print("\n")
print("B matrix elements are")
for i in range(0,2):
    for j in range(0,2):
        print(b[i][j],end="\t")
    print("\n")
       
##login for multiplication     
for i in range(0,2):    # i = 0 i = 1
    for j in range(0,2): # j = 0 j = 1
        for k in range(0,2): # k = 0 k =1
            c[i][j] = a[i][k]*b[k][j]+c[i][j]
print("Product of A and B matrix elements are") # c[0][0] = 19 c[0][1] = 22
for i in range(0,2):
    for j in range(0,2):
        print(c[i][j],end="\t")
    print("\n")