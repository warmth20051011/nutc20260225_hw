#RBAC 權限控管
from app.tools import TOOL_REGISTRY

ROLE_PERMISSIONS = {
    "viewer": [],
    "analyst": ["db_query"],
    "engineer": ["db_query", "run_python"],
}

def get_tools_for_role(role: str):
    tool_names = ROLE_PERMISSIONS.get(role, [])
    return [TOOL_REGISTRY[name] for name in tool_names]
