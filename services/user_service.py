from repositories.user_repository import UserRepository
from models.user_model import User
from werkzeug.security import generate_password_hash, check_password_hash
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UsersService:
    def __init__(self, db_session):
        self.db_session = db_session
        self.user_repo = UserRepository(db_session)  # Usamos UserRepository para manejar la creación de usuarios

    def authenticate_user(self, username: str, password: str):
        """
        Autentica a un usuario con su nombre de usuario y contraseña.
        Devuelve el usuario si las credenciales son correctas.
        """
        user = self.db_session.query(User).filter(User.username == username).first()
        logger.info(f"Authenticating user: {username}")
        if user and check_password_hash(user.password, password):
            logger.info(f"User authenticated successfully: {username}")
            return user
        logger.warning(f"Failed authentication attempt: {username}")
        return None

    def get_all_users(self):
        """
        Recupera todos los usuarios de la base de datos.
        """
        logger.info("Fetching all users")
        return self.db_session.query(User).all()

    def get_user_by_id(self, user_id: int):
        """
        Recupera un usuario específico por su ID.
        """
        logger.info(f"Fetching user by ID: {user_id}")
        return self.db_session.query(User).filter(User.id == user_id).first()

    def create_user(self, username: str, password: str, email: str, full_name: str = None):
        """
        Crea un nuevo usuario en la base de datos.
        """
        # Cifra la contraseña antes de almacenarla
        password_hashed = generate_password_hash(password)
        logger.info(f"Creating user: {username}")

        # Usamos el repositorio para crear el usuario
        user = self.user_repo.create_user(username, password_hashed, email, full_name)

        if user:
            logger.info(f"Usuario creado con éxito: {username}")
            return user
        else:
            logger.error(f"No se pudo crear el usuario: {username}")
            return None

    def update_user(self, user_id: int, username: str = None, password: str = None, email: str = None, full_name: str = None):
        """
        Actualiza la información de un usuario existente.
        """
        logger.info(f"Updating user: {user_id}")
        password_hashed = generate_password_hash(password) if password else None

        user = self.db_session.query(User).filter(User.id == user_id).first()

        if user:
            if username:
                user.username = username
            if password_hashed:
                user.password = password_hashed
            if email:
                user.email = email
            if full_name:
                user.full_name = full_name

            self.db_session.commit()
            self.db_session.refresh(user)
            logger.info(f"Usuario actualizado: {user_id}")
            return user
        else:
            logger.warning(f"Usuario no encontrado para actualizar: {user_id}")
            return None

    def delete_user(self, user_id: int):
        """
        Elimina un usuario de la base de datos.
        """
        logger.info(f"Deleting user: {user_id}")
        user = self.db_session.query(User).filter(User.id == user_id).first()

        if user:
            self.db_session.delete(user)
            self.db_session.commit()
            logger.info(f"Usuario eliminado: {user_id}")
            return user
        else:
            logger.warning(f"Usuario no encontrado para eliminar: {user_id}")
            return None
