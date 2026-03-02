num = int(input("Enter a number  :")) # num = 5
start = 1
end = num

for i in range(start,end+1,1):
    print("=============== i = ",i,"================")
    for j in range(1,11,1):
        print(f'{i} x {j} = {i*j}')
        