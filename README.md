# Proyecto de gestion de productos

El proyecto es una base para la gestion de productos y sus diferentes dependencias

## Descripción General
El sistema permite crear productos, categorias, proveedores, descuentos y impuestos, se gestionaran los productos, su inventario y se relacionaran con su categoria, su proveedor y descuestos o impuestos si aplica.
Permite crear, consultar, actualizar y eliminar productos, asi como crear y consultar categorias, proveedores, descuentos y impuestos. 

**Instala las dependencias del proyecto:**
  ```bash
     pip install -r requirements.txt
  ```
**Iniciar el proyecto:**
  ```bash
       python main.py
  ```
## Arquitectura
Se esta manejando una arquitectura por capaz, la cual permite organizar responsabilidades de mejor manera




Si quiere probar el flujo para saber si primero esta intentando crear la conexion con MySQL, cree un archivo .env y ponga la direccion de coneccion con su MySQL
Ejemplo: MYSQL_URI=mysql+pymysql://root:mipassword@localhost:3306/mi_base
