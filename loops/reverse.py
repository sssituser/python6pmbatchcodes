#Write a program to find the reverse number for the given number
# num = 345  reverse = 543
# num = 897  reverse = 798

num = int(input('Enter number : ')) #num = 345
rev = 0
while num>0: #345>0-T 34>0-T 3>0-T 0>0-F
    lastdigit = num%10 #lastdigit = 345%10  ld = 5 ld = 34%10=>4 ld = 3%10 ld = 3
    rev = rev*10+lastdigit # rev = 0+5 rev = 5  rev = 54 rev = 543
    num= num//10 # num = 345//10 num = 34//10 num = 3//10 num = 0
print(f'Reverse number is : {rev}') 