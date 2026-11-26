# FINOSCOPE

**AI-Powered Financial Intelligence & Risk Investigation Platform**

FINOSCOPE is a modular financial-intelligence research platform designed to connect macro-financial stress monitoring, transaction-fraud analysis, financial-network intelligence, and explainable investigation workflows.

> **Project status:** Initial repository foundation. No production engine, validated model, institutional integration, or commercial deployment is claimed by this repository yet.

## Product vision

Build a responsible, explainable financial-risk environment that helps authorised analysts explore financial indicators, review model-generated risk signals, investigate evidence, and understand system limitations. Model outputs are decision-support signals, not proof of fraud, money laundering, or a financial crisis.

## Product modules

| Module | Purpose | Initial status |
|---|---|---|
| MACROGUARD | Systemic financial-stress monitoring and early-warning research | First development priority |
| FRAUDGUARD | Transaction-fraud risk analysis | Planned |
| AMLGUARD | Financial transaction-network analysis | Planned |
| INTELLIGENCE NEXUS | Evidence-backed links across engines | Planned |
| Investigation Workspace | Alert and case review | Planned |
| Model Intelligence | Experiment, model-version and monitoring capabilities | Planned |
| Data Governance | Provenance, quality, privacy and audit controls | Planned |
| Platform Administration | Users, organisations and permissions | Planned |

## First implementation: MACROGUARD

The first research direction is supervised prediction of whether an elevated financial-stress episode begins within a defined future horizon (initial proposal: 20 trading days).

This research question, event definition, target construction, dataset suitability, data licence and evaluation design must be verified and approved before results are claimed. The proposed OFR Financial Stress Index is a candidate source, not yet a confirmed approved dataset.

### CCS4340 academic scope

The initial university assignment is a focused MACROGUARD study. The team must follow the lecturer's requirements:

- One approved problem and dataset (additional enrichment only when justified and approved).
- Exactly three group members.
- Individual implementations of the ML pipeline stages.
- Three different model families, including one neural network.
- Baseline development, tuning, evaluation and comparison.
- At least one justified step beyond ordinary model fitting.
- Ethics and bias analysis.
- Genuine individual Git contributions.
- A working demonstration, report, presentation and individual viva.

The academic submission is **not** the entire FINOSCOPE product. FRAUDGUARD, AMLGUARD and the other platform modules remain part of the longer-term roadmap.

## Proposed technology direction

The initial stack is intentionally small:

- Frontend: Next.js, React and TypeScript
- Backend: Python and FastAPI
- Database: PostgreSQL
- Data and ML: Python, Pandas, NumPy and Scikit-learn
- Neural networks: PyTorch when the neural-network work begins
- Local development: Docker Compose
- Version control: Git and GitHub

Airflow, dbt, Neo4j, MLflow, cloud deployment and other infrastructure will be introduced when there is a demonstrated need. They are not prerequisites for the first working research prototype.

## Repository map

```text
apps/                 Web application and API
engines/              Domain-specific intelligence engines
data_platform/        Ingestion, validation and transformations
intelligence/         Cross-engine investigation capabilities
database/             Database schemas and migrations
mlops/                Experiment and model lifecycle tooling
infrastructure/       Local and future cloud infrastructure
docs/                 Architecture, research and decisions
data/                 Small samples only; never commit restricted data
notebooks/            Academic and exploratory notebooks
src/                  Academic/shared source entry points
models/               Model artefacts and metadata (no large binaries)
app/                  Academic demonstration entry point
reports/              Academic reports and evidence
screenshots/          Demonstration screenshots
videos/               Progress and demonstration video references
tests/                Automated tests
```

## Team and contribution model

The project is designed for three contributors. Final names, student IDs and branch names will be recorded after the group confirms them.

Each member must:
1. Own an individual model family for the academic assignment.
2. Implement and explain their own pipeline decisions.
3. Work on a dedicated branch and make genuine, meaningful commits.
4. Review the overall architecture and understand the complete project.
5. Contribute to evaluation, ethics, documentation and demonstration readiness.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/academic/CCS4340_COMPLIANCE.md](docs/academic/CCS4340_COMPLIANCE.md).

## Getting started

The initial repository foundation and setup instructions are being established. Application run commands will be added when the first runnable frontend and backend skeletons are committed.

Do not place credentials in the repository. Copy environment templates to local, ignored environment files when they are added. Do not commit personal, sensitive, licensed or restricted datasets.

## Research integrity and responsible use

- Cite datasets, papers, libraries, tutorials and reused code.
- Verify licence and redistribution conditions before downloading or sharing data.
- Keep train, validation and test data separated; prevent temporal and preprocessing leakage.
- Record actual experiments and results. Never fabricate metrics.
- Treat model outputs as uncertain decision support requiring human review.
- Document dataset bias, model limitations, false positives and false negatives.
- Do not use this research prototype to make autonomous accusations or adverse decisions about individuals.

## Roadmap

1. Establish project governance, academic approval and repository foundation.
2. Build and evaluate MACROGUARD.
3. Develop FRAUDGUARD after verifying suitable data rights.
4. Develop AMLGUARD after verifying graph-data reuse rights.
5. Build evidence-backed cross-engine investigation workflows.
6. Harden, test and deploy a clearly labelled research prototype.

## Disclaimer

FINOSCOPE is an independent research and software-development project. It is not a certified banking, regulatory, fraud-investigation or anti-money-laundering system. No claim of production readiness or regulatory approval is made.
