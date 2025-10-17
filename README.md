# Proyecto de gestión de productos

Base para la gestión de productos, categorías, proveedores, descuentos e impuestos. Permite operaciones CRUD sobre productos y consultas de entidades relacionadas.

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone <repo-url> .
   ```
2. Crear y activar entorno virtual (Linux):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Variables de entorno

Configurar estas variables antes de ejecutar la aplicación:

- SECRET_KEY: clave secreta para firmar tokens (ej. una cadena larga).
- DATABASE_URL: URL de conexión a la base de datos (ej. sqlite:///./db.sqlite3 o postgres://user:pass@host:port/dbname).
- PORT: puerto de la app (ej. 8000).
- DEBUG: true|false.
- ACCESS_TOKEN_EXPIRE_MINUTES: tiempo de expiración de access token (ej. 15).
- REFRESH_TOKEN_EXPIRE_DAYS: tiempo de expiración de refresh token (ej. 7).

Ejemplo (Linux):
```bash
export SECRET_KEY='cambiar_por_una_clave_segura'
export DATABASE_URL='sqlite:///./db.sqlite3'
export PORT=8000
export DEBUG=true
```

## Cómo correr en desarrollo

Opciones comunes:

- Si el proyecto expone `main.py` como punto de entrada:
  ```bash
  python main.py
  ```

- Si usa ASGI (FastAPI/Starlette) y `app` en `main.py`:
  ```bash
  pip install "uvicorn[standard]"
  uvicorn main:app --reload --host 0.0.0.0 --port ${PORT:-8000}
  ```

Acceder en el navegador: http://localhost:8000

## Ejecutar pruebas

Usar pytest (suponiendo que hay tests):
```bash
pip install pytest
pytest -q
```
Para ver cobertura (si está configurado):
```bash
pip install coverage
coverage run -m pytest
coverage report -m
```

## Roles y permisos

Roles típicos usados en el sistema:

- admin: acceso total (crear/leer/actualizar/eliminar).
- manager: gestionar productos, inventario y descuentos.
- user: consultar productos, crear pedidos (lectura limitada).
- guest: acceso público read-only limitado (si aplica).

Asignación de permisos:
- admin: todas las rutas protegidas.
- manager: rutas de products, inventory, discounts.
- user: lectura de productos y operaciones propias.
- guest: solo endpoints públicos.

## Ejemplo de tokens

Se usa JWT (ejemplo ilustrativo, no válido):

- Access token (ejemplo): eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...ACCESS_PAYLOAD...signature
- Refresh token (ejemplo): eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...REFRESH_PAYLOAD...signature

Cabecera HTTP para llamadas autenticadas:
```
Authorization: Bearer <ACCESS_TOKEN>
```

No guardar secretos en código; usar variables de entorno.

## Flujo de autenticación (resumido)

1. Cliente envía credenciales a POST /auth/login.
2. El servidor valida y responde con access_token y refresh_token.
3. Cliente usa access_token en Authorization header para llamadas protegidas.
4. Cuando expira access_token, el cliente usa refresh_token en POST /auth/refresh para obtener nuevos tokens.
5. Logout/invalidación: opcionalmente invalidar refresh_token en el servidor.

## Tabla de endpoints (resumen)

| Método | Endpoint                      | Autenticación | Roles permitidos      | Descripción |
|--------|-------------------------------|---------------|-----------------------|-------------|
| POST   | /auth/login                   | No            | —                     | Inicio de sesión, devuelve tokens |
| POST   | /auth/refresh                 | Sí (refresh)  | —                     | Renueva access token |
| POST   | /auth/logout                  | Sí            | user, manager, admin  | Invalidar refresh token |
| GET    | /products                     | Opcional      | guest,user,manager,admin | Listar productos |
| POST   | /products                     | Sí            | manager,admin         | Crear producto |
| GET    | /products/{id}                | Opcional      | guest,user,manager,admin | Obtener producto |
| PUT    | /products/{id}                | Sí            | manager,admin         | Actualizar producto |
| DELETE | /products/{id}                | Sí            | admin                 | Eliminar producto |
| GET    | /categories                   | Opcional      | guest,user,manager,admin | Listar categorías |
| POST   | /categories                   | Sí            | manager,admin         | Crear categoría |
| GET    | /suppliers                    | Opcional      | user,manager,admin    | Listar proveedores |
| POST   | /suppliers                    | Sí            | manager,admin         | Crear proveedor |
| GET    | /discounts                    | Opcional      | user,manager,admin    | Listar descuentos |
| POST   | /discounts                    | Sí            | manager,admin         | Crear descuento |
| GET    | /taxes                        | Opcional      | user,manager,admin    | Listar impuestos |
| GET    | /inventory                    | Sí            | manager,admin         | Consultar inventario |
| PUT    | /inventory/{product_id}       | Sí            | manager,admin         | Actualizar inventario |

Nota: ajustar rutas y permisos según implementación real del proyecto.

## Notas finales

- Mantener secretos en variables de entorno.
- Documentar y versionar la API (OpenAPI/Swagger recomendado).
- Añadir más tests para cobertura de endpoints y lógica de negocio.






