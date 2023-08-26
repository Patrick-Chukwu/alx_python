"""A class module inheriting from Rectangle class"""

from typing import Any
from models.base import Base
from models.rectangle import Rectangle

class Square(Rectangle):
    """A class module inheriting from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, size, size, x, y)
 
    

    @property
    def size(self):
        return self.width

    @size.setter    
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
