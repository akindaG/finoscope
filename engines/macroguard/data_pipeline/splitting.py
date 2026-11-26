"""Chronological train/validation/test splitting for ordered observations."""
from __future__ import annotations

import pandas as pd


def chronological_split(
    frame: pd.DataFrame,
    *,
    timestamp_column: str,
    train_fraction: float = 0.70,
    validation_fraction: float = 0.15,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Split rows in chronological order without shuffling.

    Fractions apply to row counts, not calendar duration. For irregularly
    sampled data, inspect the resulting date boundaries before using them.
    """
    if timestamp_column not in frame.columns:
        raise ValueError(f"Missing timestamp column: {timestamp_column}")
    if not 0 < train_fraction < 1:
        raise ValueError("train_fraction must be between 0 and 1")
    if not 0 < validation_fraction < 1:
        raise ValueError("validation_fraction must be between 0 and 1")
    if train_fraction + validation_fraction >= 1:
        raise ValueError("train_fraction + validation_fraction must be less than 1")
    if frame.empty:
        raise ValueError("Cannot split an empty dataset")

    ordered = frame.copy()
    ordered[timestamp_column] = pd.to_datetime(
        ordered[timestamp_column], errors="raise"
    )
    if ordered[timestamp_column].duplicated().any():
        raise ValueError("Duplicate timestamps must be resolved before splitting")
    ordered = ordered.sort_values(timestamp_column, kind="stable").reset_index(drop=True)

    n_rows = len(ordered)
    train_end = int(n_rows * train_fraction)
    validation_end = train_end + int(n_rows * validation_fraction)
    if train_end < 1 or validation_end <= train_end or validation_end >= n_rows:
        raise ValueError("Dataset is too small for the requested split fractions")

    train = ordered.iloc[:train_end].copy()
    validation = ordered.iloc[train_end:validation_end].copy()
    test = ordered.iloc[validation_end:].copy()
    return train, validation, test
