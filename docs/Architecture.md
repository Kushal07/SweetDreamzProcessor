# SweetDreamzProcessor

# Software Architecture

Version: 0.4.0
Status: Architecture Freeze

---

## Document Information

| Item | Value |
|------|-------|
| Project | SweetDreamzProcessor |
| Document | Software Architecture |
| Version | 0.4.0 (Design Freeze) |
| Status | Active Development |
| Architecture | Layered Modular Architecture |
| Language | Python 3.14 |
| GUI | Tkinter |
| Workbook Library | openpyxl |

---

# 1. Purpose

This document describes the technical architecture of SweetDreamzProcessor.

It explains how the software is organised, how the different components interact, and how responsibilities are distributed across the system.

Unlike the Software Design Specification, this document focuses on implementation architecture rather than business requirements.

---

# 2. Architectural Goals

The architecture has been designed to achieve the following goals:

- High maintainability
- Clear separation of responsibilities
- Workbook safety
- Easy testing
- Modular development
- Reusable components
- Minimal coupling
- High cohesion

The architecture follows a layered modular design where each component owns exactly one responsibility.
---

# 3. Layered Architecture

SweetDreamzProcessor is organised into five logical layers.

```text
Presentation Layer
────────────────────────
Tkinter GUI

        │

Application Layer
────────────────────────
SweetDreamzProcessor

        │

Business Layer
────────────────────────
NumberExtractor
NumberArranger
RowDetector
BlockDetector

        │

Infrastructure Layer
────────────────────────
WorkbookManager
WorkbookMapper
WorkbookWriter
WorkbookVerifier
BackupManager

        │

Support Services
────────────────────────
ProcessingStatistics
Configuration
Logger

        │

Excel Workbook
```

Dependencies always flow downward.

Lower layers never depend on upper layers.

---

# 4. Component Interaction

The GUI communicates only with the application layer.

The application layer coordinates the complete processing workflow.

Business components never communicate directly with the GUI.

Infrastructure components never contain business rules.

Workbook writing is always performed through WorkbookWriter after the processor has determined the correct destination and block state.

This separation keeps the architecture modular and maintainable.

---

# 5. High-Level Architecture
                User
                 │
                 ▼
            Tkinter GUI
                 │
                 ▼
      SweetDreamzProcessor
                 │
 ┌───────────────┼────────────────┐
 │               │                │
 ▼               ▼                ▼
Business      Infrastructure    Services
Components      Components

                 │
                 ▼
           Excel Workbook

---

# 6. Component Processing Pipeline

The following diagram illustrates how the application components collaborate during workbook processing.

```text
GUI
 │
 ▼
SweetDreamzProcessor
 │
 ├── WorkbookManager
 │       │
 │       ├── Load Workbook
 │       └── Access Worksheets
 │
 ├── WorkbookValidator
 │
 ├── WorkbookMapper
 │
 ├── WorkbookVerifier
 │
 ├── BackupManager
 │
 ├── RowDetector
 │
 ├── NumberExtractor
 │
 ├── NumberArranger
 │
 ├── BlockDetector
 │
 ├── WorkbookWriter
 │
 └── ProcessingStatistics
 │
 ▼
Processed Workbook
```

---

## Processing Order

The processor coordinates the following sequence.

1. Load workbook.
2. Validate workbook structure.
3. Build worksheet mappings.
4. Verify workbook integrity.
5. Create workbook backup.
6. Start processing statistics.
7. Detect eligible rows.
8. Extract valid lottery numbers.
9. Generate Number Wise Arrangement.
10. Generate Last Digit Arrangement.
11. Detect destination block state.
12. Write arrangement blocks.
13. Update processing statistics.
14. Save processed workbook (planned).
15. Return processing summary.

---

# 7. Data Flow

The internal processing data changes format as it moves through the application.

```text
Excel Workbook

        │

WorkbookManager

        │

Workbook Row

        │

NumberExtractor

        │

LotteryNumber Objects

        │

NumberArranger

        │

Arrangement Dictionaries

        │

BlockDetector

        │

WorkbookWriter

        │

Updated Workbook
```

Each component transforms the data into a form required by the next component while maintaining clear separation of responsibilities.

---

# 8. Component Responsibilities

Every component follows the Single Responsibility Principle.

Each component owns one clearly defined responsibility and communicates only through the application layer.

The following sections describe the responsibilities of each component.

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
- Responsible for generating the suggested output filename.

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

- Generate Number Wise Arrangement.
- Generate Last Digit Arrangement.
- Group extracted lottery numbers.
- Produce normalized arrangement dictionaries.

Not Responsible For

- Reading Excel workbooks.
- Writing workbook data.
- Block detection.

---

## WorkbookWriter

Responsibilities

- Write arrangement blocks into workbook cells.
- Preserve existing workbook formatting.
- Perform only workbook writing operations.

Not Responsible For

- Business rules.
- Arrangement generation.
- Block detection.
- Skip or rewrite decisions.

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

# 9. Design Principles

SweetDreamzProcessor follows several architectural principles to ensure long-term maintainability and predictable behaviour.

---

## Single Responsibility Principle (SRP)

Every component owns exactly one responsibility.

Examples:

- WorkbookManager manages workbook operations.
- NumberExtractor extracts lottery numbers.
- NumberArranger generates arrangements.
- WorkbookWriter writes workbook data.

---

## Separation of Concerns

Business rules are completely separated from Excel operations.

Business components never directly manipulate workbook cells.

Infrastructure components never contain lottery business rules.

---

## Layered Architecture

Each layer communicates only with the layer directly below it.

```text
GUI
    ↓
Application
    ↓
Business
    ↓
Infrastructure
    ↓
Workbook
```

---

## Composition over Inheritance

The application is built from small specialized components coordinated by SweetDreamzProcessor.

Inheritance is avoided unless there is a clear architectural benefit.

---

## Fail-Fast Strategy

Critical validation occurs before workbook modification.

Validation

↓

Verification

↓

Backup

↓

Processing

If any critical step fails, processing stops immediately.

---

## Workbook Safety First

Workbook integrity has higher priority than processing speed.

The processor must never:

- Overwrite completed blocks.
- Modify an invalid workbook.
- Process without a backup.

---

# 10. Design Patterns

The application currently follows the following software design patterns.

---

## Facade Pattern

SweetDreamzProcessor acts as the single public entry point for the application.

```text
GUI

↓

SweetDreamzProcessor

↓

Processing Components
```

The GUI does not directly communicate with processing components.

---

## Coordinator Pattern

SweetDreamzProcessor coordinates independent components without implementing their internal business logic.

---

## Strategy Pattern (Future)

Future versions may support multiple arrangement algorithms while preserving the same processing workflow.

---

## Service Composition

Application behaviour is achieved through composition of specialized services rather than large monolithic classes.

---

# 11. Dependency Rules

Dependencies always flow downward.

```text
Presentation Layer
        │
        ▼
Application Layer
        │
        ▼
Business Layer
        │
        ▼
Infrastructure Layer
        │
        ▼
Workbook
```

The following dependencies are intentionally forbidden.

- WorkbookWriter → GUI
- NumberArranger → WorkbookManager
- WorkbookManager → NumberExtractor
- GUI → WorkbookWriter

Every dependency should pass through SweetDreamzProcessor whenever coordination is required.

---

# 12. Future Architecture

The current architecture has been designed to allow future expansion without major refactoring.

Planned additions include:

## User Interface

- Process Workbook button
- Progress bar
- Live processing log
- Processing summary dialog
- Save As dialog

---

## Workbook Processing

- Complete dual-arrangement processing
- Workbook integrity verification
- Workbook comparison

---

## Reporting

- PDF processing report
- CSV export
- Processing history

---

## Distribution

- PyInstaller executable
- Windows installer
- User Guide
- Developer Guide

The existing layered architecture is expected to remain unchanged throughout Version 1.x.

---

---

# Architecture Summary

SweetDreamzProcessor is designed around a layered modular architecture that separates user interaction, application coordination, business logic, and workbook infrastructure.

The architecture emphasizes:

- Maintainability
- Readability
- Testability
- Workbook safety
- Incremental development

All future development should preserve these architectural principles.