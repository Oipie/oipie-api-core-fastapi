"""
JWT parameters
"""
import os

JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "secret")
