
class Dog:
    attr1 = "mammal"
    def __init__(self, name):
        self.name = name
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))




print("\n classes and objects")
class Dog:
    attr1 = "mammal"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("My name is {}".format(self.name))
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
Rodger.speak()
Tommy.speak()

