#長對話記憶
import redis
import json
from app.config import REDIS_HOST, REDIS_PORT

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


def get_history(session_id: str):
    data = r.get(session_id)
    return json.loads(data) if data else []


def save_history(session_id: str, history: list):
    r.setex(session_id, 3600, json.dumps(history))  # 1 hour TTL
