from flask import Flask, Blueprint, render_template, request, redirect
from models.supplier_product import Supplier_Product
import repositories.supplier_product_repository as supplier_product_repository
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

suppliers_products_blueprint = Blueprint("suppliers_products", __name__)