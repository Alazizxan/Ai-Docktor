from utils.gpt_helper import gpt_request
from utils.redis_helper import get_context, save_context, clear_context

doctor_prompt = (
    "Siz professional shifokor chatbotisiz. "
    "Foydalanuvchidan uning alomatlari va simptomlarini so‘rab, birma-bir yozib boring. "
    "Agar foydalanuvchi 'Tugadi' desa, barcha simptomlarga asoslanib yakuniy javob yozing."
)

def process_user_message(user_id: str, user_input: str) -> dict:
    # Chat kontekstini olish
    context = get_context(user_id)

    # Chat tarixiga yangi xabar qo‘shish
    context["chat_history"].append({"role": "user", "content": user_input})

    # ✅ Agar 'Tugadi' bo‘lsa, oddiy yakuniy xabar berish (ML modelsiz)
    if user_input.lower() in ["tugadi", "tamom", "bo‘ldi", "yo‘q"]:
        if context["symptoms"]:
            # ML model o‘rniga GPT dan yakuniy javob olish
            symptom_list = ", ".join(context["symptoms"])
            diagnosis_prompt = (
                f"Foydalanuvchi quyidagi simptomlarni aytdi: {symptom_list}. "
                "Shu simptomlarga asoslanib, 3 ta ehtimoliy tashxis va foydali maslahat yozing."
            )
            diagnosis = gpt_request(diagnosis_prompt)
            clear_context(user_id)
            return {"reply": diagnosis or "❌ Tashxis chiqarishda xatolik yuz berdi."}
        else:
            return {"reply": "❌ Simptomlar topilmadi. Iltimos, avval alomatlarni yuboring."}

    # ✅ GPT bilan suhbatlashish
    full_prompt = f"{doctor_prompt}\nFoydalanuvchi: {user_input}"
    gpt_reply = gpt_request(full_prompt)
    context["chat_history"].append({"role": "assistant", "content": gpt_reply})

    # ✅ Simptomlarni ajratish
    symptoms_prompt = f"Quyidagi matndan faqat simptomlarni vergul bilan ajratib yozing:\n\n{user_input}"
    symptoms_text = gpt_request(symptoms_prompt)
    if symptoms_text:
        symptoms = [s.strip() for s in symptoms_text.split(",") if s.strip()]
        context["symptoms"].extend(symptoms)
        context["symptoms"] = list(set(context["symptoms"]))  # Unikal simptomlar
        print(f"[DEBUG] {user_id} uchun yig‘ilgan simptomlar: {context['symptoms']}")

    # Chat kontekstini saqlash
    save_context(user_id, context)

    return {"reply": gpt_reply or "❌ Javob olishda xatolik."}
