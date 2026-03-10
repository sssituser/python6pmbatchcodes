'''
write a program to find the frequency of the given name
'abbccaa'
a - 3
b - 2
c - 2
arun   a - 1 n - 1 r - 1 u -1
'''
def frequency(name): #"abac"
    name = name.lower()
    di = dict({}) # empty
    for i in name:        #abac
        if di.__contains__(i):
            val = di[i]
            di[i]=val+1
        else:
            di[i]=1
    return di    
        
        
print(frequency('arunkumar'))
print(frequency('kiran'))
print(frequency('reddy'))
print(frequency('kala'))
        
    

    
    
    
        
        
        
    
