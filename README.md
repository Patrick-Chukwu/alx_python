# alx_python
A repository of Python projects for the ALX Software Engineering programme.


### Import:
The import statement in Python is used to bring external modules or packages into your current code file. It allows you to use functionality from those modules within your program.
Example:

`import math

result = math.sqrt(25)
print(result)  # Output: 5.0
`

### Exception
Exceptions are events that occur during the execution of a program that disrupt the normal flow of code. They allow you to handle errors and exceptional conditions gracefully.

`try:
    num = int("abc")
except ValueError as e:
    print("Error:", e)  # Output: Error: invalid literal for int() with base 10: 'abc'
`

### Class
A class is a blueprint for creating objects that encapsulate data and behavior. It defines attributes (variables) and methods (functions) that an object of that class can have.

`class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
print(person.name)  # Output: Alice
`

### Private Attribute:

Private attributes in Python are indicated by a leading double underscore (__) convention. They are not truly private, but it's a convention to indicate that they are meant to be used internally within the class.
`class MyClass:
    def __init__(self):
        self._private_var = 42

obj = MyClass()
print(obj._private_var)  # Output: 42
`
### Getter/Setter:

Getter and setter methods are used to access and modify private attributes of a class. They provide controlled access to private variables.

`class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width > 0:
            self._width = width

rect = Rectangle(5, 10)
rect.set_width(8)
print(rect.get_width())  # Output: 8
`

### Class Method:

A class method is a method that's bound to the class and not the instance. It can be called on the class itself.
``class MyClass:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1

MyClass.increment_count()
print(MyClass.count)  # Output: 1`
`

### Static Method:
A static method is a method that's bound to the class and doesn't have access to class or instance attributes. It's primarily used for utility functions.

``class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

result = MathUtils.add(5, 10)
print(result)  # Output: 15
``
### Inheritance:
Inheritance allows you to create a new class based on an existing class. The new class inherits attributes and methods from the parent class.

``class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak())  # Output: Woof!
``

### Unittest:
unittest is a built-in Python library for writing and running unit tests. It helps you ensure that your code is working correctly and as expected.
`import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 2, 4)

if __name__ == '__main__':
    unittest.main()
`
### Read/Write File:
Python provides built-in functions for reading and writing files. You can open, read, write, and close files using these functions.

Example (Read):
`with open("example.txt", "r") as file:
    content = file.read()
    print(content)
`

Example (Write):

`with open("output.txt", "w") as file:
    file.write("Hello, World!")
`