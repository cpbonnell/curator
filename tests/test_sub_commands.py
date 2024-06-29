from curator.config import CuratorConfig
from tempfile import TemporaryDirectory


def test_main():
    from curator.sub_commands.install import main

    with TemporaryDirectory() as temp_dir:
        config = CuratorConfig(curator_root=temp_dir)
        main(config)
        assert config.root_directory.exists()
        assert config.collections_root.exists()

        # The following lines are not yet implemented in the command.
        # assert config.settings_file.exists()
        # assert config.remote_collections_file.exists()
        # assert config.settings_file_database_url == f"sqlite:///{config.settings_file.as_uri()}"
