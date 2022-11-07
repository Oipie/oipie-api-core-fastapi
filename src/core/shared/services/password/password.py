"""
Password
"""
import abc


class Password(abc.ABC):
    """
    Interface for generating and verifying passwords
    """

    @abc.abstractmethod
    def generate_from(self, plain_text: str) -> str:
        """
        Generates a hashed password from plain text
        """
        raise NotImplementedError

    @abc.abstractmethod
    def verify(self, hashed_text: str, plain_text: str) -> bool:
        """
        Verifies a password from :hashed_text and :plain_text
        """
        raise NotImplementedError
