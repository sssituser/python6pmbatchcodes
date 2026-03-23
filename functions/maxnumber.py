'''
 numlist =[112,100,321,423,678,987]
            [2,1,3,4,8,9]
            [1,0,1,2,6,7]
            011267=>11267
 984321
 //123489
 solution:
 1.numlist =[112,100,321,423,678,987]
 2.getmaxdigitlist[2,1,3,4,8,9]
 3.sortllistindesc[9,8,4,3,2,1]
 4.convertlisttonum = 984321
 
'''
def getmaxdigit(num):
    max = num%10
    while num>0:
        digit = num%10
        if digit>max:
            max=digit
        num=num//10
    return max
def getmaxdigitlist(li): # li = [112,100,321,423,678,987]
    mxdigitlist=[]
    for element in li:
        mxdigitlist.append(getmaxdigit(element))
    return mxdigitlist

def sortlistindesc(li): #[2,1,3,4,8,9]
    li.sort()
    li.reverse()
    return li
def convertlisttonum(li):
    res = 0
    for num in li:
        res = res*10+num
    return res
    
def getmaxnumber(li):
    return convertlisttonum(sortlistindesc(getmaxdigitlist(li)))

li = [112,100,321,423,678,987]
print(getmaxnumber(li))