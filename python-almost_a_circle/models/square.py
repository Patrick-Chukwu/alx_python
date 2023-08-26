"""A class module inheriting from Rectangle class"""

from typing import Any
from models.base import Base
from models.rectangle import Rectangle

class Square(Rectangle):
    """A class module inheriting from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        super(id, width, height, x, y)
        self.__size = size
        self.__width = size
        self.__height = size

    def __str__(self):
        """A special method that prints a str"""

        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.size}"
