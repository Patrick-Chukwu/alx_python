"""An almost-a-circle directory"""
class Base:
    """
    A base class with private class attribute: __nb_objects.
    """
    __nb_objects = 0
    def __init__(self,id=None):
        """
        An init object
        Arguments:
            id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


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
        for _ in range(self.__y):
            print("$")
        for _ in range(self.__height):
            print("#" * self.__width +"$" )

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args):
        """A method that updates by parsing arguments
        """
        for arg in args:
          return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"



r1 = Rectangle(2, 3, 2, 0)
r1.display()
print("New output")

r1 = Rectangle(2, 3, 2, 2)
r1.display()

print("New output")

r1 = Rectangle(2, 3, 2, 1)
r1.display()




print("---")

r2 = Rectangle(3, 2, 1, 0)
r2.display()

# r1 = Rectangle(10, 10, 10, 10)
# print(r1)

r1.update(89)
print(r1)

r1.update(89, 2)
print(r1)

r1.update(89, 2, 3)
print(r1)

r1.update(89, 2, 3, 4)
print(r1)

r1.update(89, 2, 3, 4, 5)
print(r1)