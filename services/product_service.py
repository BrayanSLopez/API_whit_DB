from repositories.product_repository import (
    CategoriaRepository,
    ProveedorRepository,
    DescuentoRepository,
    ImpuestoRepository,
    ProductoRepository
)
from sqlalchemy.orm import Session


class CategoriaService:
    """Capa de servicios para la gestión de categorías."""

    def __init__(self, db_session: Session):
        self.repository = CategoriaRepository(db_session)

    def listar_categorias(self):
        """Recupera y retorna todas las categorías registradas en el sistema."""
        return self.repository.get_all_categorias()

    def crear_categoria(self, nombre_categoria: str):
        """Crea una nueva categoría."""
        return self.repository.create_categoria(nombre_categoria)


class ProveedorService:
    """Capa de servicios para la gestión de proveedores."""

    def __init__(self, db_session: Session):
        self.repository = ProveedorRepository(db_session)

    def listar_proveedores(self):
        """Recupera y retorna todos los proveedores registrados en el sistema."""
        return self.repository.get_all_proveedores()

    def crear_proveedor(self, nombre: str, telefono: str = None, email: str = None, direccion: str = None):
        """Crea un nuevo proveedor."""
        return self.repository.create_proveedor(nombre, telefono, email, direccion)


class DescuentoService:
    """Capa de servicios para la gestión de descuentos."""

    def __init__(self, db_session: Session):
        self.repository = DescuentoRepository(db_session)

    def listar_descuentos(self):
        """Recupera y retorna todos los descuentos registrados en el sistema."""
        return self.repository.get_all_descuentos()

    def crear_descuento(self, nombre: str, porcentaje: float):
        """Crea un nuevo descuento."""
        return self.repository.create_descuento(nombre, porcentaje)


class ImpuestoService:
    """Capa de servicios para la gestión de impuestos."""

    def __init__(self, db_session: Session):
        self.repository = ImpuestoRepository(db_session)

    def listar_impuestos(self):
        """Recupera y retorna todos los impuestos registrados en el sistema."""
        return self.repository.get_all_impuestos()

    def crear_impuesto(self, nombre: str, porcentaje: float):
        """Crea un nuevo impuesto."""
        return self.repository.create_impuesto(nombre, porcentaje)


class ProductoService:
    """Capa de servicios para la gestión de productos."""

    def __init__(self, db_session: Session):
        self.repository = ProductoRepository(db_session)

    def listar_productos(self):
        """Recupera y retorna todos los productos registrados en el sistema."""
        return self.repository.get_all_productos()

    def obtener_producto(self, producto_id: int):
        """Busca y retorna un producto específico por su ID."""
        return self.repository.get_producto_by_id(producto_id)

    def crear_producto(self, nombre_producto: str, precio: float, stock: int,
                       id_categoria: int, id_descuento: int = None,
                       id_iva: int = None, id_proveedor: int = None):
        """Crea un nuevo producto con las relaciones necesarias."""
        return self.repository.create_producto(
            nombre_producto, precio, stock,
            id_categoria, id_descuento, id_iva, id_proveedor
        )

    def actualizar_producto(self, producto_id: int, nombre_producto: str = None,
                            precio: float = None, stock: int = None,
                            id_categoria: int = None, id_descuento: int = None,
                            id_iva: int = None, id_proveedor: int = None):
        """Actualiza la información de un producto existente."""
        return self.repository.update_producto(
            producto_id, nombre_producto, precio, stock,
            id_categoria, id_descuento, id_iva, id_proveedor
        )

    def eliminar_producto(self, producto_id: int):
        """Elimina un producto del sistema según su ID."""
        return self.repository.delete_producto(producto_id)
