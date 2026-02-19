#num = 5    output : 1 4 9 16 25
start = 1
end = 10
pow = int(input('Enter power : '))
while start <= end: 
    print(start**pow,end="  ")
    start = start+1
