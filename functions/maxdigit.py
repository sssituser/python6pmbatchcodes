'''
Write a program to find the max digit of given number
num = 978   max digit = 9 
num = 354   max digit = 5
'''
# defining the function
def getmaxdigit(num): # num = 354
    max = num%10 # max = 354%10 max = 4
    while num>0: # 354>0-T 35>0-T 3>0-T 0>0-F
        digit = num%10 # digit = 354%10 digit = 4 digit = 35%10 digit = 5 digit = 3%10 digit = 3
        if digit>max: # 4>4-F 5>4-T 3>5-F
            max = digit # max = 5
        num=num//10 # num = 354//10 num = 35//10 num = 3//10 num = 0
    return max

#calling the function
print(getmaxdigit(354))
print(getmaxdigit(978))
