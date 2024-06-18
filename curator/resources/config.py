from pathlib import Path
from typing import Union

Pathlike: Union = str | Path


class CuratorConfig:
    """
    Configuration for the Curator application.
    """

    def __init__(self, root_directory: Pathlike):

        if not root_directory:
            raise ValueError("A root_directory is required to instantiate a CuratorConfig object.")
        self._root_directory = root_directory.expanduser().resolve()

    @property
    def root_directory(self) -> Path:
        return self._root_directory

    @property
    def settings_file(self) -> Path:
        return self._root_directory / "curator.db"
