num = int(input('Enter a number : '))# num = 789
copy = num # copy = 789
rev = 0
while num>0:      
    digit = num%10
    rev = rev * 10+ digit 
    num=num//10 
if copy == rev:
    print(f"{copy} is a Palindrome numbber")
else:
    print(f'{copy} is not a Palindrome.')