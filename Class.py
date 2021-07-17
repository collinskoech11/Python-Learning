class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

fistname = input('enter first name: ')
lastname = input('enter last name: ')
p1 = Person(fistname, lastname)
print('the first name is '+ p1.firstname + 'and the last name is ' + p1.lastname)

        