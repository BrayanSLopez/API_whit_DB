from flask import Flask
from controllers.product_controllers import product_bp 
from controllers.user_controllers import user_bp

app = Flask(__name__)

# Registrar el blueprint de productos
app.register_blueprint(product_bp)
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(debug=True)
