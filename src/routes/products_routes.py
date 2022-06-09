
from flask import Blueprint, request
from controllers.products_controller import *

products_routes = Blueprint("products_routes", __name__)


@products_routes.route("/products", methods=["GET"])
def getProductsExample_RT():
    return getProductsExample_CT()


@products_routes.route("/products", methods=["POST"])
def create_user():
    return postProduct_CT(request.get_json())


@products_routes.route("/products/wapp", methods=["POST"])
def func_wappalizer():
    return wappalizer(request.get_json())


@products_routes.route("/products/dns", methods=["POST"])
def func_dns():
    return obtendns(request.get_json())
