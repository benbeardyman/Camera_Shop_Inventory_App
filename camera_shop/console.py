import pdb
from models.product import Product
from models.supplier import Supplier
from models. supplier_product import Supplier_Product

import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository
import repositories.supplier_product_repository as supplier_product_repository



product1 = Product('Canon DSLR', 'Camera', 'Canon Camera', 'Canon', 599.99, 3)
product_repository.save(product1)