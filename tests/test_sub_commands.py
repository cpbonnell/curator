from curator.config import CuratorConfig
from tempfile import TemporaryDirectory
from sqlalchemy import create_engine, text
import pdb


def test_main():
    from curator.sub_commands.install import main

    with TemporaryDirectory() as temp_dir:
        config = CuratorConfig(curator_root=temp_dir)
        main(config)

        # Check for the existence of the root directory and collections root
        assert config.root_directory.exists()
        assert config.collections_root.exists()

        # Ensure the database file exists and has the correct URL
        assert config.settings_file.as_posix() == f"{config.root_directory.as_posix()}/curator.db"
        assert config.settings_file_database_url == f"sqlite:///{config.settings_file.as_posix()}"
        assert config.settings_file.exists()

        # Ensure the image_metadata table exists in the database
        engine = create_engine(config.settings_file_database_url)
        with engine.connect() as connection:
            result = connection.execute(text("SELECT name FROM sqlite_master where type='table'"))
            all_tables = [result[0] for result in result.fetchall()]

            # Get a list of all alembic revisions applied to this database
            result = connection.execute(text("SELECT * FROM alembic_version"))
            alembic_revisions = [result[0] for result in result.fetchall()]

        assert "image_metadata" in all_tables
        assert len(alembic_revisions) > 0
