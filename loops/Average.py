num = 5   #1+2+3+4+5/5 Average 
start = 1
end = num
sum = 0
while start<=end:
    sum = sum + start
    start = start+1
print('Sum ',sum)
print(f'Average : ',sum//num)