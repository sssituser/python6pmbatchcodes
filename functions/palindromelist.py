'''
Write a program to generate list of palidrome number for the given range
start = 1     end = 5     11,22
start = 1 end = 100  1,2,3,4,5,6,7,8,9,11,22,33,44..99.
start = 1 end = 100
'''
def reverse(num):
    rev = 0
    while num>0:
        rev = rev*10+num%10
        num//=10
    return rev # 22

def isPalindrome(num):
    return num==reverse(num)

def palinList(start,end): # 10 ,100
    res = ''
    for i in range(start,end+1): # i = 11,12,13,22
        if isPalindrome(i): # 11 is palindrome
            res=res+str(i)+","
    return res

print(palinList(1,100))