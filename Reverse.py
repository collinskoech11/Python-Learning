def reversNumber(num):

    #converting to string
    string = int(num)

    #reversing the string
    string = list(string)
    string.reverse()
    string = ''.join(string)

    #coverting to integer
    num = int(string)

    #returning integer
    return num

    #driver code
    if __name__ == '__main__':
        num = input('enter a number: ')

        print()
