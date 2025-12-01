import importlib
import os
from pathlib import Path

_days_dir = Path(__file__).parent

for filename in sorted(os.listdir(_days_dir)):
    if filename.startswith("day") and filename.endswith(".py"):
        module_name = filename[:-3]
        importlib.import_module(f"days.{module_name}")
