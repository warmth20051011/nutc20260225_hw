#長對話記憶
import redis
import json
conversation_memory = {}

def save_message(session_id, role, content):
    if session_id not in conversation_memory:
        conversation_memory[session_id] = []

    conversation_memory[session_id].append({
        "role": role,
        "content": content
    })

def load_history(session_id):
    return conversation_memory.get(session_id, [])
