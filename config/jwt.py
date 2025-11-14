import os

from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Cargar configuración desde variables de entorno
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'clave_por_defecto_cambiar_en_produccion')
JWT_TOKEN_LOCATION = os.getenv('JWT_TOKEN_LOCATION', 'headers').split(',')
JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 2400))
JWT_HEADER_NAME = os.getenv('JWT_HEADER_NAME', 'Authorization')
JWT_HEADER_TYPE = os.getenv('JWT_HEADER_TYPE', 'Bearer')