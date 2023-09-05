class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """
    pass

u = User()
print(u.id)

#another

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """

    def __init__(self):
        self.id = 89
        super().__init__()

u = User()
print(u.id)

#ANOTHER 
class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """
    pass

for i in range(4):
    u = User()
print(u.id)

#Another one
class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """
    pass

b = Base()
u = User()
print(u.id)


"""An empty class"""
class BaseGeometry:
    """My BaseGeometry class"""
    pass
    
    def area(self):
        """function Area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function integer_validator"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        
class Rectangle(BaseGeometry):
    """A Rectangle subclass"""
    def __init__(self, width, height):
        """
        Define the init method and inherits from the super.
        Arguments:
            width
            height
        """
        # super().__init__(name, value)
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        
r = Rectangle(1, 4)
print(issubclass(Rectangle, BaseGeometry))

"""Different example"""



def print_args(*args):
    """Functon to return a sum"""
    return sum(args)

result = print_args(3, 5, 6)
print(result)

def print_loop(*args):
    for arg in args:
        print(arg)
        

loop = print_loop("hello", "hi", 3, 5)
print(loop)


def print_args(*args):
    for arg in args:
        print(arg)

print_args("Hello", "World", 42)

###new 

def format_strings(*args):
    return ", ".join(args)

formatted = format_strings("Alice", "Bob", "Charlie")
print(formatted)  # Output: Alice, Bob, Charlie


def display_user_info(**kwargs):
    if "name" in kwargs and "age" in kwargs:
        print(f"Name: {kwargs['name']}, age: {kwargs['age']}")
    else:
        print("details incomplete")


display_user_info(name="Alice", age=30, city="New York")


def print_key(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_key(name="Alice", age=30, city="New York")

### using kwargs to create HTMl tags

def create_html_element(tag, **attributes):
    attribute_str = ", ".join([f'{key}: "{value}"]' for key, value in attributes.items()])
    return f"<{tag} {attribute_str}></{tag}>"

element = create_html_element("a", href="https://example.com", target="_blank", text="Visit Example")
print(element)  # Output: <a href="https://example.com" target="_blank">Visit Example</a>


def generate_email(subject, body, recipient="user@example.com"):
    return f"Subject: {subject}\nRecipient: {recipient}\n\n{body}"

email = generate_email(subject="Important Update", body="Please review the attached document.")
print(email)

"""Example 3: Mixing Positional and Named Arguments

"""
def format_address(name, street, city, postal_code):
    return f"{name}\n{street}\n{city}, {postal_code}"

address = format_address("Alice", "123 Main St", "New York", 
                         "10001")
print(address)


"""turning python into JSON"""
import json

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(data)
print(json_string)



"""Decoding a JSON file into a Python Object"""
import json

json_string = '{"name": "Alice", "age": 30, "city": "New York"}'

python_data = json.loads(json_string)
print(python_data)  # Output: Alice
print(python_data["age"])   # Output: 30

"""Serialization and deserialization"""

import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance of the class
person = Person("Alice", 30)

# Serialize the instance using pickle
serialized_person = pickle.dumps(person)

# Save the serialized data to a file
with open("person.pickle", "wb") as file:
    file.write(serialized_person)


## New 

import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Load the serialized data from the file
with open("person.pickle", "rb") as file:
    serialized_person = file.read()

# Deserialize the data using pickle
deserialized_person = pickle.loads(serialized_person)

print(deserialized_person.name)  # Output: Alice
print(deserialized_person.age)   # Output: 30


"""New example of JSON file for nested data"""

import json

data = {
    "person": {
        "name": "Alice",
        "age": 30,
        "address": {
            "city": "New York",
            "zip": "10001"
        }
    }
}

# Writing JSON to a file
with open("nested_data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

# Reading JSON from a file
with open("nested_data.json", "r") as json_file:
    loaded_data = json.load(json_file)

print(loaded_data)

"""A new class with classmethod"""
class MyClass:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1

MyClass.increment_count()
print(MyClass.count)  # Output: 1

"""A new class with static method"""

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

result = MathUtils.add(5, 10)
print(result)  # Output: 15

with open("output.txt", "w") as file:
    file.write("Hello, world")

with open("output.txt", "r") as file:
    content = file.read()
    print(content)

with open("README.md", "r") as file:
    content = file.read()
    print(content)

with open("new_file.txt", "w") as file:
    file.write("I do hope you are well?")



"""Imported from the Base class"""



from models.base import Base


class Rectangle(Base):
    """ A subclass Rectangle with arguments    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        A function that defines the subclass

        Arguments:
            width (int)
            height (int)
            x (int)
            y (int)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """A width property"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """A width setter"""
        if not isinstance(value, int):
            raise TypeError(f"width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

   
    @property
    def height(self):
        """A height property"""
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError(f"height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        """A height setter"""
        self.__height = value
    
    @property
    def x(self):
        """A x property"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """A x setter"""
        if not isinstance(value, int):
            raise TypeError(f"x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """A y property"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """A y setter"""
        if not isinstance(value, int):
            raise TypeError(f"y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """A public method that returns the value of area of a rectangle"""
        
        return self.__width * self.__height
    
    def display(self):
        """A public method that prints in stdout"""
    
        for _ in range(self.__height):
            print("#" * self.__width)

r1 = Rectangle(10, 12)
r1.display()