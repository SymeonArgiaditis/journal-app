from pathlib import Path

# List journal directories from a given path
def list_journals(root_path: Path) -> list[str]:
    directory_names: list[str] = []

    for item in root_path.iterdir():
        if item.is_dir():
            directory_names.append(item.name)

    return directory_names

# List journal entries  from a given journal path
def list_entries(journal_path: Path) -> list[str]:
    entry_list: list[str] = []

    for item in journal_path.iterdir():
        if item.is_file() and item.suffix == '.md':
            entry_list.append(item.name)

    return sorted(entry_list)
