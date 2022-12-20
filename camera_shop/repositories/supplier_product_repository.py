from db.run_sql import run_sql

from models.product import Product
from models.supplier import Supplier
from models.supplier_product import Supplier_Product
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository


def save(supplier_product):
    sql = "INSERT INTO suppliers_products (supplier_id, product_id, cost_price) VALUES ( %s, %s, %s ) RETURNING id"
    values = [supplier_product.supplier_id, supplier_product.product_id, supplier_product.cost_price]
    results = run_sql(sql, values)
    supplier_product.id = results[0]['id']
    return supplier_product


def delete_all():
    sql = "DELETE FROM supplier_product"
    run_sql(sql)