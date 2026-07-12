# SweetDreamzProcessor
# Software Design Specification (SDS)

**Project:** SweetDreamzProcessor

**Version:** 0.3.0 (Development)

**Status:** In Development

---

# 1. Objective

SweetDreamzProcessor automates the processing of Sweet Dreamz Excel workbooks.

The application:

- Reads prize numbers from Excel workbooks.
- Extracts all valid 5-digit numbers.
- Generates Middle Pair Arrangement.
- Generates Last Pair Arrangement.
- Writes results into the workbook.
- Preserves workbook structure and formatting.
- Skips completed blocks.
- Rewrites partially completed blocks.
- Generates processing statistics.
- Creates automatic workbook backups.
- Saves the processed workbook.

---

# 2. Technology Stack

Language

- Python 3.14

GUI

- Tkinter

Excel Processing

- openpyxl

Testing

- pytest

Version Control

- Git
- GitHub

Packaging

- PyInstaller (Planned)

---

# 3. Project Structure

```text
SweetDreamzProcessor/

assets/
backup/
docs/
input/
logs/
output/

processor/
tests/
utils/

config.py
gui.py
main.py
README.md
requirements.txt
```

---

# 4. Processing Workflow

```text
User
 │
 ▼
Browse Workbook
 │
 ▼
Validate Workbook
 │
 ▼
Load Workbook
 │
 ▼
Create Backup
 │
 ▼
Detect Eligible Rows
 │
 ▼
Process Each Row
 │
 ├── Read Prize Numbers
 │
 ├── Extract Numbers
 │
 ├── Arrange Middle Pair
 │
 ├── Arrange Last Pair
 │
 └── Write Workbook
 │
 ▼
Save Workbook
 │
 ▼
Verify Workbook
 │
 ▼
Return Processing Statistics
```

---

# 5. Current Architecture

```text
GUI
 │
 ▼
SweetDreamzProcessor
 │
 ├── WorkbookManager
 ├── WorkbookMapper
 ├── WorkbookWriter
 ├── NumberExtractor
 ├── NumberArranger
 ├── RowDetector
 ├── BlockDetector
 ├── ProcessingStatistics
 └── BackupManager
```

---

# 6. Business Rules

## Block States

### EMPTY

- Series empty
- Pair empty
- Last empty

Action

- Write data

---

### COMPLETE

- Series exists
- Pair exists
- Last exists

Action

- Skip block
- Never overwrite

---

### PARTIAL

Some cells are filled.

Some cells are blank.

Action

- Rewrite entire block.
- Log warning.
- Increment partial rewrite statistics.

---

# 7. Workbook Rules

- Never overwrite completed blocks.
- Rewrite partially completed blocks.
- Preserve workbook formatting.
- Preserve merged cells.
- Preserve borders.
- Preserve fonts.
- Preserve colours.
- Preserve row heights.
- Preserve column widths.

---

# 8. Number Extraction

Every valid 5-digit number is converted into:

- Series
- Middle Pair
- Last Pair

Example

45231

Series = 4

Middle Pair = 52

Last Pair = 31

---

# 9. Arrangements

## Middle Pair Arrangement

Grouped by Middle Pair.

Output

- Series
- Pair
- Last

## Last Pair Arrangement

Grouped by Last Pair.

Output

- Series
- Pair
- Last

---

# 10. Processing Statistics

Current statistics include:

- Total rows scanned
- Rows processed
- Empty blocks written
- Complete blocks skipped
- Partial blocks rewritten
- Errors
- Processing duration

---

# 11. Logging

The application logs:

- Workbook loading
- Workbook saving
- Processing decisions
- Skipped blocks
- Partial rewrites
- Backup creation
- Processing summary

---

# 12. Error Recovery

Current

- Automatic backup

Planned

- Restore from backup
- Workbook verification
- Detailed error reporting

---

# 13. Testing

Framework

- pytest

Current Status

- 19 passing tests

Regression testing is mandatory before every commit.

---

# 14. Future Enhancements

- Progress bar
- Live GUI logging
- Drag and Drop
- Dark Mode
- PDF Report
- CSV Export
- Performance Dashboard
- Automatic Updates
- Executable Build