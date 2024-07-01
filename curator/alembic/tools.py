from importlib import resources
from pathlib import Path
from typing import Union

from alembic import command
from alembic.config import Config as AlembicConfig

import curator

PathLike: Union = str | Path


def run_migrations(database_url: PathLike) -> None:
    """
    Run the Alembic migrations for the given database URL.

    If the database file does not exist, it will be created.
    """

    alembic_ini_path = resources.files(curator) / "alembic.ini"
    alembic_config = AlembicConfig(str(alembic_ini_path))
    alembic_config.set_main_option("sqlalchemy.url", database_url)

    command.upgrade(alembic_config, "head")
