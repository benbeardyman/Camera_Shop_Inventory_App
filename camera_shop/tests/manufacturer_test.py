import unittest
from models.manufacturer import Manufacturer

class TestManufacturer(unittest.TestCase):

    def setUp(self):
        self.manufacturer = Manufacturer("FujiFilm")

    def test_manufacturer_has_name(self):
        self.assertEqual("FujiFilm", self.manufacturer.name)