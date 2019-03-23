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