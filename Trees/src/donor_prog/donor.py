from typing import Optional, Callable, TypeVar, Generic
T = TypeVar('T')

class Donor(object):
    """
    Maybe it would be a good idea to a make a simple donor class
    """

    def __init__(self, name: T, value: T) -> None:

        self.name = name
        self.value = value

    def __str__(self):
        return "{} with a donation of {}".format(self.name, self.value)


    def __eq__(self,other : object) -> bool:
        if type(other) is int:
            if self.value == other:
                return True
            else:
                return False

        else:
            if self.value == other.value: 
                return True
            else:
                return False
#
#        if self.value == other.value: 
#            return True
#        else:
#            return False

    def __ge__(self,other : object) -> bool:
        if type(other) is int:
            if self.value >= other.value:
                return True
            else:
                return False

        else:
            if self.value >= other.value: 
                return True
            else:
                return False

    def __lt__(self,other : object) -> bool:
#        if type(other) is int:
#            if self.value < other:
#                return True
#            else:
#                return False
#
#        else:
#            if self.value < other.value: 
#                return True
#            else:
#                return False

        if self.value < other.value: 
            return True
        else:
            return False
