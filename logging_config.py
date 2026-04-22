"""Logging configuration for the trading bot."""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


LOGGER_NAME = "trading_bot"


def setup_logger() -> logging.Logger:
    """Create a file logger that writes to bot.log in the project root."""

    logger = logging.getLogger(LOGGER_NAME)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    logger.propagate = False

    log_path = Path(__file__).resolve().parent.parent / "bot.log"
    handler = RotatingFileHandler(log_path, maxBytes=1_000_000, backupCount=3, encoding="utf-8")
    handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    )

    logger.addHandler(handler)
    return logger