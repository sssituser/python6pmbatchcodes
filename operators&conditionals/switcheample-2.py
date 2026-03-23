num1 = int(input('Enter num1 : '))
num2 = int(input('Enter num2 : '))
choice = input('ADD\nSUB\nMUL\nDIV\nEnter Your choice : ')
match choice:
    case "ADD" | "add" | "Add":
        print(f'sum is : {num1+num2}')
    case "SUB" | "sub" | "Sub":
        print(f'sub is : {num1-num2}')
    case "MUL" | "mul" | "Mul":
        print(f'mul is : {num1*num2}')
    case "DIV"|"div"|"Div":
        print(f'Quo is : {num1/num2}')
    case _: 
        print('Invalid choice...')       
        