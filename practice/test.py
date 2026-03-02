#Write  program to find the max digit of given number

def getMaxDigit(num): # 987
    max = num%10 # max = 987%10 max =7
    while num>0: # 987>0-T 98>0-T 9>0 0>0
        digit = num%10 #digit  = 7 digit = 8 digit = 9
        if digit>max:
            max=digit # max = 8 max = 9
        num//=10# num = 987//10 num  = 98//10 num = 9//10 num = 0
    return max
    
