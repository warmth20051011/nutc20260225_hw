#RBAC 權限控管
from app.config import ROLE_SCOPES, TOOL_SCOPE_REQUIREMENT

ROLE_SCOPES = {
    "viewer": [],
    "analyst": ["db:read"],
    "engineer": ["db:read", "python:exec"]
}

TOOL_SCOPE_REQUIREMENT = {
    "db_query": "db:read",
    "run_python": "python:exec"
}
