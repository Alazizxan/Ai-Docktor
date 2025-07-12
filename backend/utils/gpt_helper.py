import g4f
import concurrent.futures

def gpt_request(prompt_text, timeout=5) -> str:
    """
    GPT so‘rovini timeout va retry bilan yuboradi.
    """
    def call_gpt():
        return g4f.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt_text}]
        )

    for attempt in range(3):  # Retry mexanizmi
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(call_gpt)
            try:
                return future.result(timeout=timeout)
            except concurrent.futures.TimeoutError:
                print(f"[RETRY] GPT so‘rovida timeout (urinish: {attempt + 1})")
            except Exception as e:
                print(f"[ERROR] GPT so‘rovida xatolik: {e}")
    return None
