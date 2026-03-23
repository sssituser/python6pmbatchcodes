li =[1,3,4,5,6,7,8,10]

evens=[x for x in li if x%2==0]
print(li)
print(evens)
odds = [x for x in li if x%2!=0]
print(odds)

squares =[ {x:x*x} for x in li]

print(squares)