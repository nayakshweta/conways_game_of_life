from unittest import TestCase
from coordinate import Coordinate

class TestCoordinate(TestCase):

    def test_coordinate_creation(self):
        coordinate = Coordinate(1, 2)
        assert coordinate.x == 1
        assert coordinate.y == 2


    def test_coordinate_comparison(self):
        coordinate1 = Coordinate(2, 3)
        coordinate2 = Coordinate(2, 3)

        assert coordinate1 == coordinate2


    def test_coordinate_negative_comparison(self):
        coordinate1 = Coordinate(1, 2)
        coordinate2 = Coordinate(2, 3)

        assert coordinate1 != coordinate2