def Reverse(num):
    number = str(num)
    reversing = number[::-1]
    reversed = int(reversing)
    return reversed

number = input('enter a number: ')
Reverse(number)