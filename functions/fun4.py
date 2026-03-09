def getSumOfTwoDigits(num):
    if num<0:
        return -3
    if num>99:
        return -2
    if num>=0 and num<=9:
        return -1
    return num%10+num//10
print(getSumOfTwoDigits(-25))   #  -3
print(getSumOfTwoDigits(200))   #  -2
print(getSumOfTwoDigits(7))     # -1
print(getSumOfTwoDigits(11))    #  2
print(getSumOfTwoDigits(45))    #  9
print(getSumOfTwoDigits(72))    #  

    