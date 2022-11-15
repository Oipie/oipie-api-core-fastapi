"""
User Database Model
"""
import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.dependencies.database import BaseModel
from src.core.users.domain.user import User


class UserModel(BaseModel):
    """
    This class represents a User in database model
    """

    __tablename__ = "users"

    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    nickname = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    recipes = relationship("RecipeModel")

    @staticmethod
    def from_domain_object(user: User):
        """
        Transforms to User model
        """
        return UserModel(
            uuid=user.uuid,
            nickname=user.nickname,
            email=user.email,
            password=user.password,
        )

    def to_domain_object(self) -> User:
        """
        Transforms User database model to a domain object
        """
        return User(
            user_attributes={
                "uuid": str(self.uuid),
                "nickname": self.nickname,
                "email": self.email,
                "password": self.password,
                "recipes": [str(recipe.uuid) for recipe in self.recipes],
            }
        )
