from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Categoria(Base):
    __tablename__ = 'categorias'
    id_categoria = Column(Integer, primary_key=True, index=True)
    nombre_categoria = Column(String(255), nullable=False)
    productos = relationship('Producto', back_populates='categoria', cascade='all, delete-orphan')

class Producto(Base):
    __tablename__ = 'productos'
    id_producto = Column(Integer, primary_key=True, index=True)
    nombre_producto = Column(String(255), nullable=False)
    Precio = Column(Numeric(10, 2), nullable=False)
    Stock = Column(Integer, nullable=False)
    id_categoria = Column(Integer, ForeignKey('categorias.id_categoria'))
    categoria = relationship('Categoria', back_populates='productos')