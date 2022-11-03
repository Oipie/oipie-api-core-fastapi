"""
    Domain users repository interface module
"""
import abc
from src.core.users.domain.user import User


class UsersRepository(abc.ABC):
    """
    Domain users repository interface
    """

    @abc.abstractmethod
    def find_by_email(self, email: str) -> User or None:
        """
        Finds user on repository by email
        """
        raise NotImplementedError

    @abc.abstractmethod
    def find_by_nickname(self, nickname: str) -> User or None:
        """
        Finds user on repository by nickname
        """
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, user: User) -> User:
        """
        Inserts user to repository
        """
        raise NotImplementedError
