from db.run_sql import run_sql

from models.product import Product
from models.manufacturer import Manufacturer

import repositories.manufacturer_repository as manufacturer_repository


def save(product):
    sql = "INSERT INTO products (name, manufacturer_id, category, description, cost_price, retail_price, stock_level) VALUES ( %s, %s, %s, %s, %s, %s, %s ) RETURNING id"
    values = [product.name, product.manufacturer.id, product.category, product.description, product.cost_price, product.retail_price, product.stock_level]
    results = run_sql(sql, values)
    product.id = results[0]['id']
    return product


def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        product = Product(row['name'],  manufacturer, row['category'], row['description'], row['cost_price'], row['retail_price'], row['stock_level'], row['id'])
        products.append(product)
    return products


def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        product = Product(result['name'], manufacturer, result['category'], result['description'], result['cost_price'], result['retail_price'], result['stock_level'], result['id'])
    return product


def update(product):
    sql = "UPDATE products SET (name, manufacturer_id, category, description, cost_price, retail_price, stock_level) = ( %s, %s, %s, %s, %s, %s, %s ) WHERE id = %s"
    values = [product.name, product.manufacturer.id, product.category, product.description, product.cost_price, product.retail_price, product.stock_level, product.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def products_for_manufacturer(manufacturer):
    sql = "SELECT * FROM products WHERE manufacturer_id = %s"
    values = [manufacturer.id]
    result = run_sql(sql, values)[0]
    product = Product(result['name'], manufacturer, result['category'], result['description'], result['cost_price'], result['retail_price'], result['stock_level'], result['id'])
    return product