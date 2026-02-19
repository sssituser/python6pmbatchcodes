#Write a program to find the digit count of a given number
# num =345   count : 3 digits
#num = 1234  count : 4

num = int(input('Enter a number : '))
copy = num
count = 0
while num>0: 
    digit = num%10 
    count  = count+1 
    num = num//10 
print(f"{copy} has {count} Digits ")
    
    