from flask import Flask, Blueprint, render_template, request, redirect
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository
import repositories.product_repository as product_repository

suppliers_blueprint = Blueprint("suppliers", __name__)