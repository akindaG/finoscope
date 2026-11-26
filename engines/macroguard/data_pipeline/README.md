# MACROGUARD data pipeline

This package provides dataset-agnostic building blocks while the group pitch
and final dataset are pending.

## Current status

- Dataset: OFR Financial Stress Index is a candidate, not approved.
- Problem: predicting the onset of an elevated-stress episode within a future
  horizon is a proposal, not an approved target.
- Individual model: Akinda's proposed model family is Logistic Regression.
- Approval: pending confirmation through the group project pitch.
- Licence/terms: check the publisher's actual terms before downloading,
  redistributing, or using the data in a commercial product.

## Modules

- `acquisition.py`: streams a caller-supplied URL to a raw file, computes
  SHA-256 and supports checksum verification. It deliberately has no assumed
  dataset URL.
- `validation.py`: checks required columns, timestamps, missing values and
  numeric value columns without silently changing source data.
- `splitting.py`: creates chronological train, validation and test partitions
  without shuffling.

## Example

After confirming the source's direct download URL and terms:

```bash
python -m engines.macroguard.data_pipeline.acquisition \
  --url "<publisher-approved-direct-download-url>" \
  --output "data/raw/source.csv"
```

Do not commit the raw dataset. Record the source URL, access date, terms,
checksum and schema in the dataset manifest.

## Important limitations

The chronological splitter uses row-count fractions. Inspect the resulting
date boundaries and adapt the split strategy if the data is irregular or
contains event clusters. Do not fit imputers, scalers, feature selectors or
resamplers before the training split.
