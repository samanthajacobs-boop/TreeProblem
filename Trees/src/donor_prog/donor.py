from typing import Optional, Callable, TypeVar, Generic
T = TypeVar('T')

class Donor(object):
    """
    Maybe it would be a good idea to a make a simple donor class
    """

    def __init__(self, name: T, amount: T) -> None:

        self.name = name
        self.amount = amount

    def __str__(self):
        return "{} with a donation of {}".format(self.name, self.amount)

# using key now, don't need these
#    def __lt__(self,other : object) -> bool:
#        if isinstance(other,Donor):
#            if self.amount < other.amount: 
#                return True
#            else:
#                return False
#        else:
#            #if self.amount < other: 
#            if self < other.amount: 
#                return True
#            else:
#                return False
#
#
#    def __eq__(self,other : object) -> bool:
#        if isinstance(other,Donor):
#            if self.amount == other.amount: 
#                return True
#            else:
#                return False
#        else:
#            if self.amount == other: 
#                return True
#            else:
#                return False
#
#    def __ge__(self,other : object) -> bool:
#        if self.amount >= other.amount: 
#            return True
#        else:
#            return False
