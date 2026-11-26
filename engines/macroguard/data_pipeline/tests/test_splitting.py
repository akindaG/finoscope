import pandas as pd
import pytest

from engines.macroguard.data_pipeline.splitting import chronological_split


def test_split_is_chronological_and_disjoint():
    frame = pd.DataFrame({
        "date": pd.date_range("2020-01-01", periods=20, freq="D"),
        "x": range(20),
    }).sample(frac=1, random_state=7)

    train, validation, test = chronological_split(frame, timestamp_column="date")

    assert len(train) == 14
    assert len(validation) == 3
    assert len(test) == 3
    assert train.date.max() < validation.date.min()
    assert validation.date.max() < test.date.min()


def test_duplicate_dates_are_rejected():
    frame = pd.DataFrame({"date": ["2020-01-01", "2020-01-01"], "x": [1, 2]})
    with pytest.raises(ValueError, match="Duplicate timestamps"):
        chronological_split(frame, timestamp_column="date")


def test_empty_dataset_is_rejected():
    frame = pd.DataFrame({"date": [], "x": []})
    with pytest.raises(ValueError, match="empty"):
        chronological_split(frame, timestamp_column="date")
