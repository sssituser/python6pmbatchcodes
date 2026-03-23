
'''
num = 12      rev = 21
numsq=144     revsq = 441
              rev = 144


'''
def reverse(num):
    rev = 0
    while  num>0:
        rev = rev *10+num%10
        num = num//10
    return rev
def square(num):
    return num*num

def isAdam(num): # num = 12
    return square(num) == reverse(square(reverse(num)))

print(isAdam(11))
print(isAdam(12))
print(isAdam(13))
print(isAdam(14))