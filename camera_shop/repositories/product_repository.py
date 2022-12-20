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


def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        product = Product(result['name'], result['manufacturer'], result['category'], result['description'], result['retail_price'], result['stock_level'], result['id'])
    return product


def products_for_supplier(supplier):
    products = []

    sql = "SELECT products.* FROM products INNER JOIN suppliers_products ON suppliers_products.product_id = products.id WHERE supplier_id = %s"
    values = [supplier.id]
    results = run_sql(sql, values)

    for row in results:
        product = Product(row['name'], row['manufacturer'], row['category'], row['description'], row['retail_price'], row['stock_level'], row['id'])
        products.append(product)

    return products


def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)