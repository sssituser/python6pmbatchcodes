num1 = int(input('Enter num1 : '))
num2 = int(input('Enter num2 : '))
choice = input('+ ADD  - SUB  * MUL  //  Div  % Rem /nEnter Your choice : ')
match choice:
    case "+":
        print(f'sum : {num1+num2}')
    case "-":
        print(f'sub : {num1-num2}')
    case "*":
        print(f'mul : {num1*num2}')
    case "//":
        print(f'Quo : {num1//num2}')
    case "%":
        print(f'Rem : {num1%num2}')
    case _:
        print("Invalid choice.....")
print('Operation completed')