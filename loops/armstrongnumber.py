num = int(input('Enter a number : ')) # 153
copy = num # copy = 153
pow = 0
while num>0: 
    digit = num%10
    pow = pow+1 
    num=num//10 
num = copy
powersums = 0
while num>0: 
    digit = num%10 
    powersums = powersums + digit**pow 
    num=num//10 
if copy == powersums:
    print(f'{copy} is an Armstrong Number ')
else:
    print(f'{copy} is not an Armstrong Number ')
    