from models.user_model import User
from sqlalchemy.orm import Session

class UserRepository:
    """
    Repositorio para la gestión de usuarios en la base de datos.
    Proporciona métodos para crear, consultar, actualizar y eliminar usuarios.
    """

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_users(self):
        """
        Recupera todos los usuarios almacenados en la base de datos.
        Utiliza una consulta ORM para obtener todas las instancias de la clase User,
        permitiendo así listar todos los usuarios registrados en el sistema. Es útil para
        mostrar catálogos, listados generales o para operaciones que requieran acceder
        a la colección completa de usuarios.
        """
        return self.db.query(User).all()

    def get_user_by_id(self, user_id: int):
        """
        Busca y retorna un usuario específico según su identificador único (ID).
        Realiza una consulta filtrando por el campo 'id' de la tabla User. Es útil
        para obtener detalles de un usuario concreto, por ejemplo, al consultar su
        información o al realizar operaciones de actualización o eliminación.
        Devuelve la instancia de User si existe, o None si no se encuentra.
        """
        return self.db.query(User).filter(User.id == user_id).first()

    def create_user(self, username: str, password: str, email: str, full_name: str = None):
        """
        Crea y almacena un nuevo usuario en la base de datos.
        Recibe el nombre de usuario, contraseña, correo electrónico y nombre completo como parámetros,
        instancia un nuevo objeto User y lo agrega a la sesión de la base de datos. Tras confirmar la transacción,
        retorna el nuevo usuario creado, incluyendo su ID asignado automáticamente.
        Es útil para registrar nuevos usuarios en el sistema.
        """
        new_user = User(username=username, password=password, email=email, full_name=full_name)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def update_user(self, user_id: int, username: str = None, password: str = None, email: str = None, full_name: str = None):
        """
        Actualiza la información de un usuario existente en la base de datos.
        Permite modificar el nombre de usuario, contraseña, correo electrónico y nombre completo del usuario identificado por su ID.
        Si el usuario existe y se proporcionan nuevos valores, se actualiza el registro y se guarda el cambio en la base de datos.
        Devuelve el usuario actualizado o None si no existe.
        """
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        if username is not None:
            user.username = username
        if password is not None:
            user.password = password
        if email is not None:
            user.email = email
        if full_name is not None:
            user.full_name = full_name
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def delete_user(self, user_id: int):
        """
        Elimina un usuario de la base de datos por su ID.
        Si el usuario existe, lo elimina y confirma la transacción.
        Devuelve True si se eliminó, False si no existe.
        """
        user = self.get_user_by_id(user_id)
        if not user:
            return False
        self.db.delete(user)
        self.db.commit()
        return True