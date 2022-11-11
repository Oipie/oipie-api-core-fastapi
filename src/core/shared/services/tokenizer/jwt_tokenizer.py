"""
JwtTokenizer
"""
import jwt
from src.core.shared.services.tokenizer.tokenizer import Tokenizer
from src.core.shared.services.tokenizer.errors.invalid_token_error import (
    InvalidTokenError,
)


class JwtTokenizer(Tokenizer):
    """
    This class uses JSON Web Token strategy to encode and decode payloads
    """

    ALGORITHM = "HS256"

    def __init__(self, secret: str) -> None:
        self._secret = secret

    def encode(self, payload: dict) -> str:
        return jwt.encode(payload, self._secret, algorithm=JwtTokenizer.ALGORITHM)

    def decode(self, token: str) -> dict:
        try:
            return jwt.decode(token, self._secret, algorithms=[JwtTokenizer.ALGORITHM])
        except Exception as error:
            raise InvalidTokenError from error
