# System Architecture
## 1. Layered Pattern
- **UI Layer:** Tkinter-based event loop.
- **Application Layer:** Orchestrates the 'Nuclear Wipe' and 'Data Reflow'.
- **Persistence Layer:** Openpyxl-driven direct cell manipulation.

## 2. The 'Rebirth' Algorithm
Every sheet is duplicated into a memory buffer, the old sheet is destroyed, and a fresh grid is built to ensure total removal of hidden Excel rule caches.
