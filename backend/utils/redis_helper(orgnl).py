import redis
import json

# Redis client
r = redis.Redis(host='localhost', port=6379, db=0)

def get_context(user_id: str) -> dict:
    data = r.get(user_id)
    if data:
        return json.loads(data)
    return {"chat_history": [], "symptoms": []}

def save_context(user_id: str, context: dict):
    r.set(user_id, json.dumps(context), ex=3600)  # 1 soat davomida saqlash

def clear_context(user_id: str):
    r.delete(user_id)
