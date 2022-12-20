import pdb
from models.product import Product
from models.supplier import Supplier
from models. supplier_product import Supplier_Product

import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository
import repositories.supplier_product_repository as supplier_product_repository

# supplier_product_repository.delete_all()
product_repository.delete_all()
supplier_repository.delete_all()



product1 = Product('EOS 4000D', 'Canon', 'DSLR Camera', 'EOS 4000D 18-55 / 3.5-5.6 EF-S III', 399.99, 3)
product_repository.save(product1)


supplier1 = Supplier('Swains')


# supplier_product1 = Supplier_Product (supplier1, product1, 250.00)