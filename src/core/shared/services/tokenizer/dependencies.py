"""
todo
"""

from src.config.jwt import JWT_SECRET_KEY
from src.core.shared.services.tokenizer.jwt_tokenizer import JwtTokenizer
from src.core.shared.services.tokenizer.tokenizer import Tokenizer


def tokenizer() -> Tokenizer:
    """
    Returns JWT Tokenizer instance
    """

    return JwtTokenizer(JWT_SECRET_KEY)
