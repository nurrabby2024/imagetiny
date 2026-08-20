"""ImageTiny: Shrinks image files in a folder with quality settings and before/after size reports."""

__version__ = "1.0.0"

from .core import run
from .cli import main

__all__ = ["main", "run", "__version__"]