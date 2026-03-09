def getNextMultipleOf100(num):
    if num<=0:
        return -1
    return ((num//100)+1)*100
        



print(getNextMultipleOf100(0))
print(getNextMultipleOf100(-100))
print(getNextMultipleOf100(56))
print(getNextMultipleOf100(123))
print(getNextMultipleOf100(456))
    
    