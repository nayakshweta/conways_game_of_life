from unittest import TestCase
from grid import Grid
from conways_game_of_life import create_grid_from_array_of_strings

class TestConways(TestCase):
    def test_create_grid_from_array_of_strings(self):
        lines_unformatted = ['........\n', '....*...\n', '...**...\n', '........']
        grid = create_grid_from_array_of_strings(lines_unformatted)
        
        assert grid.row_count == 4
        assert grid.column_count == 8
        assert len(grid.cells) == 32