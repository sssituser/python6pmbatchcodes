while num !=0: 
    digit = num%10 
    sum = sum + digit 
    num = num//10 
print(f'sum of the digits : {sum}')