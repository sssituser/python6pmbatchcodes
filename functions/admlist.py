'''
write program to generate adams list for the given range
'''

from adamnumber import isAdam


def adamList(start,end):
    res = ''
    for i in range(start,end+1):
        if isAdam(i):
            res = res + str(i)+","
    return res
print(adamList(1,100))