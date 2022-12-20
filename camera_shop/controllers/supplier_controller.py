from flask import Flask, Blueprint, render_template, request, redirect
from models.supplier import Supplier

import repositories.supplier_repository as supplier_repository

suppliers_blueprint = Blueprint("suppliers", __name__)

@suppliers_blueprint.route("/suppliers")
def suppliers():
    suppliers = supplier_repository.select_all()
    return render_template("suppliers/index.html", suppliers=suppliers)


@suppliers_blueprint.route("/suppliers/<id>")
def show(id):
    supplier = supplier_repository.select(id)
    return render_template("suppliers/show.html", supplier=supplier)