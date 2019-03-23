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



    def test_get_neighbouring_coordinates_3_3(self):
        coordinate = Coordinate(3, 3)
        actual_neighbouring_coordinates = coordinate.get_neighbouring_cordinates(6, 6)

        assert len(actual_neighbouring_coordinates) == 8

        assert Coordinate(2, 2) in actual_neighbouring_coordinates
        assert Coordinate(2, 3) in actual_neighbouring_coordinates
        assert Coordinate(2, 4) in actual_neighbouring_coordinates
        assert Coordinate(3, 2) in actual_neighbouring_coordinates
        assert Coordinate(3, 4) in actual_neighbouring_coordinates
        assert Coordinate(4, 2) in actual_neighbouring_coordinates
        assert Coordinate(4, 3) in actual_neighbouring_coordinates
        assert Coordinate(4, 4) in actual_neighbouring_coordinates
    
    def test_get_neighbouring_coordinates_0_0(self):
        coordinate = Coordinate(0, 0)
        actual_neighbouring_coordinates = coordinate.get_neighbouring_cordinates(4, 4)

        assert len(actual_neighbouring_coordinates) == 3

        assert Coordinate(0, 1) in actual_neighbouring_coordinates
        assert Coordinate(1, 0) in actual_neighbouring_coordinates
        assert Coordinate(1, 1) in actual_neighbouring_coordinates


    def test_get_neighbouring_coordinates_4_4(self):
        coordinate = Coordinate(4, 4)
        actual_neighbouring_coordinates = coordinate.get_neighbouring_cordinates(4, 4)

        assert len(actual_neighbouring_coordinates) == 3

        assert Coordinate(3, 4) in actual_neighbouring_coordinates
        assert Coordinate(4, 3) in actual_neighbouring_coordinates
        assert Coordinate(3, 3) in actual_neighbouring_coordinates


    def test_get_neighbouring_coordinates_4_0(self):
        coordinate = Coordinate(4, 0)
        actual_neighbouring_coordinates = coordinate.get_neighbouring_cordinates(4, 4)

        assert len(actual_neighbouring_coordinates) == 3

        assert Coordinate(3, 0) in actual_neighbouring_coordinates
        assert Coordinate(3, 1) in actual_neighbouring_coordinates
        assert Coordinate(4, 1) in actual_neighbouring_coordinates


    def test_get_neighbouring_coordinates_0_4(self):
        coordinate = Coordinate(0, 4)
        actual_neighbouring_coordinates = coordinate.get_neighbouring_cordinates(4, 4)

        assert len(actual_neighbouring_coordinates) == 3

        assert Coordinate(0, 3) in actual_neighbouring_coordinates
        assert Coordinate(1, 3) in actual_neighbouring_coordinates
        assert Coordinate(1, 4) in actual_neighbouring_coordinates