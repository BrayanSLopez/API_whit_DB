import os

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_TOKEN_LOCATION = ["headers"]
JWT_ACCESS_TOKEN_EXPIRES = 2400  # Duración actual: 40 minutos
JWT_HEADER_NAME = "Authorization"
JWT_HEADER_TYPE = "Bearer"