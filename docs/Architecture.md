# SweetDreamzProcessor
# Software Architecture

**Version:** 0.3.0

---

# 1. Overview

SweetDreamzProcessor follows a modular architecture based on the **Single Responsibility Principle (SRP)**.

Each class has one clearly defined responsibility.

The central coordinator is `SweetDreamzProcessor`, which orchestrates the complete workbook processing workflow.

---

# 2. High-Level Architecture

```text
                GUI
                 │
                 ▼
      SweetDreamzProcessor
                 │
 ┌───────────────┼────────────────┐
 │               │                │
 ▼               ▼                ▼
Workbook     Processing      Utilities
Management     Engine

WorkbookManager
WorkbookMapper
WorkbookWriter

NumberExtractor
NumberArranger
RowDetector
BlockDetector
ProcessingStatistics
BackupManager

Logger
Configuration
```

---

# 3. Processing Pipeline

```text
Load Workbook
        │
        ▼
Validate Workbook
        │
        ▼
Build Worksheet Mapping
        │
        ▼
Verify Workbook
        │
        ▼
Create Backup
        │
        ▼
Start Processing Statistics
        │
        ▼
Detect Eligible Rows
        │
        ▼
For Each Row
        │
        ├── Read Row Data
        ├── Extract Numbers
        ├── Arrange Middle Pair
        ├── Arrange Last Pair
        ├── Detect Block State
        └── Write Results
        │
        ▼
Save Workbook
        │
        ▼
Return Processing Statistics
```

---

# 4. Class Responsibilities

## SweetDreamzProcessor

Role

Application coordinator.

Responsibilities

- Coordinate workbook processing.
- Call all processing components.
- Manage workflow.
- Collect processing statistics.

Not Responsible For

- Reading Excel files.
- Writing Excel files.
- Number extraction logic.
- Arrangement algorithms.

---

## WorkbookManager

Responsibilities

- Load workbook.
- Save workbook.
- Access worksheets.
- Read row data.

Not Responsible For

- Business rules.
- Arrangement logic.
- Statistics.

---

## WorkbookMapper

Responsibilities

- Scan worksheet headers.
- Cache worksheet mappings.

Not Responsible For

- Reading prize numbers.
- Writing workbook data.

---

## NumberExtractor

Responsibilities

- Extract valid 5-digit numbers.

---

## NumberArranger

Responsibilities

- Generate Middle Pair arrangement.
- Generate Last Pair arrangement.

---

## WorkbookWriter

Responsibilities

- Write values to worksheet cells.

Not Responsible For

- Skip decisions.
- Block detection.
- Business rules.

---

## RowDetector

Responsibilities

- Decide whether a workbook row should be processed.

---

## BlockDetector

Responsibilities

Determine whether a block is:

- EMPTY
- PARTIAL
- COMPLETE

---

## ProcessingStatistics

Responsibilities

Collect processing metrics.

Current metrics

- Total rows scanned
- Rows processed
- Empty blocks written
- Complete blocks skipped
- Partial blocks rewritten
- Errors
- Duration

---

## BackupManager

Responsibilities

- Create timestamped workbook backups.
- Log backup creation.
## WorkbookVerifier

Responsibilities

- Owns verification logic.


---

# 5. Dependency Diagram

```text
GUI
 │
 ▼
SweetDreamzProcessor
 │
 ├── WorkbookManager
 ├── WorkbookValidator
 ├── WorkbookVerifier
 ├── WorkbookMapper
 ├── WorkbookWriter
 ├── NumberExtractor
 ├── NumberArranger
 ├── RowDetector
 ├── BlockDetector
 ├── BackupManager
 └── ProcessingStatistics
```

Dependencies should always flow downward.

Lower-level modules should never depend on higher-level modules.

---

# 6. Design Principles

The project follows:

- Single Responsibility Principle (SRP)
- Composition over inheritance
- Modular architecture
- Incremental development
- Test-driven validation
- Separation of business logic from Excel operations

---

# 7. Future Architecture

The following components are planned:

```text

GUI Progress Manager

Report Generator

Executable Builder
```

These components will be integrated without changing the existing architecture.