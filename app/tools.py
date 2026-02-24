from dataclasses import dataclass
from typing import Callable
import requests

#內部工具系統
@dataclass
class Tool:
    name: str
    description: str
    endpoint: str


def call_mcp(endpoint: str, payload: str):
    response = requests.post(endpoint, json={"input": payload}, timeout=10)
    return response.json()


TOOL_REGISTRY = {
    "db_query": Tool(
        name="db_query",
        description="Query enterprise database",
        endpoint="http://db-mcp:5001/run"  
    ),
    "run_python": Tool(
        name="run_python",
        description="Execute secure Python code",
        endpoint="http://python-mcp:5002/run" 
    ),
}
