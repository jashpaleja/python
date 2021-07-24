class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    print("cat")
    #def walk(self):
        #print("walk")

doggie = Dog()
cat=Cat()
cat.walk()
doggie.walk()