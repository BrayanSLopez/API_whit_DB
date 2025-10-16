import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from models.product_model import Categoria, Proveedor, Descuento, Impuesto, Producto
from sqlalchemy.orm import Session

class CategoriaRepository:
    """
    Repositorio para la gestión de categorías en la base de datos.
    Proporciona métodos para crear, consultar y listar categorías.
    """

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_categorias(self):
        logger.info("Obteniendo todas las categorías desde el repositorio")
        return self.db.query(Categoria).all()

    def create_categoria(self, nombre_categoria: str):
        logger.info(f"Creando categoría: {nombre_categoria}")
        new_categoria = Categoria(nombre_categoria=nombre_categoria)
        self.db.add(new_categoria)
        self.db.commit()
        self.db.refresh(new_categoria)
        return new_categoria

class ProveedorRepository:
    """
    Repositorio para la gestión de proveedores en la base de datos.
    Proporciona métodos para crear, consultar y listar proveedores.
    """

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_proveedores(self):
        logger.info("Obteniendo todos los proveedores desde el repositorio")
        return self.db.query(Proveedor).all()

    def create_proveedor(self, nombre: str, telefono: str = None, email: str = None, direccion: str = None):
        logger.info(f"Creando proveedor: {nombre}")
        new_proveedor = Proveedor(
            nombre=nombre,
            telefono=telefono,
            email=email,
            direccion=direccion
        )
        self.db.add(new_proveedor)
        self.db.commit()
        self.db.refresh(new_proveedor)
        return new_proveedor

class DescuentoRepository:
    """
    Repositorio para la gestión de descuentos en la base de datos.
    Proporciona métodos para crear, consultar y listar descuentos.
    """

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_descuentos(self):
        logger.info("Obteniendo todos los descuentos desde el repositorio")
        return self.db.query(Descuento).all()

    def create_descuento(self, nombre: str, porcentaje: float):
        logger.info(f"Creando descuento: {nombre}")
        new_descuento = Descuento(nombre=nombre, porcentaje=porcentaje)
        self.db.add(new_descuento)
        self.db.commit()
        self.db.refresh(new_descuento)
        return new_descuento

class ImpuestoRepository:
    """
    Repositorio para la gestión de impuestos en la base de datos.
    Proporciona métodos para crear, consultar y listar impuestos.
    """

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_impuestos(self):
        logger.info("Obteniendo todos los impuestos desde el repositorio")
        return self.db.query(Impuesto).all()

    def create_impuesto(self, nombre: str, porcentaje: float):
        logger.info(f"Creando impuesto: {nombre}")
        new_impuesto = Impuesto(nombre=nombre, porcentaje=porcentaje)
        self.db.add(new_impuesto)
        self.db.commit()
        self.db.refresh(new_impuesto)
        return new_impuesto

class ProductoRepository:
    """
    Repositorio para la gestión de productos en la base de datos.
    Proporciona métodos para crear, consultar, actualizar y eliminar productos.
    """

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_productos(self):
        logger.info("Obteniendo todos los productos desde el repositorio")
        return self.db.query(Producto).all()

    def get_producto_by_id(self, producto_id: int):
        logger.info(f"Buscando producto por ID: {producto_id}")
        return self.db.query(Producto).filter(Producto.id_producto == producto_id).first()

    def create_producto(self, nombre_producto: str, precio: float, stock: int,
                        id_categoria: int, id_descuento: int = None,
                        id_iva: int = None, id_proveedor: int = None):
        logger.info(f"Creando producto: {nombre_producto}")
        new_producto = Producto(
            nombre_producto=nombre_producto,
            Precio=precio,
            Stock=stock,
            id_categoria=id_categoria,
            id_descuento=id_descuento,
            id_iva=id_iva,
            id_proveedor=id_proveedor
        )
        self.db.add(new_producto)
        self.db.commit()
        self.db.refresh(new_producto)
        return new_producto

    def update_producto(self, producto_id: int, nombre_producto: str = None,
                        precio: float = None, stock: int = None,
                        id_categoria: int = None, id_descuento: int = None,
                        id_iva: int = None, id_proveedor: int = None):
        producto = self.get_producto_by_id(producto_id)
        if producto:
            logger.info(f"Actualizando producto: {producto_id}")
            if nombre_producto:
                producto.nombre_producto = nombre_producto
            if precio is not None:
                producto.Precio = precio
            if stock is not None:
                producto.Stock = stock
            if id_categoria is not None:
                producto.id_categoria = id_categoria
            if id_descuento is not None:
                producto.id_descuento = id_descuento
            if id_iva is not None:
                producto.id_iva = id_iva
            if id_proveedor is not None:
                producto.id_proveedor = id_proveedor
            self.db.commit()
            self.db.refresh(producto)
        else:
            logger.warning(f"Producto no encontrado para actualizar: {producto_id}")
        return producto

    def delete_producto(self, producto_id: int):
        producto = self.get_producto_by_id(producto_id)
        if producto:
            logger.info(f"Eliminando producto: {producto_id}")
            self.db.delete(producto)
            self.db.commit()
        else:
            logger.warning(f"Producto no encontrado para eliminar: {producto_id}")
        return producto
