# Python Class

### Superclass/Base Class/Parent Class::

A superclass, base class, or parent class is a class that serves as the foundation for other classes. It contains common attributes and methods that are shared among its subclasses. Subclasses can inherit these attributes and methods, and they can also extend or override them if needed.

### Subclass:
A subclass is a class that inherits properties and methods from its superclass. It can add additional attributes and methods or modify existing ones while reusing the functionality of the superclass. Subclasses can be thought of as specialized versions of the superclass.

##### Example

    ``
 class Animals:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Wolf!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating instances of subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name)  # Output: Buddy
print(dog.speak())  # Output: Woof!
print(cat.name)  # Output: Whiskers
print(cat.speak())  # Output: Meow!
    ``
