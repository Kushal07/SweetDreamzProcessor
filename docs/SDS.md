# SweetDreamzProcessor v1.0
## Software Design Specification (SDS)

---

# 1. Objective

SweetDreamzProcessor automates the processing of Sweet Dreamz Excel workbooks.

The application:

- Reads prize numbers
- Extracts all valid 5-digit numbers
- Creates Number Wise Arrangement
- Creates Last Digit Arrangement
- Writes results into existing workbook
- Preserves workbook formatting
- Skips completed rows
- Saves a new workbook

---

# 2. Technology

Python 3.14

GUI
    Tkinter

Excel
    openpyxl

Build
    PyInstaller

Repository
    GitHub

---

# 3. Folder Structure

SweetDreamzProcessor

main.py

gui.py

config.py

processor/

utils/

assets/

docs/

tests/

logs/

output/

---

# 4. Workflow

User

↓

Browse Workbook

↓

Validate Workbook

↓

Load Workbook

↓

Detect incomplete rows

↓

For each row

↓

Read Date

↓

Read 1st Prize

↓

Read 2nd Prize

↓

Combine Numbers

↓

Extract

↓

Arrange Middle Pair

↓

Arrange Last Pair

↓

Write Number Sheet

↓

Write Last Sheet

↓

Save Workbook

↓

Finished

---

# 5. Data Model

LotteryNumber

original

series

middle_pair

last_pair

---

# 6. Workbook Rules

Do not modify completed rows.

Fill only blank rows.

Preserve

Fonts

Borders

Colors

Merged Cells

Conditional Formatting

Formulas

Row Heights

Column Widths

---

# 7. Number Extraction

Every 5-digit number is converted into

Series

Middle Pair

Last Pair

Example

45231

Series = 4

Middle Pair = 52

Last Pair = 31

---

# 8. Number Wise Arrangement

Group by Middle Pair

Output

Series

Pair

Blank

---

# 9. Last Digit Arrangement

Group by Last Pair

Output

Series

Blank

Pair

---

# 10. Logging

Every action is logged.

Workbook Loaded

Validation Successful

Rows Processed

Numbers Extracted

Workbook Saved

Finished

---

# 11. Error Recovery

Create automatic backup

Restore on failure

Display detailed error

---

# 12. Output

SweetDreamz_Processed.xlsx

---

# 13. Future Features

Drag and Drop

Dark Mode

Automatic Updates

PDF Report

CSV Export

Performance Dashboard
