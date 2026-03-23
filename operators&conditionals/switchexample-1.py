while True:
    num1 = int(input('Enter num1 : '))
    num2 = int(input('Enter num2 : '))
    choice =int(input('1.Add\n2.Sub\n3.Mul\n4.Div\nEnter Your choice: '))
    match choice:
        case 1:
            print(f'sum is :{num1+num2}')
        case 2:
            print(f'sub is : {num1-num2}')
        case 3:
            print(f'mul is : {num1*num2}')
        case 4:
            print(f'quo is : {num1//num2}')
        case _:
            print('Invlid choice!')
        
        