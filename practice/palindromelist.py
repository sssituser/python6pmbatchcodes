# write a program to genreate palindromes for the give start and end
#1,2,3,4,5,6,7,8,9,11,22,33....99.

from palindrome import *
from armstrong import *
from adamnum import *
def palindromesList(start,end):
    res = ""
    for i in range(start,end+1):
        if isPalindrome(i):
            res = res+str(i)+","
    return res[0:res.__len__()-1]+"."

def amsList(start,end):
    res=""
    for i in range(start,end+1):
        if isArmstrong(i):
            res += str(i)+","
    return res[0:res.__len__()-1]+"."


def admList(start,end):
    res = ""
    for i in range(start,end+1):
        if isAdam(i):
            res +=str(i)+","
    return res[:res.__len__()-1]+"."

           


        
        
    