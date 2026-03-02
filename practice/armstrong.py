# 153    => sum = 1cube+5cube+3cube
#1634    => sum =1pow4 + 6pow4+3pow4+4 pow4

def isArmstrong(num):  # 1634
    copy = num  # copy = 1634
    pow = digitCount(num) # pow = 4
    sum = 0
    while num>0: # 1634>0-T 163>0-T 16>0-T 1>0 0>0
        digit = num%10 # digit =4 digit = 3 digit = 6 digit = 1
        sum = sum + digit**pow # 4pow4 + 3pow4 + 6pow4 + 1pow4
        num//=10 # num =163 num =16 num = 1 num = 0
    return copy==sum
def digitCount(num):
    count = 0
    while num!=0: # 1632!=0-T 163!=0-T 16!=0 1!=0 0!=0-F
        count +=1 # count = 1 count = 2 count =3 count =4
        num//=10 # num = 163 num = 16 num =1 num = 0
    return count
