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
    duplicates = {}
    for path in origin.iterdir():
        if path.is_dir():
            excavate(path, destination)
        elif path.is_file():
            with destination / path.name as new:
                # handling duplicate filenames
                if new.exists():
                    if path.name in duplicates:
                        duplicates[path.name] += 1
                    else:
                        duplicates[path.name] = 1
                    new = new.with_name(''.join([path.name, '_', str(
                        duplicates[path.name]), path.suffix]))

                path.rename(new)
