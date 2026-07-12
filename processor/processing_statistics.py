from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class ProcessingStatistics:
    """Collects statistics for a processing run."""

    total_rows_scanned: int = 0
    rows_processed: int = 0

    empty_blocks_written: int = 0
    complete_blocks_skipped: int = 0
    partial_blocks_rewritten: int = 0

    errors: int = 0

    started_at: Optional[datetime] = field(default=None, init=False)
    finished_at: Optional[datetime] = field(default=None, init=False)

    def start(self) -> None:
        """Mark the beginning of processing."""
        self.started_at = datetime.now()
        self.finished_at = None

    def finish(self) -> None:
        """Mark the end of processing."""
        self.finished_at = datetime.now()

    @property
    def duration_seconds(self) -> float:
        """Return processing duration in seconds."""
        if self.started_at is None or self.finished_at is None:
            return 0.0

        return (self.finished_at - self.started_at).total_seconds()

    def summary(self) -> dict:
        """Return all collected statistics."""

        return {
            "total_rows_scanned": self.total_rows_scanned,
            "rows_processed": self.rows_processed,
            "empty_blocks_written": self.empty_blocks_written,
            "complete_blocks_skipped": self.complete_blocks_skipped,
            "partial_blocks_rewritten": self.partial_blocks_rewritten,
            "errors": self.errors,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "duration_seconds": self.duration_seconds,
        }