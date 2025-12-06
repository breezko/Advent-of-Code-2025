# utils/module_importer.py
import importlib
import os
from pathlib import Path


def load_days():
    days_dir = Path(__file__).resolve().parent.parent / "days"
    day_modules = {}

    for filename in sorted(os.listdir(days_dir)):
        if filename.startswith("day") and filename.endswith(".py"):
            module_name = filename[:-3]
            module = importlib.import_module(f"days.{module_name}")
            day_modules[module_name] = module

    return day_modules
