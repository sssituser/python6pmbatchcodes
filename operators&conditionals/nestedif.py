#Write program to read 3 integers and find the max number among them.
num1 = int(input("Enter number 1 : "))#10
num2 = int(input("Enter number 2 : "))#20
num3 = int(input("Enter number 3 : "))#309

num4 = int(input('Enter number 4 : '))#40
max = num1 # max = 10
if max<num2:
    max = num2 #max = 20
if max<num3: # max = 30
    max = num3
if max<num4: # max = 40
    max = num4
print(f'{max} is max')

