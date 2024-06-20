from pathlib import Path
import pytest

from curator.config import CuratorConfig


config = CuratorConfig(Path.home() / ".curator")
str_config = CuratorConfig("~/.curator")


def test_root_directory():
    assert config.root_directory == Path.home() / ".curator"
    assert str_config.root_directory == Path.home() / ".curator"


def test_settings_file():
    assert config.settings_file == Path.home() / ".curator" / "curator.db"
    assert str_config.settings_file == Path.home() / ".curator" / "curator.db"


def test_remote_collections_file():
    assert config.remote_collections_file == Path.home() / ".curator" / "remote_collections.yaml"
    assert str_config.remote_collections_file == Path.home() / ".curator" / "remote_collections.yaml"


def test_collections_root():
    assert config.collections_root == Path.home() / ".curator" / "collections"
    assert str_config.collections_root == Path.home() / ".curator" / "collections"


def test_curator_config_no_root_directory():
    with pytest.raises(ValueError):
        CuratorConfig(None)
