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