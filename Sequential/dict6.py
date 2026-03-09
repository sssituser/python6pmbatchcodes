d={1:'python',2:"java",7:"DotNet",4:"UI",3:"abc",6:"DotNet"}
print(d[1])
print(d.get(2))

r = d.copy()
print(r)
print(d)
data = {
    frozenset([1,2]): "Group A",
    frozenset([3,4]): "Group B"
}

print(data)