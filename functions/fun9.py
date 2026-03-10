'''
Write  a program to find the lucknumber of a
given date of birth.
'1-jan-2000'   month must be characters and min 3 letters mandate
 '2-Apr-1998'    
 lucknumber = 1+1+2000  lucky number 2002
 lucky number = 2+4+1998 => 2004 => 2+0+0+4 => 6 lucky number
'''
def convertMonthTextToNum(month): #"Jan"
    month = month.lower()
    months =['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    for i in range(0,months.__len__()):
       if month.__contains__(months[i]):
           return i+1
    return 0
def getDigitsSum(num): # 123
    sum = 0
    while num>0: # 123>0 12>0 1>0 0>0
        sum +=num%10 # sum = 3 sum = 5 sum = 6
        num//=10 # num = 123//10 num = 12//10 num = 1//10 num = 0
    return sum

def getLuckyNumber(dob):
    li = dob.split('-')
    date = int(li[0])
    month = convertMonthTextToNum(li[1])
    year = int(li[2])
    sum = date+month+year
    while(sum>9):
       sum = getDigitsSum(sum)
    return sum

print(getLuckyNumber('24-sep-2004'))
