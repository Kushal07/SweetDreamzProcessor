# Software Design Specification
## 1. Technical Architecture
- **Fresh Start Engine:** To combat Excel XML ghost rules, the system deletes all old sheets and recreates them.
- **Style Injection:** Uses Direct Styling (Fill/Font/Alignment) instead of Conditional Formatting to ensure zero performance degradation at scale.

## 2. Formatting Standards
- **Date:** Long Date format (dddd, dd mmmm yyyy).
- **Wrapping:** 1st Prize (2 lines), 2nd Prize (3 lines).
- **Grid:** Freeze Panes enabled at Column B and Row 2.
