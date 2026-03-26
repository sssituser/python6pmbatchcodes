while True:
    try:
        num1 = int(input('Enter num1 : '))
        num2 = int(input('Enter num2 : '))
        print('num1 = ',num1,"num = ",num2)
        if num2 == 0:
            raise ZeroDivisionError("Hi I check num2 is zero")
        print(f'Quo : {num1//num2}')
    except ValueError:
        print("Enter only Integers")
    except ZeroDivisionError as zx:
        print(f"num2 can't be zero : {zx}")
    except Exception as ex:
        print(f"Error : {ex}")
    