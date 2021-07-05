def reversNumber(num):

    #converting to string
    string = int(num)

    #reversing the string
    string = list(string)
    string.reverse()
    string = ''.join(string)

    #coverting to s
    num = int(string)