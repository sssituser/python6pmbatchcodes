from palindromelist import *

def allNums(start,end):
    ams=""
    palins=""
    adms=""
    for i in range(start,end+1):
        if isPalindrome(i):
            palins+=str(i)+","
        if isArmstrong(i):
            ams+=str(i)+"."
        if isAdam(i):
            adms+=str(i)+","
    return "Palindrom list : "+palins[:palins.__len__()-1]+"."+"\nAdamsList : "+adms[:adms.__len__()-1]+"."+"\nAmstrongs : "+ams[:ams.__len__()-1]+"."

print(allNums(1,1000))