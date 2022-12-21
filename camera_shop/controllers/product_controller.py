from flask import Flask, Blueprint, render_template, request, redirect
from models.product import Product

import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository
import repositories.supplier_product_repository as supplier_product_repository


products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products=products)


@products_blueprint.route("/products/<id>")
def show(id):
    product = product_repository.select(id)
    suppliers = supplier_repository.suppliers_for_product(product)
    return render_template("products/show.html", product=product, suppliers=suppliers)


@products_blueprint.route("/products/new_product")
def new_product():
    return render_template("products/new_product.html")

@products_blueprint.route("/products", methods=['POST'])
def create_product():
    name = request.form['name']
    manufacturer = request.form['manufacturer']
    category = request.form['category']
    description = request.form['description']
    retail_price = request.form['retail_price']
    stock_level = request.form['stock_level']
    product = Product(name, manufacturer, category, description, retail_price, stock_level)
    product_repository.save(product)
    return redirect('/products')


@products_blueprint.route("/products/<id>/edit_product")
def edit_product(id):
    product = product_repository.select(id)
    return render_template("products/edit_product.html", product=product)

@products_blueprint.route("/products/<id>", methods=['POST'])
def update_product(id):
    name = request.form['name']
    manufacturer = request.form['manufacturer']
    category = request.form['category']
    description = request.form['description']
    retail_price = request.form['retail_price']
    stock_level = request.form['stock_level']
    product = Product(name, manufacturer, category, description, retail_price, stock_level, id)
    product_repository.update(product)
    return redirect('/products')

@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')