#Write a program generate numbers for the given number
#num = 5  output : 5 4 3 2 1
#num = 10 output : 10,....1
#num = 20 output :20 18 16 14 12 10 8 6 4 2 0
#num = 5    output : 1  4  9  16  25
#num = 5     output: 5 10 15 20 .. 50
#num = 6     output: 6 12 18..  60
#num = 5    output : 1 2 3 4 5
max = int(input('Enter a number :'))
min = 1

while max >= min:# 5>=1-T 4>=1 3>=1 2>=1 1>=1 0>=1-f
    print(max,end="   ")#5  4   3  2  1
    max = max-1 # max = 4 3 2 1 0
