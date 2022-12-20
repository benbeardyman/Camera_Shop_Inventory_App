import pdb
from models.product import Product
from models.supplier import Supplier
from models. supplier_product import Supplier_Product

import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository
import repositories.supplier_product_repository as supplier_product_repository

supplier_product_repository.delete_all()
product_repository.delete_all()
supplier_repository.delete_all()



product1 = Product('EOS 4000D', 'Canon', 'DSLR Camera', 'Canon EOS 4000D DSLR Camera and EF-S 18-55 mm f/3.5-5.6 III Lens - Black', 399.99, 3)
product_repository.save(product1)

product2 = Product('D7500', 'Nikon', 'DSLR Camera', 'Nikon D7500 Camera Body with 18-140 mm VR Digital DSLR Kit - Black', 999.99, 2)
product_repository.save(product2)


supplier1 = Supplier('Swains')
supplier_repository.save(supplier1)

supplier2 = Supplier('JSP')
supplier_repository.save(supplier2)


supplier_product1 = Supplier_Product (supplier1, product1, 250.00)
supplier_product_repository.save(supplier_product1)

supplier_product2 = Supplier_Product (supplier2, product1, 264.99)
supplier_product_repository.save(supplier_product2)

supplier_product3 = Supplier_Product (supplier1, product2, 760.00)
supplier_product_repository.save(supplier_product3)





# pdb.set_trace()