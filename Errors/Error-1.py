while True:
    try:
        num1  = int(input('Enter num 1 : '))
        num2  =  int(input('Enter num2 : '))
        print('sum is ',num1+num2)
        if num1>=0 and num2>=0:
            print('Welcome to python Training')
            print(f'Quo : {num1//num2}')
    except ValueError:
        print('Enter only numbers with out decimal values')
    except ZeroDivisionError:
        print("num2 can't be zero")
        