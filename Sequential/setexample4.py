a = {8,"kiran",9.8,True}
li =["arun",7+10j,False]
print(a)
a.update(li)
print(a)

a = {1,2,3,4}
b = {4,3,"raj"}
c = a.difference(b)
print('c set : ',c)
print(a)
print("b= ",b)
d = b.copy()
print("d : ",d)