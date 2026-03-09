d ={}
print(d)
print(type(d))
d={1:'python',2:"java",3:"DotNet",4:"UI",5:"abc",6:"DotNet"}
print(d)
d[7]='React'
print(d)
print(d[1],d[3],d[7])
for i in d.keys():
    print(f'{i} ---> {d[i]}')
    
dt = {"first_name":"kiran","last_name":"kumar","email":"kirankj977@gmail.com"}

for i in dt.keys():
    print(f'{i}     {dt[i]}')
    
dt = {'f' :1,'d':508,'e':9000,'g':7.8,'h':True,'i':'abc','li':[98,87,67,56]}

for i in dt.keys():
    print(f'{i}   {dt[i]}')
