from unittest import TestCase
from cell import Cell
from coordinate import Coordinate

class TestCell(TestCase):
    def test_cell_initialization(self):
        coordinate = Coordinate(2, 2)
        cell = Cell(coordinate, True)

        assert cell.coordinate == coordinate
        assert cell.status == True

    def test_cell_set_next_status_while_live_neighbours_3_and_current_status_live(self):
        coordinate = Coordinate(2, 2)
        cell = Cell(coordinate, True)
        live_neighbour_count = 3

        next_status = cell.calculate_next_status(live_neighbour_count)
        assert next_status == True

    def test_cell_set_next_status_while_live_neighbours_6_and_current_status_live(self):
        coordinate = Coordinate(2, 2)
        cell = Cell(coordinate, True)
        live_neighbour_count = 6

        next_status = cell.calculate_next_status(live_neighbour_count)
        assert next_status == False

    def test_cell_set_next_status_while_live_neighbours_3_and_current_status_dead(self):
        coordinate = Coordinate(2, 2)
        cell = Cell(coordinate, False)
        live_neighbour_count = 3

        next_status = cell.calculate_next_status(live_neighbour_count)
        assert next_status == True