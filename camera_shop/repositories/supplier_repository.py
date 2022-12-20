from db.run_sql import run_sql

from models.product import Product
from models.supplier import Supplier


def save(supplier):
    sql = "INSERT INTO suppliers(name) VALUES ( %s ) RETURNING id"
    values = [supplier.name]
    results = run_sql(sql, values)
    supplier.id = results[0]['id']
    return supplier


def select_all():
    suppliers = []

    sql = "SELECT * FROM suppliers"
    results = run_sql(sql)
    for row in results:
        supplier = Supplier(row['name'], ['id'])
        suppliers.append(supplier)
    return suppliers


def delete_all():
    sql = "DELETE FROM suppliers"
    run_sql(sql)