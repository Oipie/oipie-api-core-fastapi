"""
Process bearer token to take information from it
"""

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.core.shared.services.tokenizer.dependencies import tokenizer
from src.core.shared.services.tokenizer.tokenizer import Tokenizer

from src.shared.models.user_token_data import UserTokenData


def get_user_token(
    tokenizer_service: Tokenizer = Depends(tokenizer),
    token: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> UserTokenData:
    """
    Process JWT and generate a UserTokenData object
    """

    jwt = tokenizer_service.decode(token.credentials)

    return UserTokenData(email=jwt["email"], nickname=jwt["nickname"])
