#Write program to generate number from the given number
# num = 10
# 3 6 9 12 15 18 21 24  27  30
start = 1
end = 10
while start<=end: # 1 <= 10 2<=10-T 3<=10-T 4<=10 10<=10-T 11<=10-F
    print(start*3,end="  ") # 3 6 9...30
    start = start + 1 # start = 2,3,4,, 10, 11


