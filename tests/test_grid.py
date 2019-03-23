from unittest import TestCase
from grid import Grid

class TestGrid(TestCase):

    def test_grid_creation(self):
        grid = Grid(4, 6)

        assert grid.row_count == 4
        assert grid.column_count == 6
        assert grid.cells == []
        