"""Imported from the Base class"""

from typing import Any
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

        for _ in range(self.__y):
            print("$" * self.__x)

    def __str__(self):
        """A special method that prints a str"""

        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

