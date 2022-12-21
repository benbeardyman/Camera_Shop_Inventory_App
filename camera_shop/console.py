import pdb
from models.product import Product
from models.supplier import Supplier
from models.supplier_product import Supplier_Product
from models.manufacturer import Manufacturer

import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository
import repositories.supplier_product_repository as supplier_product_repository
import repositories.manufacturer_repository as manufacturer_repository

manufacturer_repository.delete_all()
supplier_product_repository.delete_all()
product_repository.delete_all()
supplier_repository.delete_all()


manufacturer_1 = Manufacturer('Canon')
manufacturer_repository.save(manufacturer_1)

manufacturer_2 = Manufacturer('Nikon')
manufacturer_repository.save(manufacturer_2)


product_1 = Product('EOS 4000D', manufacturer_1, 'DSLR Camera', 'Canon EOS 4000D DSLR Camera and EF-S 18-55 mm f/3.5-5.6 III Lens - Black', 399.99, 3)
product_repository.save(product_1)

product_2 = Product('D7500', manufacturer_2, 'DSLR Camera', 'Nikon D7500 Camera Body with 18-140 mm VR Digital DSLR Kit - Black', 999.99, 2)
product_repository.save(product_2)

# pdb.set_trace()