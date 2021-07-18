def Palindrome(num):
    number = str(num)
    rString = number[::-1]
    reversed = int(rString)

    if reversed == num:
        return True
    else:
        return False

number = int(input('Enter a number'))
print(Palindrome(number))
