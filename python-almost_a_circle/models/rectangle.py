"""Imported from the Base class"""

from models.base import Base

"""Imported from the Base class"""

class Rectangle(Base):
    """
    A subclass Rectangle with arguments

    
    """
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
        self.__width = value

    @property
    def height(self):
        """A height property"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """A height setter"""
        self.__height = value
    
    @property
    def x(self):
        """A x property"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """A x setter"""
        self.__x = value

    @property
    def y(self):
        """A y property"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """A y setter"""
        self.__y = value

    if type(width) is not int:
        raise TypeError(f"width must be an integer")
    elif width <= 0:
        raise ValueError("width must be > 0")
    
    if type(height) is not int:
        raise TypeError(f"height must be an integer")
    elif height <= 0:
        raise ValueError("height must be > 0")
    
    if type(x) is not int:
        raise TypeError(f"x must be an integer")
    elif x < 0:
        raise ValueError("x must be >= 0")
    
    if type(y) is not int:
        raise TypeError(f"y must be an integer")
    elif y <= 0:
        raise ValueError("y must be > 0")
    
    
