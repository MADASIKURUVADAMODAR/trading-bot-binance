"""Logging configuration for the trading bot."""

from __future__ import annotations

import logging
from pathlib import Path


def setup_logging() -> None:
    """Configure logging for both console and bot.log."""

    log_path = Path(__file__).resolve().parent.parent / "bot.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_path, encoding="utf-8"),
        ],
        force=True,
    )


def setup_logger() -> None:
    """Backward-compatible alias for older callers."""

    setup_logging()