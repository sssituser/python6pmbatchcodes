dt = {'f' :1,'d':508,'e':9000,'g':7.8,'h':True,'i':'abc','li':[98,87,67,56]}

for i in dt.keys():
    print(i)

for i in dt.values():
    print(i)

for i in dt.keys():
    print(f'{i}    {dt[i]}')