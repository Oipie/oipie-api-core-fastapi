"""
Tests to check User class
"""
from user import User, UserAttributes
from src.tests.fixtures.user_fixture import JANE, JOHN


def test_serialize_is_ok():
    """
    Checks serialize serializes a user as expected
    """
    user_attributes: UserAttributes = JOHN
    user = User(user_attributes)

    result = user.serialize()

    assert result["id_"] == user_attributes["id_"]
    assert result["nickname"] == user_attributes["nickname"]
    assert result["email"] == user_attributes["email"]
    assert result["uuid"] == user_attributes["uuid"]


def test_serialize_is_not_equal():
    """
    Checks serialize serializes a user differently of another
    """
    user_attributes: UserAttributes = JOHN
    user_attributes_changed: UserAttributes = JANE
    user = User(user_attributes_changed)

    result = user.serialize()

    assert result != user_attributes


def test_create_creates_user():
    """
    Checks creates create a new domain User
    """
    user_attributes: UserAttributes = JOHN
    user = User.create(
        user_attributes["nickname"], user_attributes["email"], user_attributes["password"]
    )

    assert user.uuid is not None
    assert user.nickname == user_attributes["nickname"]
    assert user.email == user_attributes["email"]
    assert user.password == user_attributes["password"]
