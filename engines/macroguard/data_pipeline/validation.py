"""Dataset-agnostic validation helpers for MACROGUARD time-series inputs.

These checks intentionally do not encode an assumed OFR schema. Bind the
required columns only after the group confirms its dataset and target.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import pandas as pd


@dataclass(frozen=True)
class TimeSeriesValidationReport:
    row_count: int
    column_count: int
    missing_values: dict[str, int]
    duplicate_timestamp_count: int
    invalid_timestamp_count: int
    timestamps_monotonic: bool
    non_numeric_value_columns: tuple[str, ...]

    @property
    def is_valid(self) -> bool:
        return (
            self.row_count > 0
            and self.invalid_timestamp_count == 0
            and self.duplicate_timestamp_count == 0
            and self.timestamps_monotonic
            and not self.non_numeric_value_columns
        )


def validate_time_series_frame(
    frame: pd.DataFrame,
    *,
    timestamp_column: str,
    value_columns: Sequence[str],
) -> TimeSeriesValidationReport:
    """Inspect a time-series frame without silently changing its contents.

    Missing values are reported rather than automatically imputed. Timestamp
    sorting, imputation and outlier treatment belong in explicit pipeline steps.
    """
    required = [timestamp_column, *value_columns]
    missing_columns = [column for column in required if column not in frame.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    parsed_timestamps = pd.to_datetime(frame[timestamp_column], errors="coerce")
    invalid_timestamp_count = int(parsed_timestamps.isna().sum())

    valid_timestamps = parsed_timestamps.dropna()
    duplicate_timestamp_count = int(valid_timestamps.duplicated().sum())
    timestamps_monotonic = bool(valid_timestamps.is_monotonic_increasing)

    missing_values = {
        column: int(frame[column].isna().sum())
        for column in required
    }
    non_numeric_value_columns = tuple(
        column
        for column in value_columns
        if not pd.api.types.is_numeric_dtype(frame[column])
    )

    return TimeSeriesValidationReport(
        row_count=len(frame),
        column_count=len(frame.columns),
        missing_values=missing_values,
        duplicate_timestamp_count=duplicate_timestamp_count,
        invalid_timestamp_count=invalid_timestamp_count,
        timestamps_monotonic=timestamps_monotonic,
        non_numeric_value_columns=non_numeric_value_columns,
    )
