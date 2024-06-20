from pathlib import Path
from typing import Union

Pathlike: Union = str | Path

DEFAULT_CURATOR_ROOT_DIRECTORY = Path.home() / ".curator"


class CuratorConfig:
    """
    Configuration for the Curator application.
    """

    def __init__(self, curator_root: Pathlike):
        """
        Create a new CuratorConfig object.

        It is strongly recommended to use the default curator_root of the application, since curator does not
        need to be installed more than once for a user. This option is included for testing purposes, or in
        case the user wants to install Curator in a non-standard location.

        :param curator_root:  The root directory for this installation of Curator.
        """

        if not curator_root:
            raise ValueError("A root_directory is required to instantiate a CuratorConfig object.")

        if isinstance(curator_root, str):
            curator_root = Path(curator_root)

        self._curator_root = curator_root.expanduser().resolve()

    @property
    def root_directory(self) -> Path:
        """
        The root directory for this installation of Curator.
        """
        return self._curator_root

    @property
    def settings_file(self) -> Path:
        """
        The database file where Curator stores its settings and other information.
        """
        return self._curator_root / "curator.db"

    @property
    def remote_collections_file(self) -> Path:
        """
        The file where information about remote collections is stored.
        """
        return self._curator_root / "remote_collections.yaml"

    @property
    def collections_root(self) -> Path:
        """
        The root directory where files for local collections are stored.
        """
        return self._curator_root / "collections"
