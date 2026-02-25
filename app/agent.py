import json
from app.llm_client import call_llm
from app.tool_router import call_tool
from app.memory import save_message, load_history

def run_agent(user, message, session_id):
    history = load_history(session_id)

    messages = [{"role": "system", "content": "You are enterprise agent."}]
    for h in history:
        messages.append(json.loads(h))

    messages.append({"role": "user", "content": message})

    response = call_llm(messages)

    try:
        data = json.loads(response)

        if "tool" in data:
            result = call_tool(user["role"], data["tool"], data["input"])
            final_answer = str(result)
        else:
            final_answer = response

    except:
        final_answer = response

    save_message(session_id, json.dumps({"role": "user", "content": message}))
    save_message(session_id, json.dumps({"role": "assistant", "content": final_answer}))

    return final_answer
