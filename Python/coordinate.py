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


    def get_neighbouring_cordinates(self, grid_row_size, grid_column_size):
        coordinates = []

        if (self.x - 1) >= 0:
            coordinates.append(Coordinate(self.x - 1, self.y))

            if (self.y - 1) >= 0:
                coordinates.append(Coordinate(self.x - 1, self.y - 1))
            
            if (self.y + 1) < grid_column_size:
                coordinates.append(Coordinate(self.x - 1, self.y + 1))
        
        if (self.y - 1) >= 0:
            coordinates.append(Coordinate(self.x, self.y - 1))
        
        if (self.y + 1) < grid_column_size:
            coordinates.append(Coordinate(self.x, self.y + 1))

        if (self.x + 1) < grid_row_size:
            coordinates.append(Coordinate(self.x + 1, self.y))

            if (self.y - 1) >= 0:
                coordinates.append(Coordinate(self.x + 1, self.y - 1))
            
            if (self.y + 1) < grid_column_size:
                coordinates.append(Coordinate(self.x + 1, self.y + 1))

        return coordinates