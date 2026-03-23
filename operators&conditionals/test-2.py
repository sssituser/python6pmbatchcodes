li1 = [[10,11,12],[13,4,15]]
li2 =[[1,2,3],[4,5,6]]
print('matrix-1')
for i in range(0,len(li1)):
    for j in range(0, len(li1[i])):
        print(f'{li1[i][j]+li2[i][j]}',end="\t")
    print()
print('matrix-2------------------------------------')
for i in range(0,len(li2)):
    for j in li2[i]:
        print(f'{j}',end="\t")
    print()