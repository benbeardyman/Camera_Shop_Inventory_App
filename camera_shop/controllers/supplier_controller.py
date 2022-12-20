from flask import Flask, Blueprint, render_template, request, redirect
from models.supplier import Supplier

import repositories.supplier_repository as supplier_repository
import repositories.product_repository as product_repository
import repositories.supplier_product_repository as supplier_product_repository

suppliers_blueprint = Blueprint("suppliers", __name__)

@suppliers_blueprint.route("/suppliers")
def suppliers():
    suppliers = supplier_repository.select_all()
    return render_template("suppliers/index.html", suppliers=suppliers)


@suppliers_blueprint.route("/suppliers/<id>")
def show(id):
    supplier = supplier_repository.select(id)
    products= product_repository.products_for_supplier(supplier)
    return render_template("suppliers/show.html", supplier=supplier, products=products)

@suppliers_blueprint.route("/suppliers/new_supplier")
def new_supplier():
    return render_template("suppliers/new_supplier.html")

@suppliers_blueprint.route("/suppliers", methods=['POST'])
def create_supplier():
    name = request.form['name']
    supplier = Supplier(name)
    supplier_repository.save(supplier)
    return redirect('/suppliers')

@suppliers_blueprint.route("/suppliers/<id>/edit_supplier")
def edit_supplier(id):
    supplier = supplier_repository.select(id)
    return render_template("suppliers/edit_supplier.html", supplier=supplier)

@suppliers_blueprint.route("/suppliers/<id>", methods=['POST'])
def update_supplier(id):
    name = request.form['name']
    supplier = Supplier(name, id)
    supplier_repository.update(supplier)
    return redirect('/suppliers')