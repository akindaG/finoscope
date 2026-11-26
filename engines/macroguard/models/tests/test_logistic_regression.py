import pandas as pd
import pytest

from engines.macroguard.models.logistic_regression import (
    evaluate_binary_classifier,
    train_logistic_regression,
)


def sample_data():
    return pd.DataFrame({
        "feature_a": [-2.0, -1.5, -1.0, -0.5, 0.5, 1.0, 1.5, 2.0],
        "feature_b": [0.2, 0.4, 0.1, 0.3, 0.7, 0.8, 0.6, 0.9],
        "target": [0, 0, 0, 0, 1, 1, 1, 1],
    })


def test_logistic_regression_trains_and_evaluates():
    data = sample_data()
    model = train_logistic_regression(
        data.iloc[:6],
        feature_columns=["feature_a", "feature_b"],
        target_column="target",
    )
    result = evaluate_binary_classifier(
        model,
        data.iloc[6:],
        feature_columns=["feature_a", "feature_b"],
        target_column="target",
    )

    assert 0 <= result.accuracy <= 1
    assert result.confusion_matrix
    assert result.roc_auc is not None


def test_training_rejects_non_binary_target():
    data = sample_data()
    data["target"] = [0, 1, 2, 0, 1, 2, 0, 1]

    with pytest.raises(ValueError, match="exactly two"):
        train_logistic_regression(
            data,
            feature_columns=["feature_a"],
            target_column="target",
        )


def test_training_rejects_missing_feature_values():
    data = sample_data()
    data.loc[0, "feature_a"] = None

    with pytest.raises(ValueError, match="missing values"):
        train_logistic_regression(
            data,
            feature_columns=["feature_a", "feature_b"],
            target_column="target",
        )
