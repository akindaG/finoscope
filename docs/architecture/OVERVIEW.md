# FINOSCOPE Architecture Overview

## Architectural style
Start as a modular monolith: one web application, one FastAPI application and one PostgreSQL database, with logically separated domain engines. Avoid premature microservices.

## Logical layers
1. Experience: Next.js interface and analyst workflows.
2. API: FastAPI routing, validation and access-control boundary.
3. Domain engines: MACROGUARD first; FRAUDGUARD and AMLGUARD later.
4. Shared intelligence: evidence-backed alert linking and investigations, only when records can legitimately be linked.
5. Data platform: source ingestion, provenance, validation, transformation and feature generation.
6. Persistence: PostgreSQL initially; graph storage only when justified.
7. ML lifecycle: reproducible experiments, model metadata, evaluation and monitoring.

## Initial MACROGUARD flow
Approved source data -> raw source retention and metadata -> validation -> processed time series -> leakage-safe feature generation -> chronological train/validation/test partitions -> independently developed models -> evaluation and comparison -> selected model exposed through an API -> analyst-facing demonstration.

## Data and prediction integrity
- Preserve observation dates and source provenance.
- Define prediction timestamp and feature availability cutoff.
- Construct labels using future outcomes only for the target, never as input features.
- Fit preprocessing and feature selection on training data only.
- Use time-aware validation; do not randomly shuffle a time series without justification.
- Store model version, prediction timestamp, target horizon and evidence references with predictions.

## Integration boundary
Engines retain domain-specific feature and prediction semantics. A shared alert envelope may reference an engine prediction, but the platform must not infer relationships merely because unrelated datasets contain similar values.

## Current status
This describes intended architecture. The initial repository documentation, API and database foundation are being established; no trained engine is claimed.
