'''
Write a program to find the factorial of given number using
recursive function num = 5   1*2*3*4*5=>120
'''
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
print(factorial(0))
print(factorial(1))
print(factorial(5))