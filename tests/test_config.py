from pathlib import Path

from curator.config import CuratorConfig


config = CuratorConfig(Path.home() / ".curator")


def test_root_directory():
    assert config.root_directory == Path.home() / ".curator"


def test_settings_file():
    assert config.settings_file == Path.home() / ".curator" / "curator.db"


def test_remote_collections_file():
    assert config.remote_collections_file == Path.home() / ".curator" / "remote_collections.yaml"


def test_collections_root():
    assert config.collections_root == Path.home() / ".curator" / "collections"
