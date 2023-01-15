import unittest
from models.product import Product
from models.manufacturer import Manufacturer

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.manufacturer = Manufacturer("Nikon")
        self.product = Product("D7500", self.manufacturer, "DSLR", "D7500 DSLR Camera + AF-S 18-140mm VR", 800.00, 1100.00, 4)

    def test_product_has_name(self):
        self.assertEqual("D7500", self.product.name)  

    def test_product_has_manufacturer(self):
        self.assertEqual(self.manufacturer, self.product.manufacturer)  

    def test_product_has_categroy(self):
        self.assertEqual ("DSLR", self.product.category)

    def test_product_has_description(self):
        self.assertEqual("D7500 DSLR Camera + AF-S 18-140mm VR", self.product.description)

    def test_product_has_cost_price(self):
        self.assertEqual(800.00, self.product.cost_price)    

    def test_product_has_retail_price(self):
        self.assertEqual(1100.00, self.product.retail_price)

    def test_product_has_stock_level(self):
        self.assertEqual(4, self.product.stock_level)    