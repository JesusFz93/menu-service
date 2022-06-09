from flask import Flask
from routes.products_routes import products_routes

# from controllers import products as products_controller

app = Flask(__name__)

app.register_blueprint(products_routes, url_prefix="/api")


if __name__ == '__main__':
    app.run(debug=True)