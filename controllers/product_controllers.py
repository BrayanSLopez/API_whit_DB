import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.product_service import (
    CategoriaService,
    ProveedorService,
    DescuentoService,
    ImpuestoService,
    ProductoService
)
from config.database import get_db_session

# Crear blueprint para productos
product_bp = Blueprint('product_bp', __name__)

# Instancias globales de servicios (en producción, usar contexto de app o request)
db_session = get_db_session()
categoria_service = CategoriaService(db_session)
proveedor_service = ProveedorService(db_session)
descuento_service = DescuentoService(db_session)
impuesto_service = ImpuestoService(db_session)
producto_service = ProductoService(db_session)

# -------------------- CATEGORÍAS --------------------
@product_bp.route('/categorias', methods=['GET'])
@jwt_required()
def get_categorias():
    logger.info("Consulta de todas las categorías")
    categorias = categoria_service.listar_categorias()
    return jsonify([{'id': c.id_categoria, 'nombre': c.nombre_categoria} for c in categorias]), 200, {'Content-Type': 'application/json; charset=utf-8'}

@product_bp.route('/categorias', methods=['POST'])
def create_categoria():
    data = request.get_json()
    nombre = data.get('nombre_categoria')
    if not nombre:
        logger.warning("Intento de crear categoría sin nombre")
        return jsonify({'error': 'El nombre de la categoría es obligatorio'}), 400, {'Content-Type': 'application/json; charset=utf-8'}
    categoria = categoria_service.crear_categoria(nombre)
    logger.info(f"Categoría creada: {nombre}")
    return jsonify({'id': categoria.id_categoria, 'nombre': categoria.nombre_categoria}), 201, {'Content-Type': 'application/json; charset=utf-8'}


# -------------------- PROVEEDORES --------------------
@product_bp.route('/proveedores', methods=['GET'])
@jwt_required()
def get_proveedores():
    logger.info("Consulta de todos los proveedores")
    proveedores = proveedor_service.listar_proveedores()
    return jsonify([
        {
            'id': p.id_proveedor,
            'nombre': p.nombre,
            'telefono': p.telefono,
            'email': p.email,
            'direccion': p.direccion
        } for p in proveedores
    ]), 200, {'Content-Type': 'application/json; charset=utf-8'}

@product_bp.route('/proveedores', methods=['POST'])
def create_proveedor():
    data = request.get_json()
    nombre = data.get('nombre')
    if not nombre:
        logger.warning("Intento de crear proveedor sin nombre")
        return jsonify({'error': 'El nombre del proveedor es obligatorio'}), 400, {'Content-Type': 'application/json; charset=utf-8'}
    proveedor = proveedor_service.crear_proveedor(
        nombre,
        data.get('telefono'),
        data.get('email'),
        data.get('direccion')
    )
    logger.info(f"Proveedor creado: {nombre}")
    return jsonify({
        'id': proveedor.id_proveedor,
        'nombre': proveedor.nombre,
        'telefono': proveedor.telefono,
        'email': proveedor.email,
        'direccion': proveedor.direccion
    }), 201, {'Content-Type': 'application/json; charset=utf-8'}


# -------------------- DESCUENTOS --------------------
@product_bp.route('/descuentos', methods=['GET'])
@jwt_required()
def get_descuentos():
    logger.info("Consulta de todos los descuentos")
    descuentos = descuento_service.listar_descuentos()
    return jsonify([{'id': d.id_descuento, 'nombre': d.nombre, 'porcentaje': float(d.porcentaje)} for d in descuentos]), 200, {'Content-Type': 'application/json; charset=utf-8'}

@product_bp.route('/descuentos', methods=['POST'])
def create_descuento():
    data = request.get_json()
    nombre = data.get('nombre')
    porcentaje = data.get('porcentaje')
    if not nombre or porcentaje is None:
        logger.warning("Intento de crear descuento sin nombre o porcentaje")
        return jsonify({'error': 'El nombre y porcentaje son obligatorios'}), 400, {'Content-Type': 'application/json; charset=utf-8'}
    descuento = descuento_service.crear_descuento(nombre, porcentaje)
    logger.info(f"Descuento creado: {nombre}")
    return jsonify({'id': descuento.id_descuento, 'nombre': descuento.nombre, 'porcentaje': float(descuento.porcentaje)}), 201, {'Content-Type': 'application/json; charset=utf-8'}


# -------------------- IMPUESTOS --------------------
@product_bp.route('/impuestos', methods=['GET'])
@jwt_required()
def get_impuestos():
    logger.info("Consulta de todos los impuestos")
    impuestos = impuesto_service.listar_impuestos()
    return jsonify([{'id': i.id_iva, 'nombre': i.nombre, 'porcentaje': float(i.porcentaje)} for i in impuestos]), 200, {'Content-Type': 'application/json; charset=utf-8'}

@product_bp.route('/impuestos', methods=['POST'])
def create_impuesto():
    data = request.get_json()
    nombre = data.get('nombre')
    porcentaje = data.get('porcentaje')
    if not nombre or porcentaje is None:
        logger.warning("Intento de crear impuesto sin nombre o porcentaje")
        return jsonify({'error': 'El nombre y porcentaje son obligatorios'}), 400, {'Content-Type': 'application/json; charset=utf-8'}
    impuesto = impuesto_service.crear_impuesto(nombre, porcentaje)
    logger.info(f"Impuesto creado: {nombre}")
    return jsonify({'id': impuesto.id_iva, 'nombre': impuesto.nombre, 'porcentaje': float(impuesto.porcentaje)}), 201, {'Content-Type': 'application/json; charset=utf-8'}


# -------------------- PRODUCTOS --------------------
@product_bp.route('/productos', methods=['GET'])
@jwt_required()
def get_productos():
    logger.info("Consulta de todos los productos")
    productos = producto_service.listar_productos()
    return jsonify([
        {
            'id': p.id_producto,
            'nombre': p.nombre_producto,
            'precio': float(p.Precio),
            'stock': p.Stock,
            'categoria': p.id_categoria,
            'descuento': p.id_descuento,
            'iva': p.id_iva,
            'proveedor': p.id_proveedor
        } for p in productos
    ]), 200, {'Content-Type': 'application/json; charset=utf-8'}

@product_bp.route('/productos/<int:producto_id>', methods=['GET'])
def get_producto(producto_id):
    producto = producto_service.obtener_producto(producto_id)
    if producto:
        logger.info(f"Consulta de producto por ID: {producto_id}")
        return jsonify({
            'id': producto.id_producto,
            'nombre': producto.nombre_producto,
            'precio': float(producto.Precio),
            'stock': producto.Stock,
            'categoria': producto.id_categoria,
            'descuento': producto.id_descuento,
            'iva': producto.id_iva,
            'proveedor': producto.id_proveedor
        }), 200, {'Content-Type': 'application/json; charset=utf-8'}
    logger.warning(f"Producto no encontrado: {producto_id}")
    return jsonify({'error': 'Producto no encontrado'}), 404, {'Content-Type': 'application/json; charset=utf-8'}

@product_bp.route('/productos', methods=['POST'])
def create_producto():
    data = request.get_json()
    nombre = data.get('nombre_producto')
    precio = data.get('precio')
    stock = data.get('stock')
    id_categoria = data.get('id_categoria')

    if not nombre or precio is None or stock is None or id_categoria is None:
        logger.warning("Intento de crear producto sin datos obligatorios")
        return jsonify({'error': 'Nombre, precio, stock y categoría son obligatorios'}), 400, {'Content-Type': 'application/json; charset=utf-8'}

    producto = producto_service.crear_producto(
        nombre,
        precio,
        stock,
        id_categoria,
        data.get('id_descuento'),
        data.get('id_iva'),
        data.get('id_proveedor')
    )
    logger.info(f"Producto creado: {nombre}")
    return jsonify({
        'id': producto.id_producto,
        'nombre': producto.nombre_producto,
        'precio': float(producto.Precio),
        'stock': producto.Stock,
        'categoria': producto.id_categoria,
        'descuento': producto.id_descuento,
        'iva': producto.id_iva,
        'proveedor': producto.id_proveedor
    }), 201, {'Content-Type': 'application/json; charset=utf-8'}

@product_bp.route('/productos/<int:producto_id>', methods=['PUT'])
def update_producto(producto_id):
    data = request.get_json()
    producto = producto_service.actualizar_producto(
        producto_id,
        data.get('nombre_producto'),
        data.get('precio'),
        data.get('stock'),
        data.get('id_categoria'),
        data.get('id_descuento'),
        data.get('id_iva'),
        data.get('id_proveedor')
    )
    if producto:
        logger.info(f"Producto actualizado: {producto_id}")
        return jsonify({
            'id': producto.id_producto,
            'nombre': producto.nombre_producto,
            'precio': float(producto.Precio),
            'stock': producto.Stock,
            'categoria': producto.id_categoria,
            'descuento': producto.id_descuento,
            'iva': producto.id_iva,
            'proveedor': producto.id_proveedor
        }), 200, {'Content-Type': 'application/json; charset=utf-8'}
    logger.warning(f"Producto no encontrado para actualizar: {producto_id}")
    return jsonify({'error': 'Producto no encontrado'}), 404, {'Content-Type': 'application/json; charset=utf-8'}

@product_bp.route('/productos/<int:producto_id>', methods=['DELETE'])
def delete_producto(producto_id):
    producto = producto_service.eliminar_producto(producto_id)
    if producto:
        logger.info(f"Producto eliminado: {producto_id}")
        return jsonify({'message': 'Producto eliminado'}), 200, {'Content-Type': 'application/json; charset=utf-8'}
    logger.warning(f"Producto no encontrado para eliminar: {producto_id}")
    return jsonify({'error': 'Producto no encontrado'}), 404, {'Content-Type': 'application/json; charset=utf-8'}
