from unittest import TestCase
from cell import cell

class TestCell(TestCase):
    def test_cell_initialization(self):
        coordinate = Coordinate(2, 2)
        cell = Cell(coordinate, True)

        assert cell.coordinate == coordinate
        assert cell.status == True