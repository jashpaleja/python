class Jash:
    def __init__(self,age,pointer):
        self.age=age
        self.pointer=pointer


    def hi(self):
        print("hi jash paleja")


    def bye(self):
        print("bye jash paleja")


jash=Jash(20,10)
jash.age=19
print(jash.age)
print(jash.pointer)