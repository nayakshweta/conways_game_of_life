class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.x == other.x and self.y == other.y:
                return True
        return False


    def __ne__(self, other):
        return not isinstance(other, self.__class__) or (self.x != other.x and self.y != other.y)