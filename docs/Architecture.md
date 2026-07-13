# SweetDreamzProcessor

# Software Architecture

---

# Copyright Notice

Copyright © 2026 Kushal Bera. All Rights Reserved.

This document and the SweetDreamzProcessor software architecture are the exclusive intellectual property of Kushal Bera.

No part of this document may be copied, reproduced, modified, distributed, published, reverse engineered, or commercially exploited without prior written permission from the copyright owner.

Commercial licensing is available only through written authorization from Kushal Bera.

---

# Confidentiality Notice

This document contains proprietary software architecture information relating to the SweetDreamzProcessor project.

It defines the architectural organization required to implement the approved Software Design Specification.

Distribution of this document is permitted only with written authorization from the copyright owner.

---

# Document Information

| Item | Value |
|------|-------|
| Project | SweetDreamzProcessor |
| Document | Software Architecture |
| Version | 1.0.0 |
| Status | Design Freeze |
| Author | Kushal Bera |
| Owner | Kushal Bera |
| Copyright | © 2026 Kushal Bera |

---

# Document Control

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0.0 | 2026 | Kushal Bera | Initial Software Architecture |

---

# References

This document is derived from:

- Business_Specification.md
- Software_Design_Specification.md

The architecture defined in this document implements the software requirements defined by the Software Design Specification.

---

# Authority Statement

This document defines the approved software architecture for SweetDreamzProcessor.

All implementation shall conform to this architecture unless formally revised.

If conflicts exist:

Business Specification

↓

Software Design Specification

↓

Software Architecture

↓

Source Code

The higher-level document always takes precedence.

---

# Architectural Constraint

The worksheet layout is considered business data.

The architecture shall preserve:

• Date
• 1st Prize
• 2nd Prize
• Existing arrangement headers
• Existing arrangement data

Automatic processing may only complete missing arrangement headers.

No architectural component shall insert, delete, move or overwrite unrelated worksheet data.

---

# 1. Introduction

This document defines the software architecture of SweetDreamzProcessor.

It describes the organization of software components, their responsibilities, interactions, dependencies, and processing flow.

This document intentionally excludes implementation details.

---

# 2. Purpose

The purpose of this document is to provide a stable architectural blueprint for the implementation and future evolution of SweetDreamzProcessor.

It serves as the reference for:

- Software implementation
- Code reviews
- Future enhancements
- Testing strategy
- Long-term maintenance

---

# 3. Scope

This document defines:

- Architectural principles
- Software layers
- Component responsibilities
- Data flow
- Processing pipeline
- Component interactions
- Dependency rules
- Extension points

Business behaviour remains defined by the Business Specification.

Software requirements remain defined by the Software Design Specification.

---

# 4. Architectural Goals

The architecture of SweetDreamzProcessor has been designed to satisfy the following objectives.

The architecture shall preserve all existing worksheet data.

Existing source columns, arrangement headers and processed data shall never be altered except where explicitly required by the approved Business Specification.

---

## AG-001 — Correctness

Business rules shall be implemented consistently and deterministically.

---

## AG-002 — Workbook Safety

Workbook integrity shall take precedence over processing performance.

---

## AG-003 — Maintainability

Software components shall remain small, focused, and independently maintainable.

---

## AG-004 — Modularity

Each architectural component shall have one clearly defined responsibility.

---

## AG-005 — Extensibility

Future features shall be added with minimal impact on existing components.

---

## AG-006 — Testability

Business logic shall be structured to support independent automated testing.

---

## AG-007 — Separation of Concerns

Business processing, workbook operations, and user interaction shall remain independent.

---

# 5. Architectural Principles

The architecture of SweetDreamzProcessor follows a set of guiding principles that ensure the software remains maintainable, extensible, and reliable throughout its lifecycle.

---

## AP-001 — Single Responsibility Principle

Every architectural component shall have one clearly defined responsibility.

A component shall perform one primary task and shall not assume responsibilities belonging to other components.

---

## AP-002 — Separation of Concerns

The architecture separates:

- User Interface
- Workbook Operations
- Business Processing
- Arrangement Generation
- Workbook Writing
- Processing Statistics

Each concern shall remain independent.

---

## AP-003 — Business Rule Isolation

Business rules shall remain independent from workbook access and graphical user interface logic.

Business processing shall not directly manipulate workbook files.

---

## AP-004 — Dependency Direction

Higher-level business processing shall not depend on low-level implementation details.

Dependencies shall flow toward infrastructure components.

---

## AP-005 — Deterministic Behaviour

Identical input workbooks shall always produce identical output workbooks.

The architecture shall preserve deterministic behaviour across all processing stages.

---
## AP-005A — Non-Destructive Worksheet Modification

The architecture shall modify only those worksheet cells required to satisfy approved business rules.

The architecture shall never:

• delete worksheet columns
• insert worksheet columns that shift existing data
• overwrite unrelated worksheet data
• modify source worksheet columns

Only missing arrangement headers may be created automatically.

---

## AP-006 — Extensibility

Future enhancements shall require minimal modification to existing architectural components.

Whenever possible, new functionality shall be added through new components rather than modifying stable components.

---

## AP-007 — Testability

Architectural components shall be independently testable.

Business processing components shall not require a graphical user interface during testing.

---

# 6. Overall Architecture

The SweetDreamzProcessor architecture is organised into logical layers.

Each layer has a distinct responsibility.

```text
+------------------------------------------------------+
|                 User Interface Layer                 |
|------------------------------------------------------|
| GUI                                                  |
+------------------------------------------------------+
                       │
                       ▼
+------------------------------------------------------+
|              Application Service Layer               |
|------------------------------------------------------|
| SweetDreamzProcessor                                 |
+------------------------------------------------------+
                       │
                       ▼
+------------------------------------------------------+
|               Business Processing Layer              |
|------------------------------------------------------|
| Row Detection                                        |
| Number Extraction                                    |
| Number Arrangement                                   |
| Block Detection                                      |
| Statistics                                            |
+------------------------------------------------------+
                       │
                       ▼
+------------------------------------------------------+
|              Workbook Service Layer                  |
|------------------------------------------------------|
| Workbook Manager                                     |
| Workbook Validator                                   |
| Workbook Verifier                                    |
| Workbook Mapper                                      |
| Workbook Writer                                      |
| Backup Manager                                       |
+------------------------------------------------------+
                       │
                       ▼
+------------------------------------------------------+
|                 Infrastructure Layer                 |
|------------------------------------------------------|
| Excel Workbook                                       |
| File System                                          |
| Operating System                                     |
+------------------------------------------------------+
```

Each layer communicates only with the layer directly below it.

This architecture minimizes coupling and improves maintainability.

---

# 7. Layer Responsibilities

Each architectural layer has a clearly defined responsibility.

---

## User Interface Layer

Responsible for:

- User interaction
- File selection
- Save As workflow
- Progress reporting
- Error presentation

This layer contains no business rules.

---

## Application Service Layer

Responsible for:

- Coordinating workbook processing
- Managing the overall processing workflow
- Invoking business services
- Returning processing results

This layer orchestrates the processing lifecycle but does not implement business rules directly.

---

## Business Processing Layer

Responsible for:

- Row eligibility detection
- Lottery number decomposition
- Arrangement generation
- Block state detection
- Processing statistics

This layer implements the approved business rules defined in the Business Specification.

---

## Workbook Service Layer

Responsible for:

- Workbook access
- Workbook validation
- Workbook verification
- Worksheet mapping
- Workbook writing
- Backup creation

This layer manages workbook operations but contains no business logic.

---

## Infrastructure Layer

Responsible for:

- Excel workbook storage
- File system operations
- Operating system interaction

This layer represents external dependencies and is isolated from business processing.

---

# 8. Architectural Components

The architecture is composed of the following logical components.

| Component | Responsibility |
|-----------|----------------|
| SweetDreamzProcessor | Coordinates the complete processing workflow |
| Workbook Manager | Provides workbook access and save operations |
| Workbook Validator | Validates workbook structure |
| Workbook Verifier | Verifies worksheet mappings before processing |
| Backup Manager | Creates workbook backups |
| Row Detector | Identifies eligible lottery draws |
| Number Extractor | Extracts valid lottery numbers |
| Number Arranger | Generates Number Wise and Last Digit arrangements |
| Block Detector | Determines Arrangement Block state |
| Workbook Writer | Writes Arrangement Blocks into worksheets without modifying unrelated worksheet data. |
| Processing Statistics | Records processing metrics |
| GUI | Provides user interaction |
| Workbook Mapper |     Locate Number Wise Arrangement blocks.
                        Locate Last Digit Arrangement blocks.
                        Detect missing arrangement headers.
                        Maintain worksheet mapping cache.
                        Refresh worksheet mappings after header completion. |
| Block Creator | Completes missing arrangement headers while preserving existing worksheet structure. |


---

# 9. Component Specifications

## Overview

Each architectural component has a single, clearly defined responsibility.

Components collaborate to implement the functional requirements defined by the Software Design Specification while remaining independent and testable.

Each component shall expose only the behaviour required by its responsibility.

---

# COMP-001 — Application Controller

## Purpose

Coordinate the complete workbook processing workflow.

## Responsibilities

- Coordinate workbook processing.
- Control processing sequence.
- Invoke business processing components.
- Coordinate workbook services.
- Return processing statistics.

## Inputs

- Workbook path
- Processing request

## Outputs

- Processing statistics
- Processed workbook

## Depends On

- Workbook Services
- Business Processing Components

## Related Requirements

FR-001

FR-012

OR-005

---

# COMP-002 — Workbook Manager

## Purpose

Provide safe access to workbook data.

## Responsibilities

- Open workbook.
- Save workbook.
- Access worksheets.
- Read cell values.
- Write cell values.
- Close workbook safely.
- Generate suggested output filename.

## Inputs

Workbook file.

## Outputs

Workbook object.

Worksheet access.

## Depends On

Infrastructure Layer.

## Related Requirements

OR-001

OR-005

OR-006

---

# COMP-003 — Workbook Validator

## Purpose

Validate workbook structure before processing.

## Responsibilities

- Validate workbook.
- Validate worksheets.
- Validate required columns.
- Detect unsupported workbook structures.

## Related Requirements

OR-002

WB-001

---

# COMP-004 — Workbook Verifier

## Purpose

Verify workbook consistency before modification.

## Responsibilities

- Verify worksheet mappings.
- Verify destination structure.
- Verify arrangement layout.

## Related Requirements

OR-003

WB-002

---

# COMP-005 — Workbook Mapper

## Purpose

Locate and map worksheet Arrangement Blocks.

## Responsibilities

- Locate Number Wise Arrangement blocks.
- Locate Last Digit Arrangement blocks.
- Maintain worksheet mapping cache.
- Detect missing arrangement headers.
- Refresh worksheet mappings after header completion.

## Related Requirements

FR-010

PERF-002

---

# COMP-005A — Block Creator
## Purpose

Complete missing arrangement headers.

## Responsibilities

• Create missing Number Wise headers.
• Create missing Last Digit headers.
• Preserve existing worksheet data.
• Preserve existing worksheet structure.
• Never overwrite existing workbook data.

## Inputs

Worksheet
Arrangement mapping

## Outputs

Updated worksheet structure

## Depends On

Workbook Manager

## Related Requirements

FR-009

---

# COMP-006 — Backup Manager

## Purpose

Protect workbook integrity before modification.

## Responsibilities

- Create workbook backup.
- Generate backup filename.
- Preserve original workbook.

## Related Requirements

OR-004

WB-003

---

# COMP-007 — Row Detector

## Purpose

Determine whether a lottery draw is eligible for processing.

## Responsibilities

- Evaluate workbook row.
- Detect eligible draws.
- Ignore invalid rows.

## Related Requirements

FR-001

FR-002

---

# COMP-008 — Number Extractor

## Purpose

Extract valid lottery numbers from a lottery draw.

## Responsibilities

- Read First Prize.
- Read Second Prize.
- Validate numbers.
- Ignore invalid numbers.

## Related Requirements

FR-003

---

# COMP-009 — Number Arranger

## Purpose

Generate Arrangement Blocks.

## Responsibilities

Generate:

- Number Wise Arrangement.
- Last Digit Arrangement.

Maintain:

- Prize processing order.
- Duplicate handling.

## Related Requirements

FR-004

FR-005

FR-006

FR-007

FR-008

---

# COMP-010 — Block Detector

## Purpose

Determine the current Arrangement Block state.

## Responsibilities

Detect:

- EMPTY
- COMPLETE
- PARTIAL

## Related Requirements

FR-010

FR-011

---

# COMP-011 — Workbook Writer

## Purpose

Write Arrangement Blocks into worksheets.

## Responsibilities

- Write Number Wise Arrangement Blocks.
- Write Last Digit Arrangement Blocks.
- Preserve formatting.
- Preserve worksheet structure.
- Preserve existing arrangement headers.
- Preserve existing arrangement data.
- Preserve source worksheet columns.
- Write generated Arrangement Blocks only.

## Related Requirements

FR-011

NFR-001

NFR-002

---

# COMP-012 — Processing Statistics

## Purpose

Collect processing metrics.

## Responsibilities

Record:

- Eligible draws.
- Skipped draws.
- Written blocks.
- Rewritten blocks.
- Warning count.
- Error count.
- Processing duration.

## Related Requirements

FR-012

MLR-006

---

# COMP-013 — User Interface

## Purpose

Provide user interaction.

## Responsibilities

- Workbook selection.
- Save As dialog.
- Error messages.
- Processing summary.

## Related Requirements

OR-001

OR-005

OR-007

OR-008

---

# 10. Processing Flow Architecture

## Overview

The Processing Flow Architecture describes how a single lottery draw moves through the architectural components of SweetDreamzProcessor.

Each component performs one specific responsibility before passing control to the next component.

This sequential processing ensures deterministic behaviour, workbook integrity, and maintainability.

---

## 10.1 High-Level Processing Flow

```text
User
 │
 ▼
GUI
 │
 ▼
Application Controller
 │
 ▼
Workbook Manager
 │
 ▼
Workbook Validator
 │
 ▼
Workbook Verifier
 │
 ▼
Workbook Mapper
 │
 ▼
Backup Manager
 │
 ▼
Lottery Draw Processing
 │
 ▼
Workbook Writer
 │
 ▼
Workbook Save
 │
 ▼
Processing Statistics
 │
 ▼
GUI Summary
```

Each stage must complete successfully before processing continues.

---

## 10.2 Lottery Draw Processing Flow

The Application Controller processes one eligible lottery draw at a time.

```text
Lottery Draw
      │
      ▼
Row Detector
      │
      ▼
Number Extractor
      │
      ▼
Number Arranger
      │
      ▼
Block Detector
      │
      ▼
Workbook Writer
      │
      ▼
Processing Statistics
```

Each lottery draw is processed independently.

No architectural component shall combine data originating from different workbook rows.

---

## 10.3 Number Processing Flow

For every valid lottery number:

```text
Lottery Number
       │
       ▼
Validate Number
       │
       ▼
Split Number
       │
 ┌─────┴─────┐
 ▼           ▼
Series   Middle Pair
               │
               ▼
          Last Pair
               │
               ▼
Generate Arrangement Blocks
```

The resulting business data is passed to the Workbook Writer.

---

## 10.4 Arrangement Generation Flow

Each valid lottery number generates two independent Arrangement Blocks.

```text
Lottery Number
       │
       ▼
Split Number
       │
       ├──────────────┐
       ▼              ▼
Number Wise     Last Digit
Arrangement     Arrangement
       │              │
       ▼              ▼
Workbook Writer Workbook Writer
```

The two arrangement paths remain independent throughout processing.

---

## 10.5 Workbook Writing Flow

Before writing any Arrangement Block:

```text
Locate Worksheet Block
        │
        ▼
Arrangement Complete?
        │
 ┌──────┴─────────┐
 │                │
Yes              No
 │                │
 ▼                ▼
Detect       Complete Missing
Block State  Arrangement Headers
 │                │
 └──────┬─────────┘
        ▼
Refresh Mapping
        │
        ▼
Detect Block State
        │
        ▼
 ┌──────┼─────────┐
 ▼      ▼         ▼
EMPTY COMPLETE PARTIAL
 │       │         │
 ▼       ▼         ▼
Write   Skip   Rewrite
```

Completed Arrangement Blocks are never modified.

---

## 10.6 Workbook Save Flow

After all eligible lottery draws have been processed:

```text
Processing Complete
        │
        ▼
Generate Suggested Filename
        │
        ▼
Save As Dialog
        │
        ▼
User Selects Destination
        │
        ▼
Workbook Saved
        │
        ▼
Display Summary
```

The original workbook remains unchanged unless the user explicitly chooses to overwrite it.

---

## 10.7 Processing Principles

The architecture follows these processing principles:

- One lottery draw is processed at a time.
- One architectural component performs one responsibility.
- Processing is deterministic.
- Workbook integrity takes precedence over performance.
- Arrangement Blocks are generated before workbook modification.
- Processing statistics are updated throughout the processing lifecycle.

---

# 11. Component Interaction

## Overview

Architectural components communicate through well-defined responsibilities.

Components shall not bypass intermediate layers.

---

## Interaction Sequence

```text
GUI
 │
 ▼
Application Controller
 │
 ├──────────────┐
 ▼              ▼
Workbook Services
Business Processing
 │              │
 └──────┬───────┘
        ▼
Workbook Writer
        │
        ▼
Workbook Manager
        │
        ▼
Excel Workbook
```

---

## Interaction Rules

### ARCH-001

The GUI shall communicate only with the Application Controller.

---

### ARCH-002

Business Processing components shall not communicate directly with the GUI.

---

### ARCH-003

Workbook Services shall not implement business rules.

---

### ARCH-004

Business Processing components shall not directly modify workbook files.

All workbook modifications shall occur through the Workbook Writer.

---

### ARCH-005

Workbook Writer shall be the only component responsible for writing Arrangement Blocks.

---

### ARCH-006

Processing Statistics may receive information from multiple components but shall not modify processing behaviour.

---

### ARCH-007

The Application Controller coordinates the processing workflow but does not implement business logic.

---

### ARCH-008

Workbook structure shall never be modified except for completing missing arrangement headers required by the Business Specification.

---

# 12. Dependency Rules

## Overview

The architecture follows strict dependency rules to maintain modularity, reduce coupling, and simplify testing.

Dependencies shall always flow from higher architectural layers toward lower architectural layers.

Lower layers shall never depend upon higher layers.

---

## Dependency Hierarchy

```text
User Interface Layer
        │
        ▼
Application Service Layer
        │
        ▼
Business Processing Layer
        │
        ▼
Workbook Service Layer
        │
        ▼
Infrastructure Layer
```

Reverse dependencies are prohibited.

---

## DEP-001 — User Interface

The User Interface layer shall communicate only with the Application Controller.

The User Interface shall never communicate directly with:

- Workbook Manager
- Workbook Writer
- Workbook Validator
- Workbook Verifier
- Number Arranger
- Number Extractor
- Block Detector

---

## DEP-002 — Application Controller

The Application Controller coordinates processing.

It may communicate with:

- Workbook Services
- Business Processing Components
- Processing Statistics

The Application Controller shall not implement business rules.

---

## DEP-003 — Business Processing

Business Processing components may communicate with:

- Other Business Processing components
- Processing Statistics

Business Processing components shall never:

- Access workbook files directly.
- Modify worksheet cells.
- Display user interface elements.

---

## DEP-004 — Workbook Services

Workbook Service components shall communicate only with:

- Infrastructure Layer
- Application Controller

Workbook Services shall never contain business rules.

---

## DEP-005 — Infrastructure

Infrastructure components shall never depend upon business processing components.

They provide services only.

---

## DEP-006 — Dependency Direction

Dependencies shall always flow downward.

Circular dependencies are prohibited.

---

## DEP-007 — Shared Data

Shared data shall be exchanged using well-defined data structures.

Components shall not modify the internal state of unrelated components.

---

# 13. Architectural Design Decisions

## Overview

The following design decisions define the architectural direction of SweetDreamzProcessor.

These decisions shall remain stable unless formally revised.

---

## AD-001 — Layered Architecture

Decision

The software shall use a layered architecture.

Reason

Separates business logic from workbook operations and user interaction.

---

## AD-002 — Single Responsibility

Decision

Each architectural component has one primary responsibility.

Reason

Improves maintainability and testing.

---

## AD-003 — Business Rule Isolation

Decision

Business rules are implemented only within Business Processing components.

Reason

Workbook operations and user interface logic remain independent of business behaviour.

---

## AD-004 — Controller-Oriented Coordination

Decision

The Application Controller coordinates the processing workflow.

Reason

Provides a single orchestration point while preventing business logic from being duplicated.

---

## AD-005 — Workbook Safety First

Decision

Workbook integrity takes precedence over processing performance.

Reason

The original workbook is valuable business data and must be protected.

---

## AD-006 — Deterministic Processing

Decision

Identical input workbooks shall always generate identical output workbooks.

Reason

Ensures predictable behaviour and simplifies testing.

---

## AD-007 — Independent Processing Units

Decision

Each lottery draw is processed independently.

Reason

Business rules prohibit combining data from different dates.

---

## AD-008 — Arrangement Block Model

Decision

The Arrangement Block is the fundamental architectural data unit exchanged between business processing and workbook writing.

Reason

This abstraction isolates business processing from worksheet layout details.

---

## AD-010 — Non-Destructive Header Completion

Decision

The architecture shall complete missing arrangement headers without altering existing worksheet data.

Reason

Preserves workbook integrity while satisfying ARR-004.

---

## AD-009 — Formatting Preservation

Decision

Workbook formatting shall always be preserved.

Reason

Users rely on the workbook's existing appearance and structure.

---

## AD-010 — Extensible Architecture

Decision

Future features shall be implemented by extending the architecture rather than redesigning it.

Reason

Reduces maintenance cost and protects existing functionality.

---

# 15. Future Architecture

The current architecture provides a stable foundation for future development.

The following enhancements have been identified for future milestones.

| ID | Enhancement | Status |
|----|-------------|--------|
| FUT-ARCH-001 | Automatic Non-Destructive Arrangement Header Completion | Planned |
| FUT-ARCH-002 | Enhanced workbook verification | Planned |
| FUT-ARCH-003 | Improved logging framework | Future |
| FUT-ARCH-004 | User configuration management | Future |
| FUT-ARCH-005 | Additional arrangement algorithms | Future |
| FUT-ARCH-006 | Performance optimisation | Future |

Future architectural changes shall maintain compatibility with:

- Business Specification
- Software Design Specification

Architectural revisions shall not invalidate previously approved business rules.

---

# 16. Summary

This document defines the approved software architecture for SweetDreamzProcessor.

It establishes:

- Architectural Goals
- Architectural Principles
- Layered Architecture
- Component Responsibilities
- Processing Flow
- Component Interactions
- Dependency Rules
- Design Decisions
- Extension Points
- Future Architectural Direction

This architecture provides a maintainable, extensible, and testable foundation for implementing the approved Software Design Specification.

All future implementation shall conform to this architecture unless formally revised.