#Write a program to check given number is +ve and single digit
num = int(input('Enter a number : '))#num = 0
if num>0: #0>0
    if num<10:
        print(f'{num} is +ve and single digit')
    else:
        print(f'{num} is +ve but not single digit')
else:
    print(f'{num} may be zero or -ve')


    #if-else - 2     2 example nested-if