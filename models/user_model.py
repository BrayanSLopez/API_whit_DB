import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from sqlalchemy import Column, Integer, String
from models.db import Base  

class User(Base):
    """
    Modelo de usuario para la base de datos.
    """
    __tablename__ = 'users'
    # ID único del usuario, clave primaria y autoincremental
    id = Column(Integer, primary_key=True, index=True)
    # Nombre de usuario, único y obligatorio
    username = Column(String(255), unique=True, nullable=False)
    # Contraseña (hash), obligatoria
    password = Column(String(255), nullable=False)
    # Email del usuario, único y obligatorio
    email = Column(String(255), unique=True, index=True, nullable=False)
    # Nombre completo del usuario, opcional
    full_name = Column(String(255), nullable=True)