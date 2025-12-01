from pathlib import Path

def read_input(path: Path) -> str:
    return path.read_text().rstrip("\n")

def read_lines(path: Path) -> list[str]:
    return path.read_text().splitlines()