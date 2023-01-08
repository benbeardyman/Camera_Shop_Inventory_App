import unittest
from models.manufacturer import Manufacturer
from repositories.manufacturer_repository import *

class TestManufacturerRep(unittest.TestCase):

    def setUp(self):
        self.manufacturer = Manufacturer("FujiFilm")

    def test_manufacturer_saves(self):
        self.manufacturer_repository.save(self.manufacturer)
        self.assertEqual("FujiFilm", self.manufacturer.name)