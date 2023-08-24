# Python Class

### Superclass/Base Class/Parent Class::

A superclass, base class, or parent class is a class that serves as the foundation for other classes. It contains common attributes and methods that are shared among its subclasses. Subclasses can inherit these attributes and methods, and they can also extend or override them if needed.

### Subclass:
A subclass is a class that inherits properties and methods from its superclass. It can add additional attributes and methods or modify existing ones while reusing the functionality of the superclass. Subclasses can be thought of as specialized versions of the superclass.

##### Example

    `
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
    
#Creating instances of subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name)  # Output: Buddy
print(dog.speak())  # Output: Woof!
print(cat.name)  # Output: Whiskers
print(cat.speak())  # Output: Meow!
    `

## Special methods
Special methods in Python, also known as "magic methods" or "dunder methods" (short for "double underscore" methods), are predefined methods with specific names and double underscores at the beginning and end of their names. These methods are used to define behavior for built-in operations and operations involving objects of custom classes. Here's a list of some commonly used special methods along with their explanations:

 - `__init__(self, ...):`

The constructor method that gets called when an object is created.
Initializes the object's attributes.
- `__del__(self):`

Called when an object is about to be destroyed.
Performs cleanup operations or resource deallocation.
- `__str__(self):`

Returns a human-readable string representation of the object.
Used by the str() function and print() to display the object.
- `__repr__(self):`

Returns an "official" string representation of the object, ideally one that, if passed to eval(), would recreate the object.
Used to represent the object in interactive sessions and debugging.
- `__len__(self):`

Returns the length of the object.
Used by the len() function to obtain the length of objects like strings, lists, etc.
- `__getitem__(self, key):`

Allows indexing and slicing of objects.
Called when an item is accessed using square brackets (e.g., obj[key]).
- `__setitem__(self, key, value):`

Allows setting values using indexing.
Called when an item is assigned a value using square brackets (e.g., obj[key] = value).
- `__delitem__(self, key):`

Allows deletion of items using indexing.
Called when an item is deleted using the del statement (e.g., del obj[key]).
- `__contains__(self, item):`

Determines if an item is present in the object.
Used by the in operator (e.g., item in obj).
- `__iter__(self):`

Returns an iterator object.
Used to enable iteration over the object (e.g., in a for loop).
- `__next__(self):`

Returns the next item in the iterator.
Used in conjunction with __iter__() to define the behavior of an iterator.
- `__eq__(self, other):`

Checks for equality between two objects.
Used by the == operator.
- `__ne__(self, other):`

Checks for inequality between two objects.
Used by the != operator.
`__lt__(self, other), __le__(self, other), __gt__(self, other), __ge__(self, other):`

Comparison methods for less than, less than or equal to, greater than, and greater than or equal to operations.
Used by comparison operators (<, <=, >, >=).
- `__add__(self, other):`

Defines addition behavior for objects.
Used by the + operator.
`__sub__(self, other), __mul__(self, other), __truediv__(self, other), __floordiv__(self, other), __mod__(self, other):`

Methods for subtraction, multiplication, division (true division), floor division, and modulus operations.
Used by the -, *, /, //, and % operators, respectively.
- `__call__(self, ...):`

Allows instances of a class to be called as functions.
Useful for creating callable objects.
- `__enter__(self), __exit__(self, exc_type, exc_value, traceback):`

Used to define behavior when entering and exiting a context using the with statement.
Useful for managing resources (e.g., file handling, database connections).
These are just a subset of the many special methods available in Python. Understanding and utilizing these special methods can greatly enhance the functionality and versatility of your custom classes.