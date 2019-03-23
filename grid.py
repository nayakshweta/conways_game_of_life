from coordinate import Coordinate
from cell import Cell

class Grid:
    def __init__(self, row_count, column_count):
        self.row_count = row_count
        self.column_count = column_count
        self.cells = []

    def mark_cell(self, x, y, status):
        coordinate = Coordinate(x, y)
        cell = Cell(coordinate, status)
        self.cells.append(cell)
    
    def get_live_neighbour_count(self, coordinate):
        neighbouring_coordinates = coordinate.get_neighbouring_cordinates(self.row_count, self.column_count)
        live_neighbour_count = 0

        for cell in self.cells:
            if cell.coordinate in neighbouring_coordinates and cell.status == True:
                live_neighbour_count += 1

        return live_neighbour_count