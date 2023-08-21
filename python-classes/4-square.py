class Square:
    """ This is a class with a private instance
    the size is the private instance
    
    
    """
    def __init__(self, size = 0):
        """
        
        Args:
            size (int): takes the number whose square will be found.
        """
        

        
        self.__size = size  # Private instance attribute


    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    def area(self):
        return self.__size ** 2
    
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)


    
