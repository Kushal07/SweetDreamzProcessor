# SweetDreamzProcessor

# Test Strategy

---

# Copyright Notice

Copyright © 2026 Kushal Bera. All Rights Reserved.

This document and the SweetDreamzProcessor testing strategy are the exclusive intellectual property of Kushal Bera.

No part of this document may be copied, reproduced, modified, distributed, published, reverse engineered, or commercially exploited without prior written permission from the copyright owner.

Commercial licensing is available only through written authorization from Kushal Bera.

---

# Confidentiality Notice

This document contains proprietary testing information relating to the SweetDreamzProcessor project.

Distribution of this document is permitted only with written authorization from the copyright owner.

---

# Document Information

| Item | Value |
|------|-------|
| Project | SweetDreamzProcessor |
| Document | Test Strategy |
| Version | 1.0.0 |
| Status | Design Freeze |
| Author | Kushal Bera |
| Owner | Kushal Bera |
| Copyright | © 2026 Kushal Bera |

---

# Document Control

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0.0 | 2026 | Kushal Bera | Initial Test Strategy |

---

# References

This document is derived from:

- Business_Specification.md
- Software_Design_Specification.md
- Architecture.md

---

# Authority Statement

This document defines the approved testing strategy for SweetDreamzProcessor.

All software releases shall satisfy the testing requirements defined herein before being considered production ready.

---

# 1. Introduction

This document defines the testing strategy for SweetDreamzProcessor.

It specifies the testing philosophy, testing levels, acceptance criteria, and traceability required to verify that the software satisfies the approved Business Specification, Software Design Specification, and Software Architecture.

---

# 2. Purpose

The purpose of this document is to provide a consistent and repeatable testing approach.

It serves as the reference for:

- Unit testing
- Integration testing
- End-to-end testing
- Regression testing
- Release validation

---

# 3. Scope

This document defines:

- Testing principles
- Test levels
- Acceptance criteria
- Requirement traceability
- Regression strategy
- Test environment
- Release validation

Implementation details remain defined by the Software Architecture.

---

# 4. Testing Objectives

The testing strategy has the following objectives.

---

## TO-001 — Correctness

Verify that all approved business rules are correctly implemented.

---

## TO-002 — Workbook Safety

Verify that workbook integrity is preserved throughout processing.

The test strategy shall verify that:

• Source worksheet columns are preserved.
• Existing worksheet data is preserved.
• Existing arrangement headers are preserved.
• Existing arrangement data is preserved.
• Only missing arrangement headers are created.

---

## TO-003 — Repeatability

Verify that identical input produces identical output.

---

## TO-004 — Reliability

Verify that processing continues safely whenever recovery is possible.

---

## TO-005 — Regression Protection

Prevent previously implemented features from breaking when new functionality is introduced.

---

## TO-006 — Traceability

Every test shall trace back to one or more approved software requirements.

---

## TO-007 — Automation

Whenever practical, tests shall be automated using pytest.

---

# 5. Testing Principles

The following principles govern all testing activities.

---

## TP-001

Business rules are tested before implementation is considered complete.

---

## TP-002

Every new feature requires automated tests.

---

## TP-003

Regression tests shall pass before merging changes.

---

## TP-004

Tests shall be deterministic.

---

## TP-005

Test data shall be independent.

---

## TP-006

Unit tests shall not require the graphical user interface.

---

## TP-007

The original workbook shall never be modified during automated tests.

Temporary workbooks shall be used instead.

---

# TP-008

The processor shall modify only worksheet cells required by the approved Business Specification.

Tests shall verify that processing never:

• overwrites unrelated worksheet data
• shifts worksheet columns
• modifies the Date, 1st Prize or 2nd Prize columns
---

# 6. Test Levels

SweetDreamzProcessor uses multiple testing levels.

| Level | Purpose |
|---------|----------|
| Unit Testing | Verify individual components |
| Integration Testing | Verify component collaboration |
| End-to-End Testing | Verify complete workbook processing |
| Workbook Integrity Testing | Verify workbook preservation |
| GUI Testing | Verify user interaction |
| Regression Testing | Verify existing functionality after changes |

---

# 7. Unit Testing Strategy

## Overview

Unit testing verifies the behaviour of individual software components in isolation.

Each component shall be tested independently of the graphical user interface and workbook file system whenever practical.

Unit tests shall execute automatically using **pytest**.

---

## UT-001 — Component Isolation

Each unit test shall verify one architectural component.

Examples include:

- WorkbookValidator
- WorkbookVerifier
- RowDetector
- NumberExtractor
- NumberArranger
- BlockDetector
- WorkbookWriter
- ProcessingStatistics

---

## UT-002 — Deterministic Behaviour

Unit tests shall produce identical results for identical inputs.

No test shall depend upon:

- Current date
- System time
- Execution order
- External services

---

## UT-003 — Independent Test Data

Each test shall create its own data.

Tests shall never depend upon:

- Previous tests
- Shared state
- External workbook modifications

---

## UT-004 — Acceptance Criteria

A component passes unit testing when:

- Expected outputs are produced.
- Invalid inputs are handled correctly.
- Exceptions are raised when appropriate.
- No unexpected side effects occur.

---

## Current Coverage

| Component | Status |
|-----------|--------|
| WorkbookValidator | Tested |
| WorkbookVerifier | Tested |
| WorkbookMapper | Tested |
| BackupManager | Tested |
| RowDetector | Tested |
| NumberExtractor | Tested |
| NumberArranger | Tested |
| BlockDetector | Tested |
| WorkbookWriter | Tested |
| ProcessingStatistics | Tested |
| BlockCreator | Planned|

---

# 8. Integration Testing Strategy

## Overview

Integration testing verifies that architectural components collaborate correctly.

The focus is on interactions rather than individual component behaviour.

---

## IT-001 — Processing Pipeline

Verify collaboration between:

- Workbook Manager
- Workbook Validator
- Workbook Verifier
- Workbook Mapper
- Backup Manager
- Row Detector
- Number Extractor
- Number Arranger
- Block Detector
- Workbook Writer
- Processing Statistics

---

## IT-002 — Workbook Processing

Verify complete processing of:

- Valid workbook
- Partially completed workbook
- Workbook with invalid rows
- Workbook containing duplicate values
• Workbook with missing arrangement headers
• Workbook with partially completed arrangement headers

---

## IT-003 — Save Workflow

Verify:

- Suggested filename generation
- Save As workflow
- Workbook save
- Backup creation

---

## Acceptance Criteria

Integration testing passes when:

- Components communicate correctly.
- Processing statistics are correct.
- Workbook output satisfies the Business Specification.

---

# 9. End-to-End Testing

## Overview

End-to-end testing verifies complete user workflows from workbook selection through workbook saving.

---

## E2E-001 — Standard Processing

Scenario

- Select valid workbook.
- Process workbook.
- Save workbook.

Expected Result

- Workbook processed successfully.
- Original workbook unchanged.
- Processing summary displayed.

---

## E2E-002 — Duplicate Processing

Verify duplicate handling for:

- Middle Pair
- Last Pair

---

## E2E-003 — Invalid Workbook

Verify processing stops when:

- Workbook validation fails.
- Workbook verification fails.

---

## E2E-004 — Save Failure

Verify application behaviour when workbook saving fails.

Expected behaviour:

- Workbook remains unchanged.
- User receives clear error message.

---

## E2E-005 — Missing Arrangement Headers
Scenario

Open a workbook with missing arrangement headers.
Process workbook.

Expected Result

Missing headers completed.
Existing worksheet data unchanged.
Processing completed successfully.

---

## E2E-006 — Partial Arrangement Headers

Scenario

Workbook contains incomplete arrangement headers.

Expected Result

Missing headers completed.
Existing headers preserved.
Existing data preserved.

---

# 10. Workbook Integrity Testing

## Overview

Workbook integrity testing verifies that processing never damages the workbook.

---

## Verify

- Fonts preserved
- Borders preserved
- Colours preserved
- Merged cells preserved
- Row heights preserved
- Column widths preserved
- Existing completed Arrangement Blocks preserved
• Date column preserved
• 1st Prize column preserved
• 2nd Prize column preserved
• Existing worksheet data preserved
• Existing arrangement headers preserved
• Partial arrangement headers completed correctly
• Missing arrangement headers completed correctly
• Worksheet column positions preserved

---

## Acceptance Criteria

Processing shall modify only worksheet cells explicitly required by the approved Business Specification.

No unrelated worksheet data, headers, formatting or column positions shall be altered.

All other workbook content shall remain unchanged.

---

# 11. GUI Testing

## Overview

GUI testing verifies user interaction.

---

## Verify

- Workbook selection
- Save As dialog
- Suggested filename
- Processing summary
- Error dialogs

---

## Acceptance Criteria

The GUI shall:

- Display meaningful messages.
- Prevent invalid operations.
- Return safely after user cancellation.

---

# 12. Regression Testing

## Overview

Regression testing ensures that previously implemented functionality continues to work after software modifications.

---

## Policy

Regression testing shall be executed:

- Before every release.
- After every completed feature.
- Before merging changes.

---

## Regression Suite

Current regression suite includes:

- test_arranger.py
- test_backup_manager.py
- test_block_detector.py
- test_extract.py
- test_processing_statistics.py
- test_processor.py
- test_row_detector.py
- test_workbook_mapper.py
- test_workbook_processor.py
- test_workbook_verifier.py
- test_writer.py

---

## ARR-004 Manual Verification

Before approving ARR-004 related changes, verify manually that:

• Existing worksheet data remains unchanged.
• Date / 1st Prize / 2nd Prize remain unchanged.
• Existing arrangement headers remain unchanged.
• Missing arrangement headers are completed.
• Workbook formatting is preserved.

---

## Acceptance Criteria

The regression suite shall complete successfully with no failing tests.

A release shall not proceed while regression failures exist.

---

# 13. Requirement Traceability

Testing shall maintain traceability from business rules through software requirements to automated tests.

Example traceability:

| Business Rule | Software Requirement | Architecture | Test |
|---------------|----------------------|--------------|------|
| DRAW-001 | FR-001 | COMP-001 | UT-001 |
| ARR-001 | FR-005 | COMP-009 | UT-005 |
| ARR-003 | FR-008 | COMP-009 | E2E-002 |
| BLK-002 | FR-011 | COMP-010 | UT-010 |
| WB-004 | NFR-002 | COMP-011 | Workbook Integrity |
| ARR-004 | FR-009 | COMP-005A | IT-002 / E2E-005 |
---

# 14. Test Environment

The reference test environment is:

| Item | Value |
|------|-------|
| Language | Python 3.14 |
| Test Framework | pytest |
| Workbook Library | openpyxl |
| Operating System | Windows 11 (primary development environment) |

Tests should remain platform-independent whenever practical.

---

# 15. Future Testing

Future improvements include:

- GUI automation testing
- Performance benchmarking
- Stress testing with large workbooks
- Memory usage profiling
- Cross-platform testing
- Continuous Integration (CI) pipeline execution
• Workbook comparison testing

These enhancements shall be introduced without reducing the existing automated regression coverage.

---

# 16. Summary

This document defines the testing strategy for SweetDreamzProcessor.

It establishes:

- Unit testing
- Integration testing
- End-to-end testing
- Workbook integrity testing
- GUI testing
- Regression testing
- Requirement traceability
- Test environment
- Future testing

Every software release shall satisfy this testing strategy before being considered production ready.