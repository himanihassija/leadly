# Getting started (owner: Tech team)

1. Install dependencies: `uv venv && uv pip install fastapi uvicorn`
2. Start the server: `uv run uvicorn main:app --port 8000`
3. Check it works: `curl http://localhost:8000/health`
   Expected: `{"status":"ok"}`
