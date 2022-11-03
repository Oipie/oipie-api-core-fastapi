"""
User fixtures
"""
from src.core.users.domain.user import UserAttributes

JOHN: UserAttributes = {
    "uuid": "c6077573-cb45-49a7-94fb-6c6dec9b4d1a",
    "nickname": "TheRealJohnDoe",
    "email": "john.doe@domain.com",
    "password": "123456",
}

JANE: UserAttributes = {
    "uuid": "a949e5d3-5e13-4998-9f56-a95fc0f7103c",
    "nickname": "TheRealJaneDoe",
    "email": "jane.doe@domain.com",
    "password": "654321",
}
