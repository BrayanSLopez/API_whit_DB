from flask import Flask
from config.jwt import JWT_SECRET_KEY, JWT_TOKEN_LOCATION, JWT_ACCESS_TOKEN_EXPIRES, JWT_HEADER_NAME, JWT_HEADER_TYPE
import os
from dotenv import load_dotenv
from config.database import engine
from models.db import Base
from controllers.product_controllers import product_bp
from controllers.user_controllers import user_bp, register_jwt_error_handlers
from flask_jwt_extended import JWTManager
from models.product_model import Categoria, Proveedor, Descuento, Impuesto, Producto
from models.user_model import User
# Cargar variables de entorno
load_dotenv()


app = Flask(__name__)

# Configuración de JWT
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY  # Clave secreta para el JWT
app.config['JWT_TOKEN_LOCATION'] = JWT_TOKEN_LOCATION  # Ubicación del token (en los headers)
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES  # Tiempo de expiración del token
app.config['JWT_HEADER_NAME'] = JWT_HEADER_NAME  # Nombre del header donde se encuentra el token
app.config['JWT_HEADER_TYPE'] = JWT_HEADER_TYPE  # Tipo de encabezado del token (Bearer)

# Inicializa el manager de JWT
jwt = JWTManager(app)

# Crear tablas ANTES de registrar blueprints y ejecutar la aplicación
print("Verificando y creando tablas de base de datos si es necesario...")
Base.metadata.create_all(engine)  # Crear todas las tablas en la base de datos si no existen
print("Tablas listas.")
print("Base de datos usada:", engine.url)

# Registrar blueprints
app.register_blueprint(product_bp)  # Ruta de productos
app.register_blueprint(user_bp)  # Ruta de usuarios

# Registrar manejadores personalizados de error JWT
register_jwt_error_handlers(app)

if __name__ == "__main__":
    # Usar configuración de entorno para debug
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode)

