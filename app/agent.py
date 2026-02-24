import json
import re
from app.permissions import get_tools_for_role
from app.llm_client import call_llm
from app.audit import log_tool_usage
from app.memory import get_history, save_history
from app.tools import call_mcp


class EnterpriseAgent:

    def __init__(self, role: str, session_id: str):
        self.role = role
        self.session_id = session_id
        self.tools = get_tools_for_role(role)
        self.allowed_tools = {tool.name: tool for tool in self.tools}

    def run(self, user_input: str):

        history = get_history(self.session_id)
        history.append({"role": "user", "content": user_input})

        tool_descriptions = "\n".join(
            [f"- {tool.name}: {tool.description}" for tool in self.tools]
        )

        system_prompt = f"""
You are an enterprise AI Agent.
You can only use these tools:

{tool_descriptions}

If using tool, return JSON:
{{
 "action": "tool_name",
 "action_input": "input"
}}
"""

        messages = [{"role": "system", "content": system_prompt}] + history

        response = call_llm(messages)

        history.append({"role": "assistant", "content": response})
        save_history(self.session_id, history)

        json_match = re.search(r"\{.*\}", response, re.DOTALL)

        if not json_match:
            return {"response": response}

        parsed = json.loads(json_match.group())
        action = parsed.get("action")
        action_input = parsed.get("action_input")

        if action not in self.allowed_tools:
            return {"error": "Unauthorized tool access"}

        tool = self.allowed_tools[action]
        result = call_mcp(tool.endpoint, action_input)

        log_tool_usage(self.role, action, action_input)

        return {
            "tool_used": action,
            "tool_result": result
        }
