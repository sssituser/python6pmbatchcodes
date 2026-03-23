def reverse(num): # 123
    rev = 0
    while num>0: # 123>0 12>0 1>0 0>0
        rev = rev*10+num%10 # 0*10+3 = rev = 30+2 rev = 320+1= rev = 321
        num=num//10#num = 123//10 num = 12//10 num = 1//10 num = 0
    return rev

def isPlindrome(num):
    return num == reverse(num)

print(isPlindrome(121))