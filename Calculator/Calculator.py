#this is a simple calculator
num1 = int(input('Enter the first number: '))
op = input('Enter operator: ')
num2 = int(input('Enter the second number: '))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(abs(num1 / num2))
else:
    print()