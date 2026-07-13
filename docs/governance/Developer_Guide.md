# SweetDreamzProcessor

# Developer Guide

---

# Copyright Notice

Copyright © 2026 Kushal Bera. All Rights Reserved.

This document and the SweetDreamzProcessor software are the exclusive intellectual property of Kushal Bera.

No part of this document or the associated software may be copied, reproduced, modified, distributed, published, reverse engineered, or commercially exploited without prior written permission from the copyright owner.

Commercial licensing is available only through written authorization from Kushal Bera.

---

# Document Information

| Item | Value |
|------|-------|
| Project | SweetDreamzProcessor |
| Document | Developer Guide |
| Version | 1.0.0 |
| Status | Active |
| Author | Kushal Bera |
| Owner | Kushal Bera |

---

# 1. Purpose

This document defines the development workflow for the SweetDreamzProcessor project.

It provides practical guidance for implementing new features, maintaining existing functionality, and ensuring that all development follows the approved project documentation.

This guide complements the following documents:

- Business_Specification.md
- Software_Design_Specification.md
- Architecture.md
- TestStrategy.md

---

# 2. Project Philosophy

SweetDreamzProcessor is developed using a specification-driven workflow.

The software is implemented from approved documentation rather than ad hoc coding.
Workbook preservation is a core architectural principle.

Unless explicitly required by the approved Business Specification, existing worksheet structure, worksheet data, arrangement headers, and workbook formatting shall never be modified.

Every feature shall be:

1. Designed.
2. Documented.
3. Implemented.
4. Tested.
5. Released.

This approach ensures maintainability, traceability, and long-term project stability.

---

# 3. Development Workflow

Every feature follows the same workflow.

```text
Business Specification
        │
        ▼
Software Design Specification
        │
        ▼
Architecture
        │
        ▼
Test Strategy
        │
        ▼
Implementation
        │
        ▼
Pytest
        │
        ▼
Workbook Preservation Verification
        │
        ▼
Manual Workbook Testing
        │
        ▼
Git Commit
        │
        ▼
CHANGELOG Update
```

No feature is considered complete until all steps have been completed successfully.

---

# 4. Coding Principles

All source code shall follow these principles.

## Single Responsibility

Each module has one clearly defined responsibility.

## Modularity

Business logic, workbook operations, and user interface logic remain separated.

## Workbook Preservation
The processor shall modify only worksheet cells explicitly required by the approved Business Specification.

Developers shall never implement features that:

• overwrite unrelated worksheet data
• move worksheet columns
• delete worksheet columns
• modify source worksheet columns

Automatic processing shall only complete missing arrangement headers while preserving existing workbook content.

## Readability

Code should be easy to understand and maintain.

## Type Safety

Use Python type hints where practical.

## Documentation

Public classes and functions should include meaningful docstrings.

---

# 5. Feature Development Process

Each new feature is implemented incrementally.

For every feature:

1. Identify the affected business rule.
2. Review the Software Design Specification.
3. Review the Architecture.
4. 4. Update Business Specification, Software Design Specification, Architecture and Test Strategy before implementation whenever business rules or software behaviour change.
5. Implement one feature at a time.
6. Run automated tests.
7. Perform manual workbook validation.
8. Verify that existing workbook data remains unchanged.

9. Update the CHANGELOG.
10. Update the CHANGELOG.

---

# 6. Testing Workflow

Every implementation must be verified.

Required testing:

- Unit tests
- Integration tests (where applicable)
- Manual workbook testing
- Regression testing
Required testing

• Unit tests
• Integration tests
• Manual workbook testing
• Workbook preservation verification
• Regression testing

Manual workbook testing shall verify that:

• Date column is unchanged.
• 1st Prize column is unchanged.
• 2nd Prize column is unchanged.
• Existing arrangement headers remain unchanged.
• Existing arrangement data remains unchanged.
• Only missing arrangement headers are created.

The project currently uses:

- pytest
- openpyxl

No feature shall be merged while automated tests are failing.

---

# 7. Git Workflow

The preferred workflow is:

1. Implement one feature.
2. Run all tests.
3. Verify that workbook preservation requirements have been satisfied.
4. Commit changes with a descriptive commit message.
5. Update the CHANGELOG.
6. Push to the repository.

Avoid combining unrelated changes into a single commit.

---

# 8. Versioning

The project follows Semantic Versioning.

Format:

MAJOR.MINOR.PATCH

Examples:

- 1.0.0
- 1.1.0
- 1.1.1

Documentation versions should align with software releases whenever practical.

---

# 9. Project Structure

```text
SweetDreamzProcessor/

docs/
    Business_Specification.md
    Software_Design_Specification.md
    Architecture.md
    TestStrategy.md

    governance/
        Developer_Guide.md
        CHANGELOG.md
        ROADMAP.md

src/
tests/
resources/
```

---

# 10. Quality Checklist

Before completing any feature, verify:

- Business rules are satisfied.
- Architecture remains consistent.
- Existing worksheet structure is preserved.
Existing worksheet data is preserved.
Date, 1st Prize and 2nd Prize columns remain unchanged.
Existing arrangement headers remain unchanged.
Existing arrangement data remains unchanged.
Only missing arrangement headers have been created.
- New tests have been added where required.
- All pytest tests pass.
- Manual workbook validation is successful.
- Documentation has been updated if necessary.
- CHANGELOG has been updated.

---

# 11 Workbook Preservation Rules

The following worksheet elements are considered protected business data:

• Date header
• 1st Prize header
• 2nd Prize header
• Existing lottery data
• Existing arrangement headers
• Existing arrangement data

Developers shall not implement features that alter these elements unless explicitly required by the approved Business Specification.

Missing arrangement headers may be completed automatically, but existing worksheet data shall never be overwritten, moved, deleted or reformatted unnecessarily.

---

# 12. Future Development

Future enhancements should:

- Preserve the existing architecture.
- Maintain backward compatibility where possible.
- Follow the established development workflow.
- Avoid unnecessary complexity.
- Prioritize workbook safety and workbook preservation over performance.
- Future features shall never compromise the integrity of existing worksheet data.

---

# 13. Summary

This guide defines the standard development workflow for SweetDreamzProcessor.

All future development should follow the principles and processes described in this document to ensure consistent, maintainable, and high-quality software.