"""For moving all files from all subdirectories of one directory to another directory"""
import pathlib


def excavate(origin, destination):
    """
    Recursively moves all files from all subdirectories of one specified directory to another.

    Parameters:
    origin: Path
        The directory to be emptied of files
    destination: Path
        The directory the files will be moved to
    """
    for file in origin.iterdir():
        if file.is_dir():
            excavate(file, destination)
        elif file.is_file():
            file.rename(destination / file.name)
