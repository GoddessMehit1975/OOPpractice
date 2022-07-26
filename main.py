class Dog(object):
    kind = "canine"

    def __init__(self, name, age, breed):
        self.breed = breed
        self.name = name
        self.age = age
        print("This is", self.name, "a", self.breed, "and they are", self.age, "years old")

    def noise(self):
        print(self.name, "says 'bark'")

    def sage(self):
        print("")
        print(self.name, "says Bark Bark Bark which means 'Hi Katy'")

    def persephone(self):
        print("")
        print(self.name, "says Bark Bark Bark which means 'Hi Julie'" )

pet1 = Dog("Persephone", 2, "Pitbull")
pet2 = Dog("Hector", 6, "Cocker Spaniel")
pet3 = Dog("Betty", 10, "Malamute")
pet4 = Dog("Sage", 13, "Miniature Schnauzer")
pet4.sage()
pet1.persephone()
print()
