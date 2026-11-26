# Candidate dataset assessment: OFR Financial Stress Index

**Status: preliminary research. Not an approved project dataset.**

## Official source

- Publisher: U.S. Office of Financial Research (OFR).
- Dataset page: https://www.financialresearch.gov/financial-stress-index/
- Dataset: OFR Financial Stress Index (OFR FSI).

## Facts confirmed from the publisher's page

The OFR describes the FSI as a daily, market-based snapshot of stress in global
financial markets. It is constructed from 33 financial market variables,
including yield spreads, valuation measures and interest rates.

The publisher describes five indicator categories:
- Credit
- Equity valuation
- Funding
- Safe assets
- Volatility

The index also reports contributions across three regions:
- United States
- Other advanced economies
- Emerging markets

The publisher states that the index is calculated after each U.S. trading day
and that the published data is current from two business days prior.

## Suitability questions still open

1. What exact downloadable file and historical coverage will the group use?
2. What licence or terms govern downloading, storing, modifying and
   redistributing the data? The page reviewed does not establish a specific
   open-data licence. Do not assume one.
3. Does the downloadable file contain the 33 underlying variables, category
   contributions, regional contributions, or only aggregate index values?
4. Are historical observations revised? If so, can the project preserve a
   reproducible source snapshot?
5. Is the proposed target label meaningful and sufficiently represented?
6. Does the target represent a future event that can be defined without
   looking ahead in model features?
7. Is this problem and dataset available for the group's project, and has the
   lecturer approved it through the project pitch?

## Proposed research framing. Pending approval

A possible supervised classification problem is predicting whether an
elevated-stress episode begins within a future horizon. The previously discussed
20-trading-day horizon is only a hypothesis.

Before implementation, the group must define:
- the stress threshold and why it is defensible;
- what constitutes a new episode versus continuation of an existing episode;
- the event start date;
- the forecast horizon;
- how overlapping event windows are labelled;
- the prediction timestamp and information available at that timestamp;
- the positive-class prevalence and whether there are enough independent
  episodes for chronological evaluation.

## Leakage controls

- Features for date *t* may use only information available by the prediction
  cut-off on date *t*.
- A label may use future observations only to determine the future outcome.
- All fitted preprocessing, feature selection, scaling and resampling must be
  learned from training data only.
- Train, validation and test periods must be chronological.
- The two-business-day publication lag must be considered if the intended use
  is a real-time warning system.

## Preliminary conclusion

The OFR FSI is conceptually relevant to MACROGUARD and has a clear official
publisher. It is not yet cleared for the assignment because the exact file
structure, licence/terms, target feasibility and lecturer approval remain
unverified.

## Source

Office of Financial Research, “OFR Financial Stress Index,”
https://www.financialresearch.gov/financial-stress-index/ (accessed 2026-11-26).
