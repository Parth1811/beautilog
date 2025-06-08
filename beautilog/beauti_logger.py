# fancy_log/logger_setup.py
import copy
import json
import logging
import os
import sys
from logging.handlers import RotatingFileHandler

from tqdm import tqdm

from .color_console_handler import ColoredConsoleHandler
from .constants import TERMINAL_COLORS

CONFIG_FILE = "beauti-log.json"

ABSOLUTE_PATH = os.path.abspath(os.path.dirname(__file__))

CONFIG_FILE_ABS_PATH = os.path.join(ABSOLUTE_PATH, CONFIG_FILE)
with open(CONFIG_FILE_ABS_PATH, 'r') as f:
    DEFAULT_CONFIG = json.load(f)


def load_config():
    paths = [
        os.path.join(os.getcwd(), CONFIG_FILE),
        os.path.join(os.path.dirname(__file__), "..", CONFIG_FILE)
    ]
    for path in paths:
        if os.path.exists(path):
            with open(path, 'r') as f:
                CONFIG = json.load(f)
                DEFAULT_CONFIG.update(CONFIG)
                return DEFAULT_CONFIG

    return DEFAULT_CONFIG

def get_logger():
    config = load_config()
    logger = logging.getLogger()

    if config.get("suppress_other_loggers", False):
        logger.handlers.clear()

    formatter = logging.Formatter(
        '%(asctime)s : %(levelname)s : %(name)s : %(message)s',
        datefmt='%m/%d/%y %I:%M:%S %p'
    )

    if config.get("save_to_file", True):
        file_logger_config = config.get("file_logger", {})
        file_handler = RotatingFileHandler(
            file_logger_config.get("log_file_path", "fancy-run.log"),
            mode='a',
            maxBytes=file_logger_config.get("max_bytes", 10485760),  # Default 100 MB
            backupCount=file_logger_config.get("backup_count", 5),
            encoding='utf-8'
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(getattr(logging, file_logger_config.get("log_level", "DEBUG").upper(), logging.DEBUG))
        logger.addHandler(file_handler)

    def write(self, x):
        if len(x.rstrip()) > 0:
            tqdm.write(x, file=self.file, end='')
    out_stream = type("TqdmStream", (), {'file': sys.stdout, 'write': write})()

    console_handler = ColoredConsoleHandler(out_stream, config.get("level_colors", {}))
    console_handler.setFormatter(formatter)
    console_handler.setLevel(getattr(logging, config.get("log_level", "INFO").upper(), logging.INFO))

    logger.addHandler(console_handler)
    logger.setLevel(getattr(logging, config.get("log_level", "INFO").upper(), logging.INFO))

    for level_name, level_value in config.get("custom_levels", {}).items():
        logging.addLevelName(level_value, level_name.upper())
        setattr(logging, level_name.upper(), level_value)
        setattr(logger, level_name.upper(), level_value)
        setattr(logger, level_name.lower(), lambda msg, level=level_value: logger.log(level, msg))


    return logger
