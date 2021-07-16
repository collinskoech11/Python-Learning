def Reverse(num):
    number = str(num)
    reversing = number[::-1]
    reversed = int(reversing)
    print(reversed)

num = input('enter a number: ')
Reverse(num)