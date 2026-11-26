# CCS4340 Assignment Compliance Map

This is a planning aid, not lecturer approval.

## Assignment boundary
The CCS4340 submission is one approved problem and one approved dataset. The proposed first problem is supervised prediction of the onset of elevated financial stress within an initial 20-trading-day horizon. The event definition, label construction, OFR source suitability and licence must be verified and approved. Other FINOSCOPE engines are outside this initial academic problem.

## Three-member model-family plan
Provisional allocation:
- Member 1: Family A, Logistic Regression.
- Member 2: Family B, Random Forest.
- Member 3: Family C, Multilayer Perceptron (neural network).

Confirm member identities and allocation with the group. No two students may use the same model family.

## Individual mandatory workflow
Each student must show their own explainable implementation of:
1. Problem definition and data understanding.
2. Preprocessing, including missing values, outliers, duplicates, encoding/scaling where relevant, and leakage-safe splitting.
3. EDA with insights.
4. Feature engineering and at least one feature-selection method. PCA only where justified.
5. Assigned model, training, validation and tuning.
6. Appropriate evaluation, over/underfitting and error analysis.

Common utilities may be shared, but individual pipeline choices and work must remain visible in each student's branch and explainable in the viva.

## Group requirements
- Dataset selection and understanding, including source, licence, quality, bias and limitations.
- One justified step beyond ordinary model fitting.
- Comparison of all three models and justification of the selected model.
- Ethics, bias, privacy, risks and mitigation.
- A working final demonstration.
- Final report within 15 pages excluding cover, contents and appendices, using IEEE referencing.
- Progress video maximum 7 minutes, showing working code, pipeline outputs and each student's commits; slides are not accepted.
- Final presentation maximum 5 minutes, live demo 5 minutes, viva 5–7 minutes per member.

## Marking scheme
Progress evaluation: 30 assignment marks, scaled to 10% of module grade:
- Dataset selection and understanding: 10 group marks.
- Preprocessing and feature engineering: 15 individual marks.
- Baseline model development: 5 individual marks.

Final evaluation: 70 assignment marks, scaled to 20% of module grade:
- Tuned and neural-network model development: 10 individual.
- Evaluation and model comparison: 15 group.
- Ethics and bias: 10 group.
- Git contribution: 5 individual.
- Creativity / step beyond: 10 group.
- Final report: 5 group.
- Presentation: 5 individual.
- Viva: 10 individual.

A missing working demonstration caps the presentation mark at 2/5.

## Repository evidence
Required root folders: data/, notebooks/, src/, models/, app/, reports/, screenshots/, videos/, plus requirements.txt, README.md and .gitignore. Large datasets must not be committed; document source, licence and download instructions in data/README.md.

## Integrity and approvals
AI tools may assist, but each student is responsible for understanding, validating and explaining submitted work. Never fabricate results, manipulate commit history, publish personal/sensitive data or use unlicensed data. Record the lecturer's Approved / Revise / Reject response and exact LMS dates when received. Do not assume approval or invent calendar deadlines.
