# app/agent.py
import json
from app.llm_client import call_llm
from app.tools import call_tool
from app.memory import save_message, load_history

def run_agent(user, message, session_id):

    history = load_history(session_id)

    messages = [{"role": "system", "content": "You are enterprise agent."}]
    messages.extend(history)
    messages.append({"role": "user", "content": message})

    print("要送給 LLM 的 messages:", messages)  # debug 用

    response = call_llm(messages)

    try:
        data = json.loads(response)
        if "tool" in data:
            result = call_tool(user["role"], data["tool"], data["input"])
            final_answer = str(result)
        else:
            final_answer = response
    except Exception:
        # 如果不是 JSON，就直接當文字回傳
        final_answer = response

    save_message(session_id, "user", message)
    save_message(session_id, "assistant", final_answer)

    return final_answer
