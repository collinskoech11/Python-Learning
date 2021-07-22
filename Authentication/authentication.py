 # this is asimple login authentcation program
print('Create an acccount')
username = input('Enter your name: ')
password = input('Enter password: ')

print('Created account successfully')
print('Please login')

username1 = input('Enter username: ')
password1 = input('Enter password: ')

if username1 == username and password1 == password:
    print('Login successful')
else:
    print('Invalid credentials... try again')