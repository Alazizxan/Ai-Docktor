# RAMda vaqtincha kontekst saqlash uchun oddiy dict
_in_memory_store = {}

def get_context(user_id: str) -> dict:
    """
    RAM ichidan foydalanuvchi kontekstini olish.
    Agar topilmasa, yangi kontekst qaytaradi.
    """
    return _in_memory_store.get(user_id, {"chat_history": [], "symptoms": []})

def save_context(user_id: str, context: dict):
    """
    RAM ichida foydalanuvchi kontekstini yangilash.
    """
    _in_memory_store[user_id] = context

def clear_context(user_id: str):
    """
    RAM ichidan foydalanuvchi kontekstini o‘chirish.
    """
    if user_id in _in_memory_store:
        del _in_memory_store[user_id]
