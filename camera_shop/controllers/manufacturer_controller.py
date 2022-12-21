from flask import Flask, Blueprint, render_template, request, redirect
from models.manufacturer import Manufacturer

import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", manufacturers=manufacturers)

@manufacturers_blueprint.route("/manufacturers/<id>")
def show(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("manufacturers/show.html", manufacturer=manufacturer)

@manufacturers_blueprint.route("/manufacturers/new_manufacturer")
def new_manufacturer():
    return render_template("manufacturers/new_manufacturer.html")

@manufacturers_blueprint.route("/manufacturers", methods=['POST'])
def create_manufacturer():
    name = request.form['name']
    manufacturer = Manufacturer(name)
    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')

@manufacturers_blueprint.route("/manufacturers/<id>/edit_manufacturer")
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("manufacturers/edit_manufacturer.html", manufacturer=manufacturer)

@manufacturers_blueprint.route("/manufacturers/<id>", methods=['POST'])
def update_manufacturer(id):
    name = request.form['name']
    manufacturer = Manufacturer(name, id)
    manufacturer_repository.update(manufacturer)
    return redirect('/manufacturers')

@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods=['POST'])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect('/manufacturers')