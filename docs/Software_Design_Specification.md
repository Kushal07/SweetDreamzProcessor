# SweetDreamzProcessor

# Software Design Specification

---

# Copyright Notice

Copyright © 2026 Kushal Bera. All Rights Reserved.

This document and the SweetDreamzProcessor software are the exclusive intellectual property of Kushal Bera.

No part of this document or the associated software may be copied, reproduced, modified, distributed, published, reverse engineered, or commercially exploited without prior written permission from the copyright owner.

Commercial licensing is available only through written authorization from Kushal Bera.

---

# Confidentiality Notice

This document contains proprietary software design information relating to the SweetDreamzProcessor project.

It defines the software requirements necessary to implement the approved Business Specification.

Distribution of this document is permitted only with the written authorization of the copyright owner.

---

# Document Information

| Item | Value |
|------|-------|
| Project | SweetDreamzProcessor |
| Document | Software Design Specification |
| Version | 1.0.0 |
| Status | Design Freeze |
| Author | Kushal Bera |
| Owner | Kushal Bera |
| Copyright | © 2026 Kushal Bera |

---

# Document Control

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0.0 | 2026 | Kushal Bera | Initial Software Design Specification |

---

# References

This document is derived from:

- Business_Specification.md

All software requirements defined herein trace back to approved business requirements contained in the Business Specification.

---

# Authority Statement

This document defines the software requirements for SweetDreamzProcessor.

The implementation shall conform to this specification.

Where conflicts exist between this document and the Business Specification, the Business Specification shall take precedence.

---

# 1. Introduction

This document defines the software requirements for the SweetDreamzProcessor application.

It translates approved business rules into functional and non-functional software requirements.

It does not describe implementation details or software architecture.

Those subjects are defined in the Software Architecture document.

---

# 2. Purpose

The purpose of this specification is to define the behaviour required from the SweetDreamzProcessor software.

This document serves as the foundation for:

- Software Architecture
- Source Code
- Test Strategy
- System Verification
- Future Enhancements

---

# 3. Scope

This specification defines:

- Functional requirements
- Non-functional requirements
- System behaviour
- Data requirements
- Error handling
- Logging
- Performance expectations
- External interfaces

Business rules remain defined by the Business Specification.

---

# 4. System Overview

SweetDreamzProcessor is a desktop application that processes Sweet Dreamz lottery workbooks.

The software reads eligible lottery draws, generates two independent arrangement outputs, preserves workbook integrity, and records processing statistics.

The application shall implement all approved business rules defined by the Business Specification.

Design Constraint – Workbook Preservation

The software shall never modify the original worksheet structure except for completing missing arrangement headers required by the approved Business Specification.

The Date, 1st Prize and 2nd Prize columns, together with all existing worksheet data, shall remain unchanged throughout processing.

The processor shall never insert, delete, move or overwrite worksheet columns that contain existing data.

---

---

# 5. Functional Requirements

## Overview

The functional requirements define the software capabilities required to satisfy the approved Business Specification.

Every functional requirement traces back to one or more Business Specification rules.

The system shall implement all mandatory functional requirements before Version 1.0 is released.

---

## FR-001 — Process One Lottery Draw

### Derived From

DRAW-001

### Description

The system shall process one eligible lottery draw at a time.

Each lottery draw shall be completed before processing begins for the next lottery draw.

### Input

One workbook row containing:

- Draw Date
- First Prize
- Second Prize

### Output

Processed Number Wise Arrangement.

Processed Last Digit Arrangement.

Updated Processing Statistics.

### Acceptance Criteria

- One workbook row produces one independent processing result.
- Processing never combines data from different lottery draws.

### Priority

High

### Status

Implemented

---

## FR-002 — Read Lottery Draw Data

### Derived From

DRAW-002

### Description

The system shall read the Draw Date, First Prize and Second Prize belonging to the same lottery draw.

### Acceptance Criteria

- Draw data is read correctly.
- Invalid rows are ignored.

### Priority

High

### Status

Implemented

---

## FR-003 — Validate Lottery Numbers

### Derived From

NUM-001

### Description

The system shall validate each lottery number independently.

Only valid five-digit lottery numbers shall be processed.

### Acceptance Criteria

- Valid numbers continue processing.
- Invalid numbers are ignored.

### Priority

High

### Status

Implemented

---

## FR-004 — Decompose Lottery Number

### Derived From

NUM-001

### Description

The system shall decompose every valid lottery number into:

- Series
- Middle Pair
- Last Pair

### Acceptance Criteria

Every valid lottery number produces exactly three business components.

### Priority

High

### Status

Implemented

---

## FR-005 — Generate Number Wise Arrangement

### Derived From

ARR-001

### Description

The system shall generate the Number Wise Arrangement for every eligible lottery draw.

The Middle Pair determines the destination Arrangement Block.

### Acceptance Criteria

- Arrangement Blocks are generated correctly.
- Placement follows the Business Specification.

### Priority

High

### Status

Implemented

---

## FR-006 — Generate Last Digit Arrangement

### Derived From

ARR-002

### Description

The system shall generate the Last Digit Arrangement for every eligible lottery draw.

The Last Pair determines the destination Arrangement Block.

### Acceptance Criteria

- Arrangement Blocks are generated correctly.
- Placement follows the Business Specification.

### Priority

High

### Status

Implemented

---

## FR-007 — Preserve Prize Processing Order

### Derived From

ARR-005

### Description

The system shall always process:

1. First Prize
2. Second Prize

When duplicate values occur, the generated comma-separated values shall preserve this order.

### Acceptance Criteria

The generated worksheet always preserves the First Prize before the Second Prize.

### Priority

High

### Status

Implemented

---

## FR-008 — Handle Duplicate Arrangement Values

### Derived From

ARR-003

### Description

The system shall combine duplicate Middle Pair and Last Pair values occurring within the same lottery draw.

Duplicate values shall be written as comma-separated lists.

### Acceptance Criteria

- Duplicate values are combined.
- Processing order is preserved.
- Data from different lottery draws is never combined.

### Priority

High

### Status

Implemented

---

## FR-009 — Complete Missing Arrangement Headers

### Derived From

ARR-004

### Description

If the arrangement header section is incomplete, the system shall complete only the missing arrangement header blocks.

The system shall preserve all existing worksheet data, workbook structure, and formatting.

The new block shall preserve worksheet formatting and update worksheet mappings.

### Acceptance Criteria

• Missing arrangement headers are created automatically.
• Existing arrangement headers are preserved.
• Existing arrangement data is preserved.
• Date, 1st Prize and 2nd Prize columns remain unchanged.
• Existing worksheet data is never moved or overwritten.
• Workbook formatting is preserved.
• Processing continues normally after completing the headers.

### Priority

Medium

### Status

Planned (Milestone 2)

---

## FR-010 — Determine Arrangement Block State

### Derived From

BLK-001

BLK-002

BLK-003

### Description

The system shall determine whether the destination Arrangement Block is:

- EMPTY
- COMPLETE
- PARTIAL

before writing any processed data.

### Acceptance Criteria

Correct block state is identified before every write operation.

### Priority

High

### Status

Implemented

---

## FR-011 — Write Arrangement Blocks

### Derived From

BLK-001

BLK-002

BLK-003

### Description

The system shall write Arrangement Blocks according to the detected block state.

### Acceptance Criteria

- EMPTY blocks are written.
- COMPLETE blocks are skipped.
- PARTIAL blocks are rewritten.

### Priority

High

### Status

Implemented

---

## FR-012 — Maintain Processing Statistics

### Derived From

WB-005

### Description

The system shall record processing statistics during workbook processing.

### Acceptance Criteria

Statistics accurately reflect processing activity.

### Priority

Medium

### Status

Implemented

---

---

# 6. Non-Functional Requirements

## Overview

Non-functional requirements define the quality attributes of the SweetDreamzProcessor application.

These requirements specify **how** the software shall operate rather than **what** it shall do.

Failure to satisfy a non-functional requirement shall be considered a software defect.

---

## NFR-001 — Workbook Safety

### Description

The system shall protect the workbook from unintended modification.

### Acceptance Criteria

- Completed Arrangement Blocks are never overwritten.
- Workbook validation is completed before processing.
- Workbook verification is completed before modification.
- A backup is created before any workbook is changed.
- Date, 1st Prize and 2nd Prize columns shall never be modified.
- Existing worksheet data shall never be shifted or overwritten.

### Priority

Critical

### Status

Implemented

---

## NFR-002 — Workbook Integrity

### Description

The system shall preserve the workbook structure throughout processing.

### Acceptance Criteria

The processor shall preserve:

- Fonts
- Borders
- Cell colours
- Number formats
- Row heights
- Column widths
- Merged cells
- Existing formulas (where applicable)
- Existing worksheet layout
- Existing arrangement headers
- Existing arrangement data
- Source worksheet columns

### Priority

Critical

### Status

Implemented

---

## NFR-003 — Deterministic Processing

### Description

The same workbook shall always produce identical output when processed using the same version of the software.

### Acceptance Criteria

Repeated execution produces identical Arrangement Blocks and processing statistics.

### Priority

High

### Status

Implemented

---

## NFR-004 — Data Isolation

### Description

Each lottery draw shall be processed independently.

### Acceptance Criteria

- Data from different dates is never combined.
- Processing one draw does not modify another draw.

### Priority

Critical

### Status

Implemented

---

## NFR-005 — Maintainability

### Description

The software shall follow a modular architecture.

Business rules, workbook operations and presentation logic shall remain separated.

### Acceptance Criteria

- Components have a single responsibility.
- Business logic is not implemented inside workbook writing classes.
- GUI does not contain business logic.

### Priority

High

### Status

Implemented

---

## NFR-006 — Testability

### Description

The software shall support automated testing.

### Acceptance Criteria

- Core components are independently testable.
- Regression testing can be executed using pytest.
- New features include appropriate tests.

### Priority

High

### Status

Implemented

---

## NFR-007 — Reliability

### Description

The software shall continue processing whenever possible without corrupting the workbook.

### Acceptance Criteria

- Invalid lottery numbers are ignored.
- Partial Arrangement Blocks are rewritten.
- Processing statistics accurately record warnings and skipped blocks.
- Missing arrangement headers are completed without altering existing worksheet data.

### Priority

High

### Status

Implemented

---

## NFR-008 — Extensibility

### Description

The software architecture shall support future enhancements with minimal modification to existing components.

### Acceptance Criteria

Future features such as:

- Automatic heading creation
- Additional arrangement algorithms
- GUI improvements
- Workbook verification enhancements

can be added without redesigning the existing architecture.

### Priority

Medium

### Status

Partially Implemented

---

## NFR-009 — Performance

### Description

The software shall process workbooks efficiently while prioritising correctness over speed.

### Acceptance Criteria

- Workbook mappings are cached.
- Unnecessary worksheet searches are avoided.
- Processing completes within an acceptable time for typical workbook sizes.

### Priority

Medium

### Status

Implemented

---

## NFR-010 — Usability

### Description

The software shall be usable by users with little or no programming experience.

### Acceptance Criteria

The application shall provide:

- Clear error messages
- Processing summary
- Save As dialog
- Suggested output filename
- Simple GUI workflow

### Priority

Medium

### Status

Partially Implemented (Milestone 3)

---

## NFR-011 — Logging

### Description

All significant processing events shall be recorded.

### Acceptance Criteria

The application logs:

- Processing start
- Processing finish
- Warnings
- Errors
- Skipped blocks
- Rewritten blocks

### Priority

Medium

### Status

Implemented

---

## NFR-012 — Documentation

### Description

All software behaviour shall be documented and traceable.

### Acceptance Criteria

Every implemented feature shall be reflected in:

- Business Specification
- Software Design Specification
- Software Architecture
- Test Strategy
- Changelog

### Priority

High

### Status

Implemented

---

---

# 7. Operational Requirements

## Overview

Operational requirements define how the SweetDreamzProcessor application interacts with users, workbook files, the operating system, and external resources.

These requirements govern the application's operational behaviour rather than its internal business logic.

---

## OR-001 — Workbook Selection

### Description

The application shall allow the user to select an input workbook from the local file system.

### Acceptance Criteria

- Only supported workbook formats may be selected.
- Invalid selections shall display an appropriate error message.
- Processing shall not begin until a valid workbook has been selected.

### Priority

High

### Status

Implemented

---

## OR-002 — Workbook Validation

### Description

Before processing begins, the application shall validate the selected workbook.

### Acceptance Criteria

The application shall verify:

- Workbook can be opened.
- Required worksheets exist.
- Required source columns exist.
- Workbook structure is supported.

Processing shall stop if validation fails.

### Priority

Critical

### Status

Implemented

---

## OR-003 — Workbook Verification

### Description

The application shall verify worksheet mappings and destination structures before modifying the workbook.

### Acceptance Criteria

Verification shall complete successfully before processing begins.

### Priority

Critical

### Status

Implemented

---

## OR-004 — Backup Creation

### Description

A backup copy of the workbook shall be created before any modification occurs.

### Acceptance Criteria

- Backup filename is unique.
- Original workbook remains unchanged.
- Processing stops if backup creation fails.

### Priority

Critical

### Status

Implemented

---

## OR-005 — Save As Workflow

### Description

The application shall allow the user to choose the location and filename of the processed workbook.

### Acceptance Criteria

- A Save As dialog is displayed.
- The user may choose any writable folder.
- The user may modify the suggested filename before saving.
- Processing does not overwrite the original workbook unless explicitly chosen by the user.

### Priority

High

### Status

Planned (Milestone 2)

---

## OR-006 — Suggested Output Filename

### Description

The application shall automatically generate a suggested output filename.

### Example

```
Lottery.xlsx
```

Suggested filename

```
Lottery_Modified_KB.xlsx
```

### Acceptance Criteria

- Suggested filename preserves the original extension.
- User may edit the suggested filename.
- User may save using any filename.

### Priority

High

### Status

Implemented

---

## OR-007 — Processing Summary

### Description

After processing completes, the application shall display a processing summary.

### Acceptance Criteria

The summary shall include:

- Total rows processed
- Eligible rows
- Skipped rows
- Arrangement Blocks written
- Arrangement Blocks skipped
- Warnings
- Errors
- Processing duration

### Priority

Medium

### Status

Partially Implemented

---

## OR-008 — Error Reporting

### Description

The application shall display meaningful error messages whenever processing cannot continue.

### Acceptance Criteria

Errors shall identify:

- Cause
- Possible resolution
- Processing status

The application shall not terminate unexpectedly.

### Priority

High

### Status

Implemented

---

## OR-009 — User Cancellation

### Description

The user shall be able to cancel workbook selection or save operations.

### Acceptance Criteria

- Canceling an operation does not modify the workbook.
- The application returns to an idle state.

### Priority

Medium

### Status

Planned (Milestone 3)

---

## OR-010 — Processing Completion

### Description

The application shall notify the user when workbook processing completes successfully.

### Acceptance Criteria

The notification shall indicate:

- Processing completed successfully.
- Output workbook location.
- Processing summary is available.

### Priority

Medium

### Status

Planned (Milestone 3)

---

## OR-011 — Supported Workbook Formats

### Description

The application shall process Microsoft Excel workbooks.

### Acceptance Criteria

Supported formats:

- .xlsx

Unsupported formats shall be rejected.

### Priority

High

### Status

Implemented

---

## OR-012 — Configuration Independence

### Description

The application shall operate without requiring manual configuration files for normal operation.

### Acceptance Criteria

A new user can process a supported workbook immediately after installation.

### Priority

Medium

### Status

Implemented

---

---

# 8. System Responsibilities

## Overview

SweetDreamzProcessor is composed of several logical responsibilities that together implement the approved business requirements.

These responsibilities describe **what the software must accomplish** without defining **how the software is implemented**.

The allocation of these responsibilities to software components is defined in the Software Architecture document.

---

## SR-001 — Workbook Management

### Description

The system shall manage workbook access throughout the processing lifecycle.

### Responsibilities

- Open workbook
- Read workbook
- Access worksheets
- Save workbook
- Close workbook safely

### Related Requirements

FR-001

FR-012

OR-001

OR-005

---

## SR-002 — Workbook Validation

### Description

The system shall validate workbook structure before processing.

### Responsibilities

- Validate workbook format
- Validate worksheets
- Validate required columns
- Validate workbook integrity

### Related Requirements

OR-002

WB-001

---

## SR-003 — Workbook Verification

### Description

The system shall verify workbook mappings and destination structures before modification.

### Responsibilities

- Verify worksheet mappings
- Verify destination blocks
- Verify workbook consistency

### Related Requirements

OR-003

WB-002

---

## SR-004 — Lottery Number Processing

### Description

The system shall process eligible lottery draws.

### Responsibilities

- Read lottery draw
- Validate lottery numbers
- Split lottery numbers
- Generate business data

### Related Requirements

FR-001

FR-002

FR-003

FR-004

---

## SR-005 — Arrangement Generation

### Description

The system shall generate worksheet arrangements.

### Responsibilities

Generate:

- Number Wise Arrangement
- Last Digit Arrangement

Maintain:

- Prize processing order
- Duplicate handling

### Related Requirements

FR-005

FR-006

FR-007

FR-008

---

## SR-006 — Arrangement Block Management

### Description

The system shall manage Arrangement Blocks.

### Responsibilities

• Detect missing arrangement headers
• Complete missing arrangement headers
• Preserve existing arrangement headers
• Preserve existing arrangement data
• Detect block state
• Protect completed blocks
• Rewrite partial blocks

### Related Requirements

FR-009

FR-010

FR-011

---

## SR-007 — Workbook Writing

### Description

The system shall safely write generated Arrangement Blocks into the workbook.

### Responsibilities

• Preserve workbook formatting
• Preserve workbook structure
• Preserve source worksheet columns
• Preserve existing arrangement headers
• Preserve existing arrangement data
• Write generated arrangement blocks
• Never overwrite unrelated worksheet data

### Related Requirements

NFR-001

NFR-002

FR-011

---

## SR-008 — Processing Statistics

### Description

The system shall collect processing statistics.

### Responsibilities

Track:

- Processed draws
- Eligible draws
- Skipped draws
- Written blocks
- Rewritten blocks
- Warnings
- Errors
- Processing duration

### Related Requirements

FR-012

OR-007

---

## SR-009 — User Interaction

### Description

The system shall provide an interface for users to operate the application.

### Responsibilities

- Select workbook
- Display errors
- Display processing summary
- Save processed workbook

### Related Requirements

OR-001

OR-005

OR-007

OR-008

OR-010

---

## SR-010 — Logging

### Description

The system shall record significant processing events.

### Responsibilities

Log:

- Processing start
- Processing finish
- Validation failures
- Verification failures
- Warnings
- Errors

### Related Requirements

NFR-011

---

---

# 9. User Workflows

## Overview

User workflows describe how a user interacts with the SweetDreamzProcessor application.

Each workflow defines a complete operational sequence from the user's perspective.

These workflows do not describe internal implementation details.

---

# UW-001 — Process Workbook

## Objective

Process a Sweet Dreamz workbook and generate the required arrangements.

## Preconditions

- The application is running.
- A valid workbook is available.

## Main Workflow

1. Launch the application.
2. Select the input workbook.
3. The system validates the workbook.
4. The system verifies workbook structure.
5. A backup is created.
6. Every eligible lottery draw is processed.
7. Number Wise Arrangement Blocks are generated.
8. Last Digit Arrangement Blocks are generated.
9. Processing statistics are updated.
10. The Save As dialog is displayed.
11. The user selects the destination folder.
12. The user confirms or edits the suggested filename.
13. The workbook is saved.
14. Processing summary is displayed.

## Postconditions

- Processed workbook exists.
- Original workbook remains unchanged.
- Processing statistics are available.

---

# UW-002 — Save Processed Workbook

## Objective

Allow the user to save the processed workbook.

## Preconditions

Processing completed successfully.

## Main Workflow

1. Save As dialog opens.
2. Suggested filename is displayed.
3. User selects destination folder.
4. User may modify the filename.
5. User clicks Save.
6. Workbook is written to disk.

## Alternative Flow

If the selected filename already exists:

- The user is asked whether the existing file should be replaced.
- If the user cancels, processing remains complete but the workbook is not saved.

## Postconditions

Processed workbook exists at the selected location.

---

# UW-003 — Invalid Workbook

## Objective

Prevent processing of unsupported workbooks.

## Preconditions

User selects an invalid workbook.

## Main Workflow

1. User selects workbook.
2. Validation begins.
3. Validation fails.
4. Error message is displayed.
5. Processing stops.

## Postconditions

- Workbook remains unchanged.
- Processing does not begin.

---

# UW-004 — User Cancels Workbook Selection

## Objective

Allow the user to safely cancel workbook selection.

## Main Workflow

1. User opens the file selection dialog.
2. User clicks Cancel.

## Expected Behaviour

- No workbook is loaded.
- No processing occurs.
- Application returns to the idle state.

---

# UW-005 — User Cancels Save Operation

## Objective

Allow the user to cancel saving the processed workbook.

## Preconditions

Processing completed successfully.

## Main Workflow

1. Save As dialog opens.
2. User clicks Cancel.

## Expected Behaviour

- Processed workbook is not written.
- Original workbook remains unchanged.
- Processing statistics remain available.
- Application returns to the idle state.

---

# UW-006 — Processing Failure

## Objective

Handle unexpected processing errors safely.

## Main Workflow

1. Processing begins.
2. Unexpected error occurs.
3. Processing stops.
4. Error is logged.
5. Error message is displayed.
6. Original workbook remains unchanged.

## Postconditions

- Workbook integrity is preserved.
- User is informed of the failure.

---

---

# 10. Error Handling

## Overview

The system shall detect, report, and recover from expected processing errors whenever possible.

Error handling shall prioritize:

1. Workbook integrity
2. User safety
3. Data preservation
4. Clear user communication

Errors shall never leave the workbook in an inconsistent state.

---

## Error Severity Levels

| Level | Description | Processing Behaviour |
|---------|-------------|----------------------|
| Information | Normal processing event | Continue |
| Warning | Recoverable issue | Continue processing |
| Error | Processing cannot continue | Stop current operation |
| Critical | Workbook integrity at risk | Abort processing immediately |

---

## ERR-001 — Workbook Not Found

### Description

The selected workbook cannot be found.

### System Response

- Display an error message.
- Do not begin processing.
- Return to the idle state.

### Severity

Error

---

## ERR-002 — Unsupported Workbook Format

### Description

The selected file is not a supported workbook.

### System Response

- Display an error message.
- Reject the file.
- Allow the user to select another workbook.

### Severity

Error

---

## ERR-003 — Workbook Validation Failed

### Description

The workbook does not satisfy the required structure.

Examples include:

- Missing worksheet
- Missing required columns
- Invalid workbook layout

### System Response

- Display validation failure.
- Stop processing.
- Do not modify the workbook.

### Severity

Critical

---

## ERR-004 — Workbook Verification Failed

### Description

Workbook verification failed before processing.

### System Response

- Display verification failure.
- Stop processing.
- Do not modify the workbook.

### Severity

Critical

---

## ERR-005 — Backup Creation Failed

### Description

The backup workbook could not be created.

### System Response

- Stop processing immediately.
- Inform the user.
- Leave the original workbook unchanged.

### Severity

Critical

---

## ERR-006 — Invalid Lottery Number

### Description

A lottery number is blank, malformed, or not a valid five-digit value.

### System Response

- Ignore the invalid number.
- Continue processing any remaining valid numbers within the same draw.
- Record the event in the processing statistics.

### Severity

Warning

---

## ERR-007 — Ineligible Lottery Draw

### Description

The current workbook row does not contain any valid prize numbers.

### System Response

- Skip the draw.
- Continue processing the next draw.
- Update processing statistics.

### Severity

Information

---

## ERR-008 — Missing Arrangement Block

### Description

The required destination Arrangement Block cannot be located.

### System Response

Current Behaviour

- Stop processing.
- Inform the user.

System Response

• Detect the incomplete arrangement header section.
• Create only the missing arrangement headers.
• Preserve all existing worksheet data.
• Preserve workbook formatting.
• Refresh worksheet mappings.
• Continue processing automatically.

### Severity

Error

---

## ERR-009 — Partial Arrangement Block

### Description

The destination Arrangement Block contains incomplete data.

### System Response

- Rewrite the complete Arrangement Block.
- Record a warning.
- Continue processing.

### Severity

Warning

---

## ERR-010 — Workbook Save Failed

### Description

The processed workbook cannot be saved.

Possible causes include:

- Permission denied
- Destination unavailable
- File already open
- Insufficient disk space

### System Response

- Display the save error.
- Allow the user to select another location.
- Do not lose processing results currently held in memory.

### Severity

Error

---

## ERR-011 — Unexpected Processing Exception

### Description

An unexpected software error occurred.

### System Response

- Stop processing safely.
- Preserve workbook integrity.
- Record diagnostic information.
- Display an unexpected error message.

### Severity

Critical

---

## Error Handling Principles

The system shall always follow these principles:

- Never overwrite completed workbook data after an unrecoverable error.
- Never corrupt workbook formatting.
- Preserve the original workbook whenever processing fails.
- Display clear and meaningful error messages.
- Continue processing whenever recovery is safe.
- Stop processing immediately whenever workbook integrity cannot be guaranteed.

---

---

# 11. Monitoring & Logging Requirements

## Overview

The system shall monitor significant processing events and maintain sufficient logging information to support troubleshooting, auditing, and software maintenance.

Monitoring information shall provide visibility into processing progress and software behaviour without affecting workbook integrity.

---

## MLR-001 — Processing Lifecycle Logging

### Description

The system shall record the start and completion of every processing session.

### Logged Information

- Processing start time
- Processing completion time
- Processing duration
- Processing result

### Priority

High

### Status

Implemented

---

## MLR-002 — Workbook Logging

### Description

The system shall record workbook-related events.

### Logged Information

- Workbook selected
- Workbook validation
- Workbook verification
- Backup creation
- Workbook save

### Priority

High

### Status

Implemented

---

## MLR-003 — Arrangement Processing Logging

### Description

The system shall record arrangement generation events.

### Logged Information

- Eligible draws processed
- Number Wise Arrangement generated
- Last Digit Arrangement generated
- Arrangement Blocks written
- Arrangement Blocks skipped
- Arrangement Blocks rewritten
- Missing arrangement headers completed

### Priority

High

### Status

Implemented

---

## MLR-004 — Warning Logging

### Description

The system shall record all recoverable processing issues.

### Logged Information

Examples include:

- Invalid lottery numbers
- Partial Arrangement Blocks
- Skipped rows
- Duplicate handling events

Processing shall continue whenever recovery is possible.

### Priority

Medium

### Status

Implemented

---

## MLR-005 — Error Logging

### Description

The system shall record all processing errors.

### Logged Information

- Validation failures
- Verification failures
- Backup failures
- Save failures
- Unexpected exceptions

### Priority

High

### Status

Implemented

---

## MLR-006 — Processing Statistics

### Description

The system shall maintain processing statistics throughout the processing lifecycle.

### Statistics

- Total workbook rows
- Eligible draws
- Skipped draws
- Invalid numbers
- Arrangement Blocks written
- Arrangement Blocks skipped
- Arrangement Blocks rewritten
- Warning count
- Error count
- Processing duration

### Priority

High

### Status

Implemented

---

## MLR-007 — User Processing Summary

### Description

After successful processing, the system shall present a processing summary to the user.

### Summary Information

- Workbook processed
- Destination workbook
- Processing duration
- Total eligible draws
- Total skipped draws
- Arrangement Blocks written
- Warnings
- Errors

### Priority

Medium

### Status

Partially Implemented

---

## Logging Principles

The logging system shall:

- Never modify workbook data.
- Never expose confidential workbook contents.
- Record sufficient information for debugging.
- Support future diagnostic enhancements.

---

---

# 12. Performance Requirements

## Overview

The system shall provide consistent performance while prioritising correctness, workbook integrity, and maintainability.

Correctness shall always take precedence over execution speed.

---

## PERF-001 — Processing Performance

### Description

The system shall process eligible lottery draws efficiently.

### Requirement

Processing time shall scale approximately linearly with the number of eligible workbook rows.

### Priority

Medium

---

## PERF-002 — Workbook Search Optimisation

### Description

Worksheet lookups shall avoid unnecessary repeated searches.

### Requirement

Worksheet mappings shall be reused whenever possible.

### Priority

Medium

---

## PERF-003 — Memory Usage

### Description

The system shall minimise unnecessary memory allocation.

### Requirement

Only the data required for the current processing session shall be retained.

### Priority

Medium

---

## PERF-004 — Startup Performance

### Description

The application shall become ready for workbook selection without unnecessary delay.

### Priority

Low

---

## PERF-005 — Scalability

### Description

The software architecture shall support larger workbooks without requiring architectural redesign.

### Requirement

Performance shall degrade predictably as workbook size increases.

### Priority

Medium

---

---

# 13. Requirement Traceability

The following matrix establishes traceability between the Business Specification and the Software Design Specification.

| Business Rule | Functional Requirement |
|---------------|------------------------|
| DRAW-001 | FR-001 |
| DRAW-002 | FR-002 |
| NUM-001 | FR-003, FR-004 |
| ARR-001 | FR-005 |
| ARR-002 | FR-006 |
| ARR-003 | FR-008 |
| ARR-004 | FR-009 |
| ARR-005 | FR-007 |
| BLK-001 | FR-010, FR-011 |
| BLK-002 | FR-010, FR-011 |
| BLK-003 | FR-010, FR-011 |
| WB-001 | OR-002 |
| WB-002 | OR-003 |
| WB-003 | OR-004 |
| WB-004 | NFR-002 |
| WB-005 | FR-011 |

Every software requirement shall be traceable to an approved business rule.

Requirements without business traceability shall not be implemented without approval.

---
---

# 14. Future Requirements

The following approved features are planned for future milestones.

| ID | Feature | Status |
|----|---------|--------|
| FUT-001 | Automatic Non-Destructive Arrangement Header Completion | Planned |
| FUT-002 | Enhanced Save As workflow | Planned |
| FUT-003 | Improved processing summary dialog | Planned |
| FUT-004 | Advanced logging export | Future |
| FUT-005 | Additional workbook validation rules | Future |
| FUT-006 | Performance optimisation for large workbooks | Future |
| FUT-007 | User configuration options | Future |

Future requirements shall first be approved within the Business Specification before implementation.

---

---

# 15. Summary

This Software Design Specification defines the software behaviour required to implement the approved Business Specification.

It establishes:

- Functional Requirements
- Non-Functional Requirements
- Operational Requirements
- System Responsibilities
- User Workflows
- Error Handling
- Monitoring and Logging
- Performance Requirements
- Requirement Traceability
- Future Software Requirements

This document serves as the authoritative software requirements specification for the SweetDreamzProcessor project.

The Software Architecture document shall implement the requirements defined herein.

No software implementation shall intentionally diverge from this specification without corresponding updates to both the Business Specification and this Software Design Specification.