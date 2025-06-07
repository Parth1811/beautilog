# fancy_log/__init__.py
from .color_console_handler import ColoredConsoleHandler
from .constants import TERMINAL_COLORS
from .fancy_logger import get_logger

# Initialize logger at import time
logger = get_logger()

# Optional: expose utility functions if needed later
__all__ = [
    "ColoredConsoleHandler",
    "TERMINAL_COLORS",
    "get_logger",
    "logger"
]
