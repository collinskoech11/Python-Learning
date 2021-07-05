def reverseNum(num):
    #converting to string
    string = str(num)

    #reversing the string
    string = list(string)
    string.reverse()
    string = ''.join(string)

    #converting string to integer
    num = int(string)

    #returning the integer
    
    print(num) 

    #driver code
    if __name__ == '__main__':

        num = input('enter a number')
        print(reverseNum(num))

