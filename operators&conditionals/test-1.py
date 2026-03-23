import copy

list1 = [[1,2,3],[4,5,6]]
list2 = copy.deepcopy(list1)   # Shallow copy

list2[0][0] = 100

print(list1)
print(list2)