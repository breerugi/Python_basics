# Inheritance: By defining a common base class,
# you can use polymorphism to treat objects of
# derived classes as instances of the base class.
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

shapes = [Circle(18), Square(24)]

for shape in shapes:
    print(f"Area: {shape.area()}")

# Duck Typing: Python uses dynamic typing, which means that it determines the
# type of an object at runtime. If an object behaves like a certain type, it
# is considered an instance of that type, regardless of its actual class.

class Parrot:
    def speak(self):
        return "Polly wants a cracker!"

class Car:
    def drive(self):
        return "Vroom! Vroom!"

def describe_entity(entity):
    if hasattr(entity, 'speak'):
        print(entity.speak())
    elif hasattr(entity, 'drive'):
        print(entity.drive())

polly = Parrot()
tesla = Car()

describe_entity(polly)  # Output: Polly wants a cracker!
describe_entity(tesla)  # Output: Vroom! Vroom!



#Method Overriding: This is also known as runtime polymorphism. In Python,
# you can define a method in a subclass with the same name as a method in
# its base class. When you call the method on an object, Python will determine
# which method to execute based on the object's actual class.

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!

