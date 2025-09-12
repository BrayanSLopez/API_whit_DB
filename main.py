from flask import Flask
from controllers.product_controllers import product_bp 

app = Flask(__name__)

# Registrar el blueprint de productos
app.register_blueprint(product_bp)

if __name__ == "__main__":
    app.run(debug=True)
