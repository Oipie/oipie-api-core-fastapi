"""
Argon2 password generator
"""
from argon2 import PasswordHasher
from argon2.exceptions import VerificationError

from src.core.shared.services.password.password import Password


class Argon2Password(Password):
    """
    Class to generate passwords hashed with Argon2 algorithm
    """

    def __init__(self) -> None:
        self._password_hasher = PasswordHasher()

    def generate_from(self, plain_text: str) -> str:
        """
        Returns string hashed with Argon2
        """
        return self._password_hasher.hash(plain_text)

    def verify(self, hashed_text: str, plain_text: str) -> bool:
        """
        Verifies if hashed string matches plain text
        """
        try:
            return self._password_hasher.verify(hashed_text, plain_text)
        except VerificationError:
            return False
