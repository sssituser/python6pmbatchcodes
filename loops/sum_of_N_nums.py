'''
    num=5
    Sum of 5 nums from 1+2+3+4+5 = > 15
    factorial of 5! => 1*2*3*4*5 = > 120
'''
num = 5
start = 1
end = num
sum = 0
while start<=end:# 1<=5-T 2<=5-T 3<=5-T 4<=5-T 5<=5 6<=5-F
    sum = sum + start  # sum = 1 sum = 3 sum = 6 sum = 10 sum = 15
    start = start+1  # start = 2,3,4,5,6
print("sum is : ",sum)