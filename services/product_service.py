from sqlalchemy.orm import Session
from models import Categoria, Proveedor, Descuento, Impuesto, Producto


class CategoriaRepository:
    """Repositorio para la gestión de categorías."""

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_categorias(self):
        """Recupera todas las categorías."""
        return self.db.query(Categoria).all()

    def create_categoria(self, nombre_categoria: str):
        """Crea una nueva categoría."""
        new_categoria = Categoria(nombre_categoria=nombre_categoria)
        self.db.add(new_categoria)
        self.db.commit()
        self.db.refresh(new_categoria)
        return new_categoria


class ProveedorRepository:
    """Repositorio para la gestión de proveedores."""

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_proveedores(self):
        """Recupera todos los proveedores."""
        return self.db.query(Proveedor).all()

    def create_proveedor(self, nombre: str, telefono: str = None, email: str = None, direccion: str = None):
        """Crea un nuevo proveedor."""
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
    """Repositorio para la gestión de descuentos."""

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_descuentos(self):
        """Recupera todos los descuentos."""
        return self.db.query(Descuento).all()

    def create_descuento(self, nombre: str, porcentaje: float):
        """Crea un nuevo descuento."""
        new_descuento = Descuento(nombre=nombre, porcentaje=porcentaje)
        self.db.add(new_descuento)
        self.db.commit()
        self.db.refresh(new_descuento)
        return new_descuento


class ImpuestoRepository:
    """Repositorio para la gestión de impuestos."""

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_impuestos(self):
        """Recupera todos los impuestos."""
        return self.db.query(Impuesto).all()

    def create_impuesto(self, nombre: str, porcentaje: float):
        """Crea un nuevo impuesto."""
        new_impuesto = Impuesto(nombre=nombre, porcentaje=porcentaje)
        self.db.add(new_impuesto)
        self.db.commit()
        self.db.refresh(new_impuesto)
        return new_impuesto


class ProductoRepository:
    """Repositorio para la gestión de productos."""

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_productos(self):
        """Recupera todos los productos con sus relaciones."""
        return self.db.query(Producto).all()

    def get_producto_by_id(self, producto_id: int):
        """Obtiene un producto por ID."""
        return self.db.query(Producto).filter(Producto.id_producto == producto_id).first()

    def create_producto(self, nombre_producto: str, precio: float, stock: int,
                        id_categoria: int, id_descuento: int = None,
                        id_iva: int = None, id_proveedor: int = None):
        """Crea un nuevo producto."""
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
        """Actualiza los datos de un producto."""
        producto = self.get_producto_by_id(producto_id)
        if not producto:
            return None

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
        return producto

    def delete_producto(self, producto_id: int):
        """Elimina un producto por ID."""
        producto = self.get_producto_by_id(producto_id)
        if producto:
            self.db.delete(producto)
            self.db.commit()
        return producto
