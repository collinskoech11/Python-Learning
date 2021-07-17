class Family:
    def __init__(self, name, complexion):
        self.name = name
        self.complexion = complexion

class GrandKid(Family):
    def height(self):
        print('she is taller')

nem = input('enter your name: ')
complexs = input('enter your complexion')
g1 = GrandKid(nem, complexs)
print('your name is: ' + g1.nem + ' and your complexion is ' + g1.complexs)
       