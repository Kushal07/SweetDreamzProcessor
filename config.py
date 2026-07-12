"""
SweetDreamzProcessor Configuration
----------------------------------
Global configuration used throughout the application.
"""

from pathlib import Path


# -----------------------------
# Application Information
# -----------------------------
APP_NAME = "SweetDreamzProcessor"
APP_VERSION = "1.0.0"

# -----------------------------
# Folder Structure
# -----------------------------
ROOT_DIR = Path(__file__).resolve().parent

INPUT_DIR = ROOT_DIR / "input"
OUTPUT_DIR = ROOT_DIR / "output"
LOG_DIR = ROOT_DIR / "logs"
ASSET_DIR = ROOT_DIR / "assets"

# Create folders automatically
INPUT_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)
ASSET_DIR.mkdir(exist_ok=True)

# -----------------------------
# Workbook Sheet Names
# -----------------------------
NUMBER_WISE_SHEET = "Number wise arrangement"
LAST_DIGIT_SHEET = "Last digit arrangement"

# -----------------------------
# Prize Columns
# -----------------------------
FIRST_PRIZE_COLUMN = "B"
SECOND_PRIZE_COLUMN = "C"

# -----------------------------
# Logging
# -----------------------------
LOG_FILE = LOG_DIR / "SweetDreamzProcessor.log"

# -----------------------------
# Output
# -----------------------------
OUTPUT_FILENAME = "SweetDreamz_Processed.xlsx"

# -----------------------------
# Validation
# -----------------------------
VALID_NUMBER_LENGTH = 5