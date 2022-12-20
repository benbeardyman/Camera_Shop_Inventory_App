from flask import Flask, Blueprint, render_template, request, redirect
from models.product import Product

import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository


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