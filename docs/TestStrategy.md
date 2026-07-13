# SweetDreamzProcessor

# Test Strategy

---

## Document Information

| Item | Value |
|------|-------|
| Project | SweetDreamzProcessor |
| Document | Test Strategy |
| Version | 0.4.0 |
| Status | Active Development |

---

# 1. Purpose

This document defines the testing strategy for SweetDreamzProcessor.

The objective is to ensure that every feature works correctly, existing functionality is not broken, and workbook integrity is maintained throughout development.

---

# 2. Testing Philosophy

SweetDreamzProcessor follows an incremental testing approach.

Every feature must complete the following lifecycle before it is considered finished.

```text
Design
    ↓
Implementation
    ↓
Unit Testing
    ↓
Regression Testing
    ↓
Documentation Update
    ↓
Git Commit
```

No feature is complete until all regression tests pass.

---

# 3. Testing Levels

The project uses multiple levels of testing.

## Unit Testing

Verifies the behaviour of individual components in isolation.

Current unit-tested components include:

- NumberExtractor
- NumberArranger
- RowDetector
- BlockDetector
- WorkbookWriter
- WorkbookMapper
- WorkbookVerifier
- BackupManager
- ProcessingStatistics
- SweetDreamzProcessor

---

## Integration Testing

Verifies interaction between multiple components.

Examples include:

- Workbook loading and validation
- Workbook verification
- Backup creation
- Processing pipeline execution

---

## End-to-End Testing

End-to-end testing verifies the complete processing workflow.

The workflow includes:

1. Load workbook
2. Validate workbook
3. Verify workbook
4. Create backup
5. Process eligible rows
6. Generate both arrangements
7. Write workbook
8. Save processed workbook
9. Return processing statistics

---

## Regression Testing

Regression testing ensures that newly implemented features do not break previously working functionality.

Regression testing is mandatory before every Git commit.

---

# 4. Current Test Coverage

Current automated tests verify:

- Lottery number extraction
- Number arrangement
- Row detection
- Block detection
- Workbook mapping
- Workbook writing
- Backup creation
- Workbook verification
- Processing statistics
- Processing workflow

Current Status:

- 20 automated pytest tests
- All tests passing

---

# 5. Future Test Coverage

Additional tests planned include:

## GUI Tests

- Workbook selection
- Process button
- Progress bar
- Save As dialog
- Processing summary

---

## Workbook Integrity Tests

- Formatting preservation
- Merged cells
- Conditional formatting
- Workbook comparison

---

## End-to-End Tests

Complete workbook processing using sample workbooks.

---

# 6. Quality Gates

Before a feature is considered complete:

- Design reviewed
- Implementation completed
- Unit tests passing
- Regression tests passing
- Documentation updated
- Git commit created

No feature may bypass these quality gates.

---

# 7. Test Execution

Run the complete regression suite using:

```bash
python -m pytest
```

Every test must pass before code is merged into the main development branch.

---

# 8. Long-Term Goal

The long-term objective is to achieve comprehensive automated testing covering:

- Business logic
- Workbook operations
- GUI workflow
- End-to-end processing
- Regression protection

The test suite should provide confidence that future development can continue without introducing regressions.