# Candidate dataset assessment: OFR Financial Stress Index

**Status: preliminary research. The group pitch and dataset approval are pending.**

## Official source

- Publisher: U.S. Office of Financial Research (OFR).
- Dataset page: https://www.financialresearch.gov/financial-stress-index/
- Dataset: OFR Financial Stress Index (OFR FSI).

## Publisher-described characteristics

The OFR describes the FSI as a daily, market-based snapshot of stress in global
financial markets, constructed from 33 financial market variables. It reports
five indicator categories: credit, equity valuation, funding, safe assets and
volatility. It also reports contributions from the United States, other
advanced economies and emerging markets.

The publisher states that the index is calculated after each U.S. trading day
and that published data is current from two business days prior.

## Source and reuse checks still required

The official page provides a download control, but the exact direct file URL
and the applicable licence or reuse terms have not yet been verified. Do not
assume the dataset is public domain or cleared for commercial use. The actual
downloaded file, its metadata and any third-party restrictions must be checked.

## Proposed research framing. Not approved

A possible supervised classification problem is predicting whether a new
elevated-stress episode begins within a future horizon. A 20-trading-day
horizon was previously suggested as a hypothesis only.

Before implementation, the group must define and justify:
- the stress threshold;
- what counts as a new episode versus continuation of an existing episode;
- event start date and forecast horizon;
- treatment of overlapping future windows;
- prediction timestamp and information available by that timestamp;
- positive-class prevalence and number of independent events;
- chronological training, validation and test periods.

## Leakage and operational considerations

- Features at time *t* may use only information available by the prediction
  cut-off at *t*.
- The label may use future observations to define the outcome, but future
  values must never enter model features.
- The two-business-day publication lag must be represented if the system is
  intended to issue real-time warnings.
- All fitted preprocessing and feature selection must be learned from training
  data only.
- Evaluation must use chronological partitions and report their date ranges.

## Preliminary conclusion

The OFR FSI is conceptually relevant to MACROGUARD and has an official
publisher. Dataset approval, exact file schema, reuse terms and target
feasibility remain unresolved. Do not train a final model or claim a
commercially reusable dataset until these checks are complete.

## Sources

Office of Financial Research, “OFR Financial Stress Index,”
https://www.financialresearch.gov/financial-stress-index/ (accessed 2026-11-26).
