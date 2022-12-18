from db.run_sql import run_sql

from models.product import Product
from models.supplier import Supplier


def save(supplier):
    sql = "INSERT INTO suppliers(name) VALUES ( %s ) RETURNING id"
    values = [supplier.name]
    results = run_sql(sql, values)
    supplier.id = results[0]['id']
    return supplier