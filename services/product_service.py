import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from repositories.product_repository import (
    CategoriaRepository,
    ProveedorRepository,
    DescuentoRepository,
    ImpuestoRepository,
    ProductoRepository
)
from sqlalchemy.orm import Session

"""
Librerías utilizadas:
- repositories.product_repository: Proporciona las clases de repositorio para la gestión de productos y sus entidades relacionadas.
- sqlalchemy.orm.Session: Permite manejar la sesión de la base de datos para realizar operaciones transaccionales.
"""

class CategoriaService:
    """
    Capa de servicios para la gestión de categorías.
    Orquesta la lógica de negocio relacionada con las categorías, utilizando el repositorio para acceder a los datos.
    """
    def __init__(self, db_session: Session):
        self.repository = CategoriaRepository(db_session)
        logger.info("Servicio de categorías inicializado")

    def listar_categorias(self):
        logger.info("Listando todas las categorías")
        return self.repository.get_all_categorias()

    def crear_categoria(self, nombre_categoria: str):
        logger.info(f"Creando categoría: {nombre_categoria}")
        return self.repository.create_categoria(nombre_categoria)

class ProveedorService:
    """
    Capa de servicios para la gestión de proveedores.
    Orquesta la lógica de negocio relacionada con los proveedores, utilizando el repositorio para acceder a los datos.
    """
    def __init__(self, db_session: Session):
        self.repository = ProveedorRepository(db_session)
        logger.info("Servicio de proveedores inicializado")

    def listar_proveedores(self):
        logger.info("Listando todos los proveedores")
        return self.repository.get_all_proveedores()

    def crear_proveedor(self, nombre: str, telefono: str = None, email: str = None, direccion: str = None):
        logger.info(f"Creando proveedor: {nombre}")
        return self.repository.create_proveedor(nombre, telefono, email, direccion)

class DescuentoService:
    """
    Capa de servicios para la gestión de descuentos.
    Orquesta la lógica de negocio relacionada con los descuentos, utilizando el repositorio para acceder a los datos.
    """
    def __init__(self, db_session: Session):
        self.repository = DescuentoRepository(db_session)
        logger.info("Servicio de descuentos inicializado")

    def listar_descuentos(self):
        logger.info("Listando todos los descuentos")
        return self.repository.get_all_descuentos()

    def crear_descuento(self, nombre: str, porcentaje: float):
        logger.info(f"Creando descuento: {nombre}")
        return self.repository.create_descuento(nombre, porcentaje)

class ImpuestoService:
    """
    Capa de servicios para la gestión de impuestos.
    Orquesta la lógica de negocio relacionada con los impuestos, utilizando el repositorio para acceder a los datos.
    """
    def __init__(self, db_session: Session):
        self.repository = ImpuestoRepository(db_session)
        logger.info("Servicio de impuestos inicializado")

    def listar_impuestos(self):
        logger.info("Listando todos los impuestos")
        return self.repository.get_all_impuestos()

    def crear_impuesto(self, nombre: str, porcentaje: float):
        logger.info(f"Creando impuesto: {nombre}")
        return self.repository.create_impuesto(nombre, porcentaje)

class ProductoService:
    """
    Capa de servicios para la gestión de productos.
    Orquesta la lógica de negocio relacionada con los productos, utilizando el repositorio para acceder a los datos.
    """
    def __init__(self, db_session: Session):
        self.repository = ProductoRepository(db_session)
        logger.info("Servicio de productos inicializado")

    def listar_productos(self):
        logger.info("Listando todos los productos")
        return self.repository.get_all_productos()

    def obtener_producto(self, producto_id: int):
        logger.info(f"Obteniendo producto por ID: {producto_id}")
        return self.repository.get_producto_by_id(producto_id)

    def crear_producto(self, nombre_producto: str, precio: float, stock: int,
                       id_categoria: int, id_descuento: int = None,
                       id_iva: int = None, id_proveedor: int = None):
        logger.info(f"Creando producto: {nombre_producto}")
        return self.repository.create_producto(
            nombre_producto, precio, stock,
            id_categoria, id_descuento, id_iva, id_proveedor
        )

    def actualizar_producto(self, producto_id: int, nombre_producto: str = None,
                            precio: float = None, stock: int = None,
                            id_categoria: int = None, id_descuento: int = None,
                            id_iva: int = None, id_proveedor: int = None):
        logger.info(f"Actualizando producto: {producto_id}")
        return self.repository.update_producto(
            producto_id, nombre_producto, precio, stock,
            id_categoria, id_descuento, id_iva, id_proveedor
        )

    def eliminar_producto(self, producto_id: int):
        logger.info(f"Eliminando producto: {producto_id}")
        return self.repository.delete_producto(producto_id)
