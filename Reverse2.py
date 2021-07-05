def reversDigits(num):
 
    # converting number to string
    string = str(num)
 
    # reversing the string
    string = list(string)
    string.reverse()
    string = ''.join(string)
 
    # converting string to integer
    num = int(string)
 
    # returning integer
    return num
 
# Driver code
if __name__ == "__main__":
 
    num = 4562
    print("Reverse of no. is ", reversDigits(num))