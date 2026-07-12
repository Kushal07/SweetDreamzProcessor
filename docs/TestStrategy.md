# SweetDreamzProcessor
# Test Strategy

**Version:** 0.3.0

---

# 1. Purpose

This document describes the testing strategy used by the SweetDreamzProcessor project.

Testing ensures that every feature works correctly, regressions are detected early, and the application remains stable as new functionality is added.

---

# 2. Testing Framework

Framework

- pytest

Python Version

- Python 3.14

---

# 3. Testing Philosophy

The project follows an incremental development process.

Every feature follows this workflow:

Design

↓

Implement

↓

Unit Test

↓

Fix (if required)

↓

Regression Test

↓

Documentation Update

↓

Git Commit

↓

Git Push

No feature is complete until the entire regression suite passes.

---

# 4. Current Test Coverage

## Workbook

- WorkbookManager
- WorkbookValidator
- WorkbookMapper

---

## Processing

- NumberExtractor
- NumberArranger
- RowDetector
- BlockDetector
- WorkbookWriter
- SweetDreamzProcessor

---

## Statistics

- ProcessingStatistics

---

## Backup

- BackupManager

---

# 5. Current Status

Current Tests

- 19 passing tests

Status

- No known failures
- No skipped tests
- No expected failures (xfail)

---

# 6. Regression Testing

Run the complete test suite before every commit.

Command

```bash
python -m pytest
```

Expected Output

```text
19 passed
```

---

# 7. Coding Rules

Every new feature should include:

- New tests when appropriate.
- No existing tests should fail.
- Existing behaviour must not change unless intentionally updated.

Regression testing is mandatory.

---

# 8. Future Testing

Planned additions

## Unit Tests

- WorkbookVerifier
- GUI Components
- Save Workflow

---

## Integration Tests

- Complete workbook processing
- Backup creation
- Workbook saving
- Workbook verification

---

## End-to-End Tests

Complete application workflow

Workbook

↓

Processing

↓

Saving

↓

Verification

↓

GUI confirmation

---

# 9. Quality Goals

The project aims to achieve:

- Stable regression suite
- High code reliability
- Maintainable architecture
- Predictable feature development
- Easy debugging
- Production-ready quality

---

# 10. Continuous Improvement

After every completed feature:

- Add or update tests.
- Run the full regression suite.
- Update the changelog.
- Update the roadmap.
- Update the architecture document if required.

This ensures that documentation and implementation remain synchronized throughout the project's lifecycle.