'''
write a program to find the sum of the n numbers
example: num = 5     sum = 1+2+3+4+5 => sum = 15
The function calling its own function can be called recursive function
'''

def sum(num):
    if num==0: 
        return 0
    else:
        return num+sum(num-1)

#1. sum(5)  => return 5+sum(4) retturn 5+10
#2. sum(4) => retrun 4+sum(3) return 4+6=>10
#3. sum(3)=> return 3+sum(2) retrun 3+3 => 6
#4. sum(2)=> return 2+sum(1)=>sum(2) return 3
#5. sum(1)=>return 1+0=>