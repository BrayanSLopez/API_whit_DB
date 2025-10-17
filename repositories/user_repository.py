import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from models.user_model import User
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

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
        try:
            logger.info("Obteniendo todos los usuarios desde el repositorio")
            return self.db.query(User).all()
        except SQLAlchemyError as e:
            logger.error(f"Error al obtener todos los usuarios: {str(e)}")
            return []

    def get_user_by_id(self, user_id: int):
        """
        Busca y retorna un usuario específico según su identificador único (ID).
        Devuelve la instancia de User si existe, o None si no se encuentra.
        """
        try:
            logger.info(f"Buscando usuario por ID: {user_id}")
            return self.db.query(User).filter(User.id == user_id).first()
        except SQLAlchemyError as e:
            logger.error(f"Error al obtener usuario por ID {user_id}: {str(e)}")
            return None

    def get_user_by_username(self, username: str):
        """
        Busca y retorna un usuario por su nombre de usuario.
        """
        try:
            logger.info(f"Buscando usuario por username: {username}")
            return self.db.query(User).filter(User.username == username).first()
        except SQLAlchemyError as e:
            logger.error(f"Error al obtener usuario por username {username}: {str(e)}")
            return None

    def get_user_by_email(self, email: str):
        """
        Busca y retorna un usuario por su email.
        """
        try:
            logger.info(f"Buscando usuario por email: {email}")
            return self.db.query(User).filter(User.email == email).first()
        except SQLAlchemyError as e:
            logger.error(f"Error al obtener usuario por email {email}: {str(e)}")
            return None

    def create_user(self, username: str, password: str, email: str, full_name: str = None):
        """
        Crea y almacena un nuevo usuario en la base de datos.
        Recibe el nombre de usuario, contraseña, correo electrónico y nombre completo como parámetros,
        instancia un nuevo objeto User y lo agrega a la sesión de la base de datos.
        Tras confirmar la transacción, retorna el nuevo usuario creado.
        """
        try:
            # Verificar si el usuario o email ya existen
            existing_user = self.get_user_by_username(username)
            if existing_user:
                logger.warning(f"Intento de crear usuario con username existente: {username}")
                return None
            
            existing_email = self.get_user_by_email(email)
            if existing_email:
                logger.warning(f"Intento de crear usuario con email existente: {email}")
                return None

            # Crear una instancia de usuario con los datos proporcionados
            logger.info(f"Creando usuario: {username}")
            new_user = User(username=username, password=password, email=email, full_name=full_name)
            
            # Agregar el nuevo usuario a la base de datos y confirmar la transacción
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)  # Refresca la instancia del objeto para obtener los datos actualizados

            logger.info(f"Usuario creado con éxito: {username}")
            return new_user
            
        except IntegrityError as e:
            self.db.rollback()
            logger.error(f"Error de integridad al crear usuario {username}: {str(e)}")
            return None
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Error de base de datos al crear usuario {username}: {str(e)}")
            return None
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error inesperado al crear usuario {username}: {str(e)}")
            return None

    def update_user(self, user_id: int, username: str = None, password: str = None, email: str = None, full_name: str = None):
        """
        Actualiza la información de un usuario existente en la base de datos.
        Permite modificar el nombre de usuario, contraseña, correo electrónico y nombre completo del usuario identificado por su ID.
        Devuelve el usuario actualizado o None si no existe.
        """
        try:
            user = self.get_user_by_id(user_id)
            if user:
                logger.info(f"Actualizando usuario: {user_id}")
                
                # Verificar unicidad si se está cambiando username
                if username is not None and username != user.username:
                    existing_user = self.get_user_by_username(username)
                    if existing_user:
                        logger.warning(f"Username ya existe: {username}")
                        return None
                
                # Verificar unicidad si se está cambiando email
                if email is not None and email != user.email:
                    existing_email = self.get_user_by_email(email)
                    if existing_email:
                        logger.warning(f"Email ya existe: {email}")
                        return None
                
                # Actualizar campos
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
                logger.info(f"Usuario actualizado: {user_id}")
                return user
                
            logger.warning(f"Usuario no encontrado para actualizar: {user_id}")
            return None
            
        except IntegrityError as e:
            self.db.rollback()
            logger.error(f"Error de integridad al actualizar usuario {user_id}: {str(e)}")
            return None
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Error de base de datos al actualizar usuario {user_id}: {str(e)}")
            return None

    def delete_user(self, user_id: int):
        """
        Elimina un usuario de la base de datos según su identificador único (ID).
        Busca el usuario correspondiente y, si existe, lo elimina de la base de datos y
        confirma la transacción. Devuelve la instancia del usuario eliminado o None si
        no se encuentra el usuario.
        """
        try:
            user = self.get_user_by_id(user_id)
            if user:
                logger.info(f"Eliminando usuario: {user_id}")
                self.db.delete(user)
                self.db.commit()
                logger.info(f"Usuario eliminado: {user_id}")
                return user
            logger.warning(f"Usuario no encontrado para eliminar: {user_id}")
            return None
            
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Error de base de datos al eliminar usuario {user_id}: {str(e)}")
            return None
