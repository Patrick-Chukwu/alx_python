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
        if id != 0:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects