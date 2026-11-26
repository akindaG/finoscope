from fastapi import FastAPI

app = FastAPI(
    title="FINOSCOPE API",
    description="Initial API foundation for the FINOSCOPE research platform.",
    version="0.1.0",
)


@app.get("/health", tags=["operations"])
def health_check() -> dict[str, str]:
    """Return process health; this does not assert database or model readiness."""
    return {"status": "ok", "service": "finoscope-api"}
