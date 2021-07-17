class Family:
    def __init__(self, name, complexion):
        self.name = name
        self.complexion = complexion

class GrandKid(Family):
    def height(self):
        print('she is taller')

name = input('enter your name: ')
complexion = input('enter your complexion')
g1 = GrandKid(name, complexion)

       