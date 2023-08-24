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
    """
    A subclass Rectangle with arguments

    
    """
    def __init__(self, width, height, x, y, id=None):
        """
        A function that defines the subclass
        Arguments:
            width (int)
            height (int)
            x (int)
            y (int)
        """
        super().__init__(id=None)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y