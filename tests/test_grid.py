from unittest import TestCase
from grid import Grid
from coordinate import Coordinate

class TestGrid(TestCase):

    def test_grid_creation(self):
        grid = Grid(4, 6)

        assert grid.row_count == 4
        assert grid.column_count == 6
        assert grid.cells == []

    def test_grid_mark_cell(self):
        grid = Grid(4, 6)
        grid.mark_cell(1, 2, True)

        assert len(grid.cells) == 1
    
    def test_live_neighbour_count(self):
        grid = Grid(3, 3)
        grid.mark_cell(0, 0, False)
        grid.mark_cell(0, 1, False)
        grid.mark_cell(0, 2, False)
        grid.mark_cell(1, 0, False)
        grid.mark_cell(1, 1, True)
        grid.mark_cell(1, 2, True)
        grid.mark_cell(2, 0, False)
        grid.mark_cell(2, 1, False)
        grid.mark_cell(2, 2, False)

        coordinate = Coordinate(1, 1)
        
        actual_live_neighbour_count = grid.get_live_neighbour_count(coordinate)

        assert actual_live_neighbour_count == 1

    def test_calculate_next_grid(self):
        grid = Grid(3, 3)
        grid.mark_cell(0, 0, False)
        grid.mark_cell(0, 1, False)
        grid.mark_cell(0, 2, True)
        grid.mark_cell(1, 0, False)
        grid.mark_cell(1, 1, True)
        grid.mark_cell(1, 2, True)
        grid.mark_cell(2, 0, False)
        grid.mark_cell(2, 1, False)
        grid.mark_cell(2, 2, False)

        next_grid = grid.calculate_next_grid()
        
        assert len(next_grid.cells) == 9

        for cell in next_grid.cells:
            if cell.coordinate == Coordinate(1, 2):
                actual_status = cell.get_current_status()
                assert actual_status == True
    
