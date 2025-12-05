from pathlib import Path

def read_input(path: Path) -> str:
    return path.read_text().rstrip("\n")

def read_lines(path: Path) -> list[str]:
    return path.read_text().splitlines()

def read_split_by_character(path: Path, split_char: str = "\n\n"):
    text = path.read_text().strip()          
    part_x, part_y = text.split(split_char, 1)

    X_lines = part_x.splitlines()
    Y_lines = part_y.splitlines()
    return X_lines, Y_lines