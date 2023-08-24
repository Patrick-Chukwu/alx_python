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
    def __init__(self, width, height, name, value):
        super().__init__(name, value)
        self.__width = width
        self.__height = height