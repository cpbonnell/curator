from curator.config import CuratorConfig
from curator.alembic.tools import run_migrations


def main(config: CuratorConfig) -> None:
    """
    Initialize all files needed for a distinct Curator installation.
    """

    # Step 0: If the root directories of the installation does not exist, create it
    config.root_directory.expanduser().mkdir(parents=True, exist_ok=True)
    config.collections_root.expanduser().mkdir(parents=True, exist_ok=True)

    # Step 1: Create the database file
    run_migrations(config.settings_file_database_url)
