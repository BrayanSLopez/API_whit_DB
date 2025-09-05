from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Categoria(Base):
    __tablename__ = 'categorias'
    id_categoria = Column(Integer, primary_key=True, index=True)
    nombre_categoria = Column(String(255), nullable=False)
    productos = relationship('Producto', back_populates='categoria', cascade='all, delete-orphan')

class Proveedor(Base):
    __tablename__ = 'proveedores'
    id_proveedor = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    telefono = Column(String(50), nullable=True)
    email = Column(String(255), nullable=True)
    direccion = Column(String(255), nullable=True)    
    productos = relationship('Producto', back_populates='proveedor', cascade='all, delete-orphan')

class Descuento(Base):
    __tablename__ = 'descuentos'
    id_descuento = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    porcentaje = Column(Numeric(5, 2), nullable=False)
    productos = relationship('Producto', back_populates='descuento')  

class Impuesto(Base):
    __tablename__ = 'impuestos'   
    id_iva = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    porcentaje = Column(Numeric(5, 2), nullable=False)    
    productos = relationship('Producto', back_populates='impuesto')

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