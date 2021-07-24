class Jash:
    def __init__(self,name):
        self.name = name
    def hi(self):
        print(f"hi {self.name} ")

    def bye(self):
        print(f"bye {self.name}")
dhairya=Jash('sanju')
#if you dont put() then u need to pass a positonal parameter
# TypeError: hi() missing 1 required positional argument: 'self'

dhairya.name='jash paleja'
dhairya.hi()
dhairya.bye()
# print(dhairya.x)
