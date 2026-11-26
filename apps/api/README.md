# FINOSCOPE API

Initial FastAPI service foundation.

## Local setup

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn apps.api.app.main:app --reload --host 0.0.0.0 --port 8000
```

Open http://localhost:8000/health for the process health endpoint and http://localhost:8000/docs for OpenAPI documentation.

The initial API exposes health only. No prediction or financial-risk endpoint is implemented yet.
