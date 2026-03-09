li = [8,11,3,'kiran',11]

fs =frozenset(li) # frozen set create by using list
print(fs)
t =(5,6,"abc",7.8)
fs1 = frozenset(t) #frozenset with tuple
fs =frozenset([8,11,3,'kiran',11])
print(fs)

fs1 = frozenset((5,6,"abc",7.8))

print(fs1)

print(dir(fs1))
fs1.add(10)