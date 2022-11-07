"""
Fake Password class for testing purposes
"""
from src.core.shared.services.password.password import Password


class PlainTextPassword(Password):
    """
    Class to generate fake passwords for texting purposes
    """

    def generate_from(self, plain_text: str) -> str:
        """
        Returns same string without hashing it
        """
        return plain_text

    def verify(self, hashed_text: str, plain_text: str) -> bool:
        """
        Verifies a password from :hashed_text and :plain_text
        """
        return hashed_text == plain_text
