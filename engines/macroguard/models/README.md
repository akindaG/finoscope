# Akinda's MACROGUARD Logistic Regression

**Status: baseline implementation scaffold. Not trained on the project dataset.**

The implementation provides:
- A scikit-learn Pipeline with StandardScaler and regularised Logistic Regression.
- Configurable L1/L2 penalty, inverse regularisation strength and class weighting.
- Training on an explicitly supplied training partition.
- Binary classification evaluation with accuracy, balanced accuracy, precision,
  recall, F1, ROC-AUC, average precision (PR-AUC) and confusion matrix.

## Important controls

- Fit the scaler only on training data. The Pipeline enforces this when fitted.
- Do not use the test partition for hyperparameter or threshold selection.
- Choose the positive class explicitly in the final project target specification.
  This scaffold currently treats the second sorted class as positive.
- Do not interpret the current module as evidence of model performance. No
  project dataset has been approved or loaded yet.
- This implementation assumes numeric features and complete feature values.
  Any imputation must be added as a training-fitted pipeline step after the
  final schema is known.

## Planned experiments after target approval

1. L2 baseline with C=1.0.
2. L1 regularisation and a justified C search.
3. Class-weight comparison if class imbalance is confirmed.
4. Validation-only threshold analysis if probability-based decisions are part
   of the approved problem.
5. Calibration and error analysis, where sample size supports them.
