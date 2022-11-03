"""
SQLAlchemy repository for Users
"""
from typing import Optional
from sqlalchemy.orm import Session
from src.core.users.domain.user import User
from src.core.users.domain.users_repository import UsersRepository
from src.core.users.infrastructure.user_model import UserModel


class UsersRepositorySQLAlchemy(UsersRepository):
    """
    This class manages database connection to query within users table
    """

    model = UserModel

    def __init__(self, session: Session):
        self.session = session

    def find_by_email(self, email: str) -> Optional[User]:
        """
        Tries to find an user in database by their email
        """
        user_model: Optional[UserModel] = (
            self.session.query(self.model).filter_by(email=email).one_or_none()
        )
        if user_model is None:
            return None

        return user_model.to_domain_object()

    def find_by_nickname(self, nickname: str) -> Optional[User]:
        """
        Tries to find an user in database by their nickname
        """

        user_model: Optional[UserModel] = (
            self.session.query(self.model).filter_by(nickname=nickname).one_or_none()
        )
        if user_model is None:
            return None

        return user_model.to_domain_object()

    def create(self, user: User) -> User:
        """
        Inserts a new user to the database
        """
        user_model = UserModel.from_domain_object(user)

        self.session.add(user_model)
        self.session.flush()
        self.session.commit()
        self.session.refresh(user_model)

        return user_model.to_domain_object()
