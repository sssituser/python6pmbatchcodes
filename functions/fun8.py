'''
    Write a program to check find namescore of a
    given name.
    
    name ="abc"   result = 1+2+3 =>6
    name ="aza"   result = 1+26+1 =>28
'''
def namescore(name):#abc
    alphas = "abcdefghijklmnopqrstuvwxyz"
    name = name.lower()
    sum = 0
    for ch in name: 
        sum =sum + alphas.index(ch)+1  # sum = 3
    return sum


print(namescore('arunkumar'))
        