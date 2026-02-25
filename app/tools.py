#內部工具系統
import requests
from app.config import ROLE_SCOPES, TOOL_SCOPE_REQUIREMENT, TOOL_REGISTRY
from app.audit import log_tool_usage

def authorize_tool_call(role, tool_name):
    required = TOOL_SCOPE_REQUIREMENT.get(tool_name)

    if required not in ROLE_SCOPES.get(role, []):
        raise Exception("Unauthorized tool call")

def call_tool(role, tool_name, payload):
    authorize_tool_call(role, tool_name)

    url = TOOL_REGISTRY[tool_name]

    headers = {
        "X-User-Role": role
    }

    response = requests.post(url, json=payload, headers=headers)

    log_tool_usage(role, tool_name, payload)

    return response.json()
