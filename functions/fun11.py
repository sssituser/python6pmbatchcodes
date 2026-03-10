'''
    Write program to check given input is palindrome
    input = 123     rev = 321 Not Plindrome input
    input = 121     rev = 121 given input is a Palindrome input
'''



def isPalindrome(input):
    input=str(input)
    if input == input[::-1]:
        return f'{input} is a Palindrome'
    else:
        return f'{input} is not a Palindrome'

print(isPalindrome(121))
print(isPalindrome('abc'))
print(isPalindrome(123))
print(isPalindrome('madam'))