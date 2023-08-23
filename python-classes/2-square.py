"""This is a module in class"""
class Square:
    """ This is a class with a private instance
    the size is the private instance
    
    
    """
    def __init__(self, size = 0):
        """
        
        Args:
            size (int): takes the number whose square will be found.
        """
        

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size  # Private instance attribute


    def area(self):
        return self.__size ** 2