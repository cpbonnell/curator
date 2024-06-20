from pathlib import Path
from typing import Union

Pathlike: Union = str | Path


class CuratorConfig:
    """
    Configuration for the Curator application.
    """

    def __init__(self, curator_root: Pathlike):

        if not curator_root:
            raise ValueError("A root_directory is required to instantiate a CuratorConfig object.")

        if isinstance(curator_root, str):
            curator_root = Path(curator_root)

        self._curator_root = curator_root.expanduser().resolve()

    @property
    def root_directory(self) -> Path:
        return self._curator_root

    @property
    def settings_file(self) -> Path:
        return self._curator_root / "curator.db"
