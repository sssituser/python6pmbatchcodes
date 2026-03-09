f1 = frozenset([12,34,56,78])
f2 = frozenset([12,45,66,78])
# f3 = f1.union(f2)
# print(f3)
# f4 = f1.intersection(f2)
# print(f4)
f3 = f1|f2 # union
print("f3 = ",f3)
f4 = f1 & f2
print("f4 = ",f4)

f5 = f1-f2   #f1.difference(f2) 
print(f5)
f6 = f1.symmetric_difference(f2)
print('f6 = ',f6)
