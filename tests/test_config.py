from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from data_curator.config import CuratorConfig

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


def test_assert_valid_installation():
    """
    The assert_valid_installation method raises FileNotFound errors on the
    absence of a variety of files. To ensue that the method is working as
    expected, this test creates an empty temp director, and then adds the
    needed files one by one until the method no longer raises an error.

    """

    with TemporaryDirectory() as tmpdirname:
        bad_config = CuratorConfig(tmpdirname)

        # Empty root directory
        with pytest.raises(FileNotFoundError):
            bad_config.assert_valid_installation()

        # Add settings file
        (Path(tmpdirname) / "curator.db").touch()
        with pytest.raises(FileNotFoundError):
            bad_config.assert_valid_installation()

        # Add remote collections file
        (Path(tmpdirname) / "remote_collections.yaml").touch()
        with pytest.raises(FileNotFoundError):
            bad_config.assert_valid_installation()

        # Add collections directory (function should now return without raising an error)
        (Path(tmpdirname) / "collections").mkdir()
        bad_config.assert_valid_installation()
