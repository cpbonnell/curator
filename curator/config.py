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
    def settings_file_database_url(self) -> str:
        """
        The database URL for the settings file.
        """
        return f"sqlite:///{self.settings_file.as_uri()}"

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

    def assert_valid_installation(self):
        """
        Ensure that the root directory and all files exist, raise error if it doesn't.
        """
        missing_files = list()
        if not self._curator_root.exists():
            missing_files.append(self._curator_root)

        if not self.settings_file.exists():
            missing_files.append(self.settings_file)

        if not self.remote_collections_file.exists():
            missing_files.append(self.remote_collections_file)

        if not self.collections_root.exists():
            missing_files.append(self.collections_root)

        if missing_files:
            raise FileNotFoundError(f"The following files or directories are missing: {missing_files}")
