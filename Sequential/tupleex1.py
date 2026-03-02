t =(36,23,56,12,45,45,True,"kiran")
print(t)

print('Displaying the elements of tuple using  for loop')

for i in t:
    print(i,end=" ")
print('Displaying the elements using range function with +ve index')

for i in range(0,t.__len__()):
    print(f'index - {i} --- > {t[i]}')
    
print('Displaying the elements using range function with -ve index')
for i in range(-1,-t.__len__(),-1):
   print(f'index - {i} element -> {t[i]}')