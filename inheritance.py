class Animal:
    def speak(self):
        print("Animal speaking")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


class Dogchild(Dog):
    def eats(self):
        print("Drinking milk")


dog = Dog()  # this is the object
dog.bark()
dog.speak()

dogmdogo = Dogchild()
dogmdogo.eats()
dogmdogo.bark()
dogmdogo.speak()
