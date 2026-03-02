def isAdam(num):
    return square(num)==reverse(square(reverse(num)))

def square(num):
    return num*num;
def reverse(num):
    rev = 0
    while num>0:
        rev =rev*10+num%10
        num//=10
    return rev

