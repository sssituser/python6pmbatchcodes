d={1:'python',2:"java",7:"DotNet",4:"UI",3:"abc",6:"DotNet"}
print(d)
d.setdefault(10,'php')
d[11]='html'
print(d)
print(f'deleted key value is : {d.popitem()}')
print(f'deleted key and value is :{d.pop(1)}')
print(d)
d.clear()
print(d)