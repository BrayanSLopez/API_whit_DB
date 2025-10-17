import os

# Definir las claves y configuraciones directamente en el código
JWT_SECRET_KEY = "tu_clave_secreta_aleatoria"  
JWT_TOKEN_LOCATION = ["headers"]
JWT_ACCESS_TOKEN_EXPIRES = 2400  # Duración del token en segundos (40 minutos)
JWT_HEADER_NAME = "Authorization"
JWT_HEADER_TYPE = "Bearer"