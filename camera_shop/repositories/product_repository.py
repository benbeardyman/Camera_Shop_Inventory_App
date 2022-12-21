from db.run_sql import run_sql

from models.product import Product
from models.supplier import Supplier
from models.manufacturer import Manufacturer

import repositories.manufacturer_repository as manufacturer_repository


def save(product):
    sql = "INSERT INTO products (name, manufacturer_id, category, description, retail_price, stock_level) VALUES ( %s, %s, %s, %s, %s, %s ) RETURNING id"
    values = [product.name, product.manufacturer.id, product.category, product.description, product.retail_price, product.stock_level]
    results = run_sql(sql, values)
    product.id = results[0]['id']
    return product


def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for row in results:
        product = Product(row['name'],  row['manufacturer'], row['category'], row['description'], row['retail_price'], row['stock_level'], row['id'])
        products.append(product)
    return products


def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        product = Product(result['name'], result['manufacturer'], result['category'], result['description'], result['retail_price'], result['stock_level'], result['id'])
    return product



def update(product):
    sql = "UPDATE products SET (name, manufacturer, category, description, retail_price, stock_level) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.name, product.manufacturer, product.category, product.description, product.retail_price, product.stock_level, product.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)