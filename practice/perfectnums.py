def isPerfect(num):
    return num==factorsSum(num)

def factorsSum(num):
    sum = 0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return sum
print(isPerfect(6))
print(isPerfect(28))
print(isPerfect(12))
