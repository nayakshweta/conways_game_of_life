from unittest import TestCase
from coordinate import Coordinate

class TestCoordinate(TestCase):

    def test_coordinate_creation(self):
        coordinate = Coordinate(1, 2)
        assert coordinate.x == 1
        assert coordinate.y == 2
        