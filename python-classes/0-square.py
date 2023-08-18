
class Square:
    """ This is a class with a private instance
    the size is the private instance

    """
    def __init__(self, size):
        self.__size = size  # Private instance attribute
    
    def area(self):
        return self.__size ** 2
