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
        super().__init__(name, value)
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height