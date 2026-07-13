# Changelog

All notable changes to this project will be documented in this file.

The format follows Keep a Changelog principles.

---

## [Unreleased]

### Added

#### Documentation
- Business Specification completed.
- Software Design Specification completed.
- Software Architecture document completed.
- Test Strategy document completed.
- Developer Guide added.
- Initial Roadmap added.

#### Core Infrastructure
- WorkbookManager
- WorkbookValidator
- WorkbookVerifier
- WorkbookMapper
- BackupManager
- WorkbookWriter
- ProcessingStatistics

#### Processing Engine
- Main processing engine.
- Lottery row detection.
- Number extraction from First Prize and Second Prize.
- LotteryNumber data model.
- Middle Pair arrangement generation.
- Last Pair arrangement generation.
- Duplicate value preservation.
- Ordered arrangement generation.

#### Workbook Processing
- Cached worksheet mapping.
- Block detection.
- Complete block detection.
- Partial block detection.
- Empty block detection.
- Safe overwrite logic.
- Backup creation before processing.

#### GUI
- Tkinter desktop application.
- Workbook browsing.
- Workbook loading.
- Workbook information display.
- Application logging.
- Processing button.
- Processing summary display.
- Save As workflow.
- Success notification dialog.

#### Writing
- Number Wise Arrangement writing.
- Last Digit Arrangement writing.
- Dual worksheet processing.
- Independent worksheet mapping.

#### Testing
- Unit tests for:
  - NumberExtractor
  - NumberArranger
  - WorkbookMapper
  - WorkbookVerifier
  - WorkbookWriter
  - RowDetector
  - BlockDetector
  - BackupManager
  - ProcessingStatistics
  - Processor

Current status:
- 20/20 pytest tests passing.

---

### Changed

- Processor now supports independent Number Wise and Last Digit destination worksheets.
- Workbook mapping now supports multiple worksheet layouts.
- Processing statistics integrated with GUI.
- Processing workflow now returns detailed execution statistics.
- Save workflow now preserves the original workbook.
- GUI now uses Save As instead of overwriting source workbook.

---

### Fixed

- Processor processed only one row due to loop indentation issue.
- Last Digit Arrangement writing pipeline completed.
- GUI processing callback connected.
- Workbook mapping extended for Last Digit Arrangement.
- Regression issues resolved while preserving architecture.

---

### Performance

- Cached worksheet mappings reduce repeated worksheet scanning.
- Workbook processing completes approximately 1000 rows in under one second on test workbook.
