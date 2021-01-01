"""
🎾 Recursively calculates the probability of winning a tennis match
"""


try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata  # type: ignore

try:
    __version__ = importlib_metadata.version(__name__)
except importlib_metadata.PackageNotFoundError:
    __version__ = ""

from .set import set
from .game import game
from .match import match
from .errors import InvalidScore, InvalidProbability, InvalidGamesWon
