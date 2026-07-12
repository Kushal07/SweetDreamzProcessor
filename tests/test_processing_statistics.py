import time

from processor.processing_statistics import ProcessingStatistics


def test_default_values():
    stats = ProcessingStatistics()

    assert stats.total_rows_scanned == 0
    assert stats.rows_processed == 0
    assert stats.empty_blocks_written == 0
    assert stats.complete_blocks_skipped == 0
    assert stats.partial_blocks_rewritten == 0
    assert stats.errors == 0


def test_start_finish():
    stats = ProcessingStatistics()

    stats.start()
    time.sleep(0.01)
    stats.finish()

    assert stats.started_at is not None
    assert stats.finished_at is not None
    assert stats.duration_seconds > 0


def test_summary():
    stats = ProcessingStatistics()

    stats.total_rows_scanned = 25
    stats.rows_processed = 10
    stats.empty_blocks_written = 8
    stats.complete_blocks_skipped = 6
    stats.partial_blocks_rewritten = 2
    stats.errors = 1

    summary = stats.summary()

    assert summary["total_rows_scanned"] == 25
    assert summary["rows_processed"] == 10
    assert summary["empty_blocks_written"] == 8
    assert summary["complete_blocks_skipped"] == 6
    assert summary["partial_blocks_rewritten"] == 2
    assert summary["errors"] == 1