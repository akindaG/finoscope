"""Akinda's baseline Logistic Regression implementation for MACROGUARD.

The target column and final feature set must be agreed after dataset/pitch
approval. This module deliberately accepts them as parameters.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    balanced_accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


@dataclass(frozen=True)
class BinaryClassificationResults:
    accuracy: float
    balanced_accuracy: float
    precision: float
    recall: float
    f1: float
    roc_auc: float | None
    pr_auc: float | None
    confusion_matrix: list[list[int]]


def build_logistic_regression(
    *,
    c: float = 1.0,
    penalty: str = "l2",
    class_weight: str | None = None,
    max_iter: int = 2000,
    random_state: int = 42,
) -> Pipeline:
    """Create a scaler + regularised logistic regression pipeline."""
    if c <= 0:
        raise ValueError("c must be greater than zero")
    if penalty not in {"l1", "l2"}:
        raise ValueError("penalty must be 'l1' or 'l2'")

    return Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "classifier",
                LogisticRegression(
                    C=c,
                    penalty=penalty,
                    solver="liblinear",
                    class_weight=class_weight,
                    max_iter=max_iter,
                    random_state=random_state,
                ),
            ),
        ]
    )


def train_logistic_regression(
    train: pd.DataFrame,
    *,
    feature_columns: Sequence[str],
    target_column: str,
    c: float = 1.0,
    penalty: str = "l2",
    class_weight: str | None = None,
) -> Pipeline:
    """Fit the model on training rows only."""
    if not feature_columns:
        raise ValueError("At least one feature column is required")
    required = [*feature_columns, target_column]
    missing = [column for column in required if column not in train.columns]
    if missing:
        raise ValueError(f"Missing training columns: {missing}")

    x_train = train.loc[:, feature_columns]
    y_train = train.loc[:, target_column]
    if y_train.nunique(dropna=True) != 2:
        raise ValueError("Logistic Regression baseline requires exactly two target classes")
    if y_train.isna().any():
        raise ValueError("Target contains missing values")
    if x_train.isna().any().any():
        raise ValueError(
            "Features contain missing values. Add an explicit imputation step "
            "inside the training pipeline before fitting."
        )
    if not all(pd.api.types.is_numeric_dtype(x_train[col]) for col in feature_columns):
        raise ValueError("All selected features must be numeric")

    model = build_logistic_regression(
        c=c, penalty=penalty, class_weight=class_weight
    )
    model.fit(x_train, y_train)
    return model


def evaluate_binary_classifier(
    model: Pipeline,
    evaluation_data: pd.DataFrame,
    *,
    feature_columns: Sequence[str],
    target_column: str,
) -> BinaryClassificationResults:
    """Evaluate a fitted binary classifier on a separate held-out partition."""
    required = [*feature_columns, target_column]
    missing = [column for column in required if column not in evaluation_data.columns]
    if missing:
        raise ValueError(f"Missing evaluation columns: {missing}")

    x_eval = evaluation_data.loc[:, feature_columns]
    y_true = evaluation_data.loc[:, target_column]
    if y_true.isna().any():
        raise ValueError("Evaluation target contains missing values")
    if x_eval.isna().any().any():
        raise ValueError("Evaluation features contain missing values")

    y_pred = model.predict(x_eval)
    labels = list(model.named_steps["classifier"].classes_)
    if len(labels) != 2:
        raise ValueError("Evaluation requires a fitted binary classifier")
    positive_label = labels[1]
    y_score = model.predict_proba(x_eval)[:, 1]

    roc_auc = None
    pr_auc = None
    if y_true.nunique() == 2:
        y_binary = (y_true == positive_label).astype(int)
        roc_auc = float(roc_auc_score(y_binary, y_score))
        pr_auc = float(average_precision_score(y_binary, y_score))

    matrix = confusion_matrix(y_true, y_pred, labels=labels).tolist()
    return BinaryClassificationResults(
        accuracy=float(accuracy_score(y_true, y_pred)),
        balanced_accuracy=float(balanced_accuracy_score(y_true, y_pred)),
        precision=float(precision_score(y_true, y_pred, pos_label=positive_label, zero_division=0)),
        recall=float(recall_score(y_true, y_pred, pos_label=positive_label, zero_division=0)),
        f1=float(f1_score(y_true, y_pred, pos_label=positive_label, zero_division=0)),
        roc_auc=roc_auc,
        pr_auc=pr_auc,
        confusion_matrix=matrix,
    )
