#RBAC 權限控管
from app.tools import TOOL_REGISTRY

ROLE_SCOPES = {
    "viewer": [],
    "analyst": ["db:read"],
    "engineer": ["db:read", "python:exec"]
}

TOOL_SCOPE_REQUIREMENT = {
    "db_query": "db:read",
    "run_python": "python:exec"
}
