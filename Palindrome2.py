def Palindrome(num):
    number = str(num)
    rString = number[::-1]
    reversed = int(rString)

    if reversed != num and reversed != int:
        return False
    else:
        return True
        

number = input('Enter a number: ')
print(Palindrome(number))
