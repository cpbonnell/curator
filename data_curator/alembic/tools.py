from importlib import resources
from pathlib import Path
from typing import Union

from alembic import command
from alembic.config import Config as AlembicConfig

import data_curator

PathLike: Union = str | Path


def run_migrations(database_url: PathLike) -> None:
    """
    Run the Alembic migrations for the given database URL.

    If the database file does not exist, it will be created.
    """

    # NOTE: By default Alembic determines the location of some critical components (such as the alembic.ini file)
    # based on the current working directory. This is not ideal for a library like Curator, so we need to
    # explicitly specify the location of the Alembic configuration files. We also need to inject the URL
    # for the database file into the configuration, since it is determined as part of the command line invocation
    package_resources_root = Path(str(resources.files(data_curator)))
    alembic_ini_path = package_resources_root / "alembic.ini"
    alembic_versions_path = package_resources_root / "alembic"

    assert alembic_ini_path.exists(), f"alembic.ini not found at {alembic_ini_path}"
    assert alembic_versions_path.exists(), f"Revisions directory not found at {alembic_versions_path}"
    assert (
        alembic_versions_path / "versions"
    ).exists(), f"Versions directory not found at {alembic_versions_path / 'versions'}"

    alembic_config = AlembicConfig(str(alembic_ini_path))
    alembic_config.set_main_option("sqlalchemy.url", database_url)
    alembic_config.set_main_option("script_location", alembic_versions_path.absolute().as_posix())

    command.upgrade(alembic_config, "head")
