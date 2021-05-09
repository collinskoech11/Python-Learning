class animal:
    def __init__(self, animal1, animal2):
        self.animal1 = animal1
        self.animal2 = animal2

spec = animal("cat", "dog")
print(spec.animal)