#Develop Console application which can find the maxdigit from the given number
num = int(input('Enter a number : ')) # num = 321
max = num%10 # 321%10 max = 1
while num!=0: # 321!=0-T 32!=0 3!=0 0!=0-F
    digit = num%10 # digit = 321%10 digit = 1 digit = 32%10 digit = 2 digit = 3%10 digit = 3
    if digit>max: # 1>1-F 2>1-T 3>2-T
        max = digit # max = 2 max = 3
    num = num//10 # num = 321//10 num= 32//10 num = 3//10 num = 0
print(f'max digit is :{max}')
        