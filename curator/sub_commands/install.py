from curator.config import CuratorConfig


def main(config: CuratorConfig) -> None:
    """
    Initialize all files needed for a distinct Curator installation.
    """

    # Step 0: If the root of the installation does not exist, create it
    config.root_directory.expanduser().mkdir(parents=True, exist_ok=True)
    config.collections_root.expanduser().mkdir(parents=True, exist_ok=True)
