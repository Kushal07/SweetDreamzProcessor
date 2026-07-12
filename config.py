"""
=========================================================
SweetDreamz Processor
Configuration Module

Author : Kushal Bera
Version : 1.0.0
Python : 3.11+

Stores every configurable setting used by the application.
=========================================================
"""

from pathlib import Path


class Config:
    """Application configuration."""

    APP_NAME = "SweetDreamz Processor"
    VERSION = "1.0.0"

    ROOT = Path(__file__).resolve().parent

    INPUT_FOLDER = ROOT / "input"
    OUTPUT_FOLDER = ROOT / "output"
    LOG_FOLDER = ROOT / "logs"
    ASSET_FOLDER = ROOT / "assets"

    OUTPUT_FILE = "SweetDreamz_Processed.xlsx"

    VALID_NUMBER_LENGTH = 5

    LOG_FILE = LOG_FOLDER / "SweetDreamz.log"

    WINDOW_WIDTH = 950
    WINDOW_HEIGHT = 650

    TITLE = f"{APP_NAME} v{VERSION}"

    @classmethod
    def create_folders(cls) -> None:
        """Create required folders."""

        cls.INPUT_FOLDER.mkdir(exist_ok=True)
        cls.OUTPUT_FOLDER.mkdir(exist_ok=True)
        cls.LOG_FOLDER.mkdir(exist_ok=True)
        cls.ASSET_FOLDER.mkdir(exist_ok=True)


Config.create_folders()