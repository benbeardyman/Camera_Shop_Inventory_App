from flask import Flask, Blueprint, render_template, request, redirect
from models.product import Product
from models.manufacturer import Manufacturer

import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository


products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products=products)

@products_blueprint.route("/products/<id>")
def show(id):
    product = product_repository.select(id)
    return render_template("products/show.html", product=product)

@products_blueprint.route("/products/new_product")
def new_product():
    manufacturers = manufacturer_repository.select_all()
    return render_template("products/new_product.html", manufacturers=manufacturers)

@products_blueprint.route("/products", methods=['POST'])
def create_product():
    name = request.form['name']
    manufacturer_id = request.form['manufacturer_id']
    category = request.form['category']
    description = request.form['description']
    cost_price = request.form['cost_price']
    retail_price = request.form['retail_price']
    stock_level = request.form['stock_level']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    product = Product(name, manufacturer, category, description, cost_price, retail_price, stock_level)
    product_repository.save(product)
    return redirect('/products')


@products_blueprint.route("/products/<id>/edit_product")
def edit_product(id):
    product = product_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template("products/edit_product.html", product=product, manufacturers=manufacturers)

@products_blueprint.route("/products/<id>", methods=['POST'])
def update_product(id):
    name = request.form['name']
    manufacturer_id = request.form['manufacturer_id']
    category = request.form['category']
    description = request.form['description']
    cost_price = request.form['cost_price']
    retail_price = request.form['retail_price']
    stock_level = request.form['stock_level']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    product = Product(name, manufacturer, category, description, cost_price, retail_price, stock_level, id)
    product_repository.update(product)
    return redirect('/products')

@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')