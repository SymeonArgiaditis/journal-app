from pathlib import Path

def list_journals(root_path: Path) -> list[str]:
    directory_names: list[str] = []

    for item in root_path.iterdir():
        if item.is_dir():
            directory_names.append(item.name)

    return directory_names
