li =[ [11,22,33],[10,20,30], [44,55,66]]
print("==============Matrix Elements==============")
for i in range(0,len(li)):
    for j in range(0,len(li[i])):
        print(f'{li[i][j]}',end="\t")
    print("\n")
print("==============Matrix Diagonal  Elements==============")
for i in range(0,len(li)):
    for j in range(0,len(li[i])):
       if i==j or i+j == 2:
            print(f'{li[i][j]}',end="\t")
       else:
           print(end="\t")
    print("\n")
print("==============Matrix other than Diagonal  Elements==============")
for i in range(0,len(li)):
    for j in range(0,len(li[i])):
       if i==j or i+j == 2:
            print(end="\t")
       else:
           print(f'{li[i][j]}',end="\t")
    print("\n")