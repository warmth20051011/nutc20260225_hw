import os

SECRET_KEY = "enterprise_secret"
ALGORITHM = "HS256"

LITELLM_URL = "http://localhost:4000/v1/chat/completions"

ROLE_SCOPES = {
    "admin": ["db", "python"],
    "engineer": ["python"],
    "analyst": ["db"]
}

TOOL_SCOPE_REQUIREMENT = {
    "db_query": "db",
    "run_python": "python"
}

TOOL_REGISTRY = {
    "db_query": "http://localhost:5001/query",
    "run_python": "http://localhost:5002/run"
}
