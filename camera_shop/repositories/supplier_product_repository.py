from db.run_sql import run_sql

from models.product import Product
from models.supplier import Supplier
from models.supplier_product import Supplier_Product

import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository


def save(supplier_product):
    sql = "INSERT INTO suppliers_products (supplier_id, product_id, cost_price) VALUES ( %s, %s, %s ) RETURNING id"
    values = [supplier_product.supplier.id, supplier_product.product.id, supplier_product.cost_price]
    results = run_sql(sql, values)
    supplier_product.id = results[0]['id']
    return supplier_product


def delete_all():
    sql = "DELETE FROM suppliers_products"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM suppliers_products WHERE id = %s"
    values = [id]
    run_sql(sql, values)