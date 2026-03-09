def sum(num1,num2):
    print(type(num1),type(num2))
    return num1+num2

def sub(num1,num2):
    return num1-num2
res = sum(15,20)
print('res = ',res,'and its type is ',type(res))

result = sum("kiran","kumar")
print(f'result is :{result}')

result = sum(5.6,8.2)
print(f'result is :{result}')