from flask import Flask
from config.jwt import *
from config.database import engine
from models.product_model import Base  # Asegúrate que Base esté correctamente importado
from controllers.product_controllers import product_bp
from controllers.user_controllers import user_bp, register_jwt_error_handlers
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Configuración de JWT
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_TOKEN_LOCATION'] = JWT_TOKEN_LOCATION
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
app.config['JWT_HEADER_NAME'] = JWT_HEADER_NAME
app.config['JWT_HEADER_TYPE'] = JWT_HEADER_TYPE

jwt = JWTManager(app)

# Registrar blueprints
app.register_blueprint(product_bp)
app.register_blueprint(user_bp)

# Registrar manejadores personalizados de error JWT
register_jwt_error_handlers(app)

if __name__ == "__main__":
    # Crear tablas automáticamente si no existen
    print("Verificando y creando tablas de base de datos si es necesario...")
    Base.metadata.create_all(engine)
    print("Tablas listas.")
    app.run(debug=True)
