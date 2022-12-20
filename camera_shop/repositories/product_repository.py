from db.run_sql import run_sql

from models.product import Product
from models.supplier import Supplier


def save(product):
    sql = "INSERT INTO products(name,  category, description, manufacturer, retail_price, stock_level) VALUES ( %s, %s, %s, %s, %s, %s ) RETURNING id"
    values = [product.name, product.manufacturer, product.category, product.description, product.retail_price, product.stock_level]
    results = run_sql(sql, values)
    product.id = results[0]['id']
    return product


def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for row in results:
        product = Product(row['name'],  row['manufacturer'], row['category'], row['description'], row['retail_price'], row['stock_level'], ['id'])
        products.append(product)
    return products


def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)