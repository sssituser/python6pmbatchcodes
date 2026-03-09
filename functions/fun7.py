#Write a program to find the encrypyt the name
#Example name = "abc"   result = "zyx"

def encrypt(text): # abc
    alphas = "abcdefghijklmnopqrstuvwxyz"
    ralphas = "zyxwvutsrpqonmlkjihgfedcba";
    res = ''
    for ch in text:
        res+=ralphas.__getitem__(alphas.index(ch))
    return res
print(encrypt('kala'))
    
    
    