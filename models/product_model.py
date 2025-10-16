import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from models.db import Base

"""
La clase Categoria representa una categoría de productos en el sistema.
Cada instancia corresponde a una categoría específica y está mapeada a la tabla 'categorias'.
Permite gestionar la información de las categorías y acceder a todos los productos asociados mediante una relación uno a muchos.
"""
class Categoria(Base):
    __tablename__ = 'categorias'
    id_categoria = Column(Integer, primary_key=True, index=True)
    nombre_categoria = Column(String(255), nullable=False)
    productos = relationship('Producto', back_populates='categoria', cascade='all, delete-orphan')

"""
La clase Proveedor representa un proveedor de productos.
Cada instancia corresponde a un proveedor específico y está mapeada a la tabla 'proveedores'.
Permite gestionar la información de los proveedores y acceder a todos los productos asociados mediante una relación uno a muchos.
"""
class Proveedor(Base):
    __tablename__ = 'proveedores'
    id_proveedor = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    telefono = Column(String(50), nullable=True)
    email = Column(String(255), nullable=True)
    direccion = Column(String(255), nullable=True)
    productos = relationship('Producto', back_populates='proveedor', cascade='all, delete-orphan')

"""
La clase Descuento representa un descuento aplicable a productos.
Cada instancia corresponde a un descuento específico y está mapeada a la tabla 'descuentos'.
Permite gestionar la información de los descuentos y acceder a todos los productos asociados mediante una relación uno a muchos.
"""
class Descuento(Base):
    __tablename__ = 'descuentos'
    id_descuento = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    porcentaje = Column(Numeric(5, 2), nullable=False)
    productos = relationship('Producto', back_populates='descuento')

"""
La clase Impuesto representa un impuesto aplicable a productos.
Cada instancia corresponde a un impuesto específico y está mapeada a la tabla 'impuestos'.
Permite gestionar la información de los impuestos y acceder a todos los productos asociados mediante una relación uno a muchos.
"""
class Impuesto(Base):
    __tablename__ = 'impuestos'
    id_iva = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    porcentaje = Column(Numeric(5, 2), nullable=False)
    productos = relationship('Producto', back_populates='impuesto')

"""
La clase Producto representa un producto en el sistema.
Cada instancia corresponde a un producto específico y está mapeada a la tabla 'productos'.
Permite gestionar la información de los productos y establecer relaciones con categoría, proveedor, descuento e impuesto.
"""
class Producto(Base):
    __tablename__ = 'productos'
    id_producto = Column(Integer, primary_key=True, index=True)
    nombre_producto = Column(String(255), nullable=False)
    Precio = Column(Numeric(10, 2), nullable=False)
    Stock = Column(Integer, nullable=False)
    id_categoria = Column(Integer, ForeignKey('categorias.id_categoria'))
    id_descuento = Column(Integer, ForeignKey('descuentos.id_descuento'), nullable=True)
    id_iva = Column(Integer, ForeignKey('impuestos.id_iva'), nullable=True)
    id_proveedor = Column(Integer, ForeignKey('proveedores.id_proveedor'), nullable=True)
    categoria = relationship('Categoria', back_populates='productos')
    descuento = relationship('Descuento', back_populates='productos')
    impuesto = relationship('Impuesto', back_populates='productos')
    proveedor = relationship('Proveedor', back_populates='productos')