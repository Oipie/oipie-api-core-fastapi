"""
Password service dependencies
"""

from src.core.shared.services.password.argon2_password import Argon2Password
from src.core.shared.services.password.password import Password


def password_hasher() -> Password:
    """
    Returns an instance of Password
    """
    return Argon2Password()
