import pandas as pd
import pytest

from engines.macroguard.data_pipeline.validation import (
    validate_time_series_frame,
)


def test_valid_time_series_frame_passes():
    frame = pd.DataFrame(
        {
            "date": ["2024-01-02", "2024-01-03", "2024-01-04"],
            "index_value": [0.1, 0.2, -0.1],
        }
    )

    report = validate_time_series_frame(
        frame,
        timestamp_column="date",
        value_columns=["index_value"],
    )

    assert report.is_valid
    assert report.row_count == 3
    assert report.duplicate_timestamp_count == 0
    assert report.missing_values["index_value"] == 0


def test_duplicate_timestamps_fail_validation():
    frame = pd.DataFrame(
        {
            "date": ["2024-01-02", "2024-01-02"],
            "index_value": [0.1, 0.2],
        }
    )

    report = validate_time_series_frame(
        frame,
        timestamp_column="date",
        value_columns=["index_value"],
    )

    assert not report.is_valid
    assert report.duplicate_timestamp_count == 1


def test_invalid_timestamp_is_reported():
    frame = pd.DataFrame({"date": ["not-a-date"], "index_value": [0.1]})

    report = validate_time_series_frame(
        frame,
        timestamp_column="date",
        value_columns=["index_value"],
    )

    assert not report.is_valid
    assert report.invalid_timestamp_count == 1


def test_missing_required_column_raises():
    frame = pd.DataFrame({"date": ["2024-01-02"]})

    with pytest.raises(ValueError, match="Missing required columns"):
        validate_time_series_frame(
            frame,
            timestamp_column="date",
            value_columns=["index_value"],
        )


def test_non_chronological_rows_fail_validation():
    frame = pd.DataFrame(
        {
            "date": ["2024-01-03", "2024-01-02"],
            "index_value": [0.2, 0.1],
        }
    )

    report = validate_time_series_frame(
        frame,
        timestamp_column="date",
        value_columns=["index_value"],
    )

    assert not report.is_valid
    assert not report.timestamps_monotonic
