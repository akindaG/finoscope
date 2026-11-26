# MACROGUARD data pipeline

This package starts with dataset-agnostic validation. It deliberately does not
assume a final source schema, target definition, event threshold or forecast
horizon.

## Current status

- Dataset: OFR Financial Stress Index is a candidate only.
- Problem: predict the onset of an elevated stress episode within a future
  horizon is a proposal only.
- Approval: pending confirmation through the group project pitch.
- Licence/terms: must be verified from the publisher before redistribution or
  commercial use is considered.

## Validation contract

`validate_time_series_frame` checks required columns, parseable timestamps,
duplicate timestamps, chronological ordering, missing values and numeric value
columns. It reports issues without sorting, imputing or modifying the input.

Do not add source-specific transformations until the dataset schema and
approved prediction target are documented.
