"""
    Database configuration
"""
import os
from typing import Optional


DATABASE_CONFIG = {
    "host": os.environ.get("DATABASE_HOST", "localhost"),
    "port": int(
        os.environ.get("DATABASE_PORT", "5432"),
    ),
    "username": os.environ.get("DATABASE_USER", "oipie"),
    "password": os.environ.get("DATABASE_PASSWORD", "password"),
    "database_name": os.environ.get("DATABASE_NAME", "oipie"),
}


def database_url_connection(override_config: Optional[dict] = None):
    """
    Builds PostgreSQL database connection
    """
    database_config = {**DATABASE_CONFIG, **(override_config or {})}

    return os.environ.get(
        "DATABASE_URL",
        (
            f"postgresql://{database_config['host']}:{database_config['port']}"
            f"/{database_config['database_name']}"
            f"?user={database_config['username']}&password={database_config['password']}"
        ).replace("postgres://", "postgresql://"),
    )
