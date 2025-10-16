from repositories.user_repository import UserRepository
from models.user_model import User
from werkzeug.security import generate_password_hash, check_password_hash
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UsersService:
    def __init__(self, db_session):
        self.db_session = db_session

    def authenticate_user(self, username: str, password: str):
        user = self.db_session.query(User).filter(User.username == username).first()
        logger.info(f"Authenticating user: {username}")
        if user and check_password_hash(user.password, password):
            logger.info(f"User authenticated successfully: {username}")
            return user
        logger.warning(f"Failed authentication attempt: {username}")
        return None

    def get_all_users(self):
        logger.info("Fetching all users")
        return self.db_session.query(User).all()

    def get_user_by_id(self, user_id: int):
        logger.info(f"Fetching user by ID: {user_id}")
        return self.db_session.query(User).filter(User.id == user_id).first()

    def create_user(self, username: str, password: str, email: str, full_name: str = None):
        password_hashed = generate_password_hash(password)
        logger.info(f"Creating user: {username}")
        return self.db_session.query(User).filter(User.username == username).first()

    def update_user(self, user_id: int, username: str = None, password: str = None, email: str = None, full_name: str = None):
        logger.info(f"Updating user: {user_id}")
        password_hashed = generate_password_hash(password) if password else None
        return self.db_session.query(User).filter(User.id == user_id).first()

    def delete_user(self, user_id: int):
        logger.info(f"Deleting user: {user_id}")
        return self.db_session.query(User).filter(User.id == user_id).delete()