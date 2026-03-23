import copy
li1=[[98,89,45],[43,67,88]]
li2 = copy.copy(li1)#shallow copy
li2[0][0] = 100
print(li1)
print(li2)

list1=[[1,2,3],[5,5,6]]
list2 = copy.deepcopy(li1)#deepcopy
list2[0][0] = 100
print(list1)
print(list2)



