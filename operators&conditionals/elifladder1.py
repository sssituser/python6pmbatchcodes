sub1 = int(input('Enter s1 marks : '))
sub2 = int(input('Enter s2 marks : '))
sub3 = int(input('Enter s3 marks : '))
total = sub1+sub2+sub3
per  = (total/300)*100
if per>=70:
    print(f'Student got passed in  Distinction with Percenage of  {per}')
elif per>=60:
    print(f'Student got passed in  First with Percenage of  {per}')
elif per>=50:
    print(f'Student got passed in  Second Dvision with Percenage of  {per}')
elif per>=40:
    print(f'Student Passed In Third divsion with  a percenttage o {per}')
else:
    print("Stuent Failed..")