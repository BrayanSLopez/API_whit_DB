import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
        permitiendo así listar todos los usuarios registrados en el sistema.
        """
        logger.info("Obteniendo todos los usuarios desde el repositorio")
        return self.db.query(User).all()

    def get_user_by_id(self, user_id: int):
        """
        Busca y retorna un usuario específico según su identificador único (ID).
        Devuelve la instancia de User si existe, o None si no se encuentra.
        """
        logger.info(f"Buscando usuario por ID: {user_id}")
        return self.db.query(User).filter(User.id == user_id).first()

    def create_user(self, username: str, password: str, email: str, full_name: str = None):
        """
        Crea y almacena un nuevo usuario en la base de datos.
        Recibe el nombre de usuario, contraseña, correo electrónico y nombre completo como parámetros,
        instancia un nuevo objeto User y lo agrega a la sesión de la base de datos.
        Tras confirmar la transacción, retorna el nuevo usuario creado.
        """
        logger.info(f"Creando usuario: {username}")
        new_user = User(username=username, password=password, email=email, full_name=full_name)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def update_user(self, user_id: int, username: str = None, password: str = None, email: str = None, full_name: str = None):
        """
        Actualiza la información de un usuario existente en la base de datos.
        Permite modificar el nombre de usuario, contraseña, correo electrónico y nombre completo del usuario identificado por su ID.
        Devuelve el usuario actualizado o None si no existe.
        """
        user = self.get_user_by_id(user_id)
        if user:
            logger.info(f"Actualizando usuario: {user_id}")
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
        logger.warning(f"Usuario no encontrado para actualizar: {user_id}")
        return None

    def delete_user(self, user_id: int):
        """
        Elimina un usuario de la base de datos según su identificador único (ID).
        Busca el usuario correspondiente y, si existe, lo elimina de la base de datos y
        confirma la transacción. Devuelve la instancia del usuario eliminado o None si
        no se encuentra el usuario.
        """
        user = self.get_user_by_id(user_id)
        if user:
            logger.info(f"Eliminando usuario: {user_id}")
            self.db.delete(user)
            self.db.commit()
            return user
        logger.warning(f"Usuario no encontrado para eliminar: {user_id}")
        return None