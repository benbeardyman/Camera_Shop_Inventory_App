from db.run_sql import run_sql

from models.product import Product
from models.supplier import Supplier


def save(product):
    sql = "INSERT INTO products(name,  category, description, manufacturer, retail_price, stock_level) VALUES ( %s, %s, %s, %s, %s, %s ) RETURNING id"
    values = [product.name, product.category, product.description, product.manufacturer, product.retail_price, product.stock_level]
    results = run_sql(sql, values)
    product.id = results[0]['id']
    return product

def select_all():
    products = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        product = Product(row['name'], row['category'], row['description'], row['manufacturer'], row['retail_price'], row['stock_level'], ['id'])
        products.append(product)
    return products