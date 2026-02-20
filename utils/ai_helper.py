from loader import client
from config import KEYWORDS_MAP
import re

async def ai_suggest_category(product_name):
    name_lower = product_name.lower().strip()
    
    # 1. СПОЧАТКУ СЛОВНИК (щоб не витрачати запити ШІ)
    for category, keywords in KEYWORDS_MAP.items():
        for word in keywords:
            if re.search(rf'\b{word}\b', name_lower):
                return category
            
    # 2. СПИСОК МОДЕЛЕЙ ДЛЯ РОТАЦІЇ
    # Порядок: Lite (вищий RPM) -> Flash (стандарт) -> 1.5 Flash (стабільна)
    models_to_try = [
        "gemini-2.5-flash-lite", 
        "gemini-2.5-flash", 
        "gemini-1.5-flash"
    ]
    
    categories_dict = {
        "Продукти": "Продукти 🛒", "Транспорт": "Транспорт 🚕", 
        "Відпочинок": "Відпочинок ☕", "Дім": "Дім/Побут 🏠", 
        "Здоров'я": "Здоров'я 💊", "Техніка": "Техніка 💻",
        "Одяг": "Одяг та взуття 👕", "Краса": "Краса та догляд ✨",
        "Донати": "Донати та подарунки 🎁", "Тварини": "Тварини 🐾"
    }
    
    prompt = (
        f"Визнач категорію для: '{product_name}'. "
        f"Обери ОДНУ назву ТІЛЬКИ з цього списку: {', '.join(categories_dict.keys())}. "
        "Відповідай тільки одним словом."
    )

    # 3. ЦИКЛ ПЕРЕКЛЮЧЕННЯ МОДЕЛЕЙ
    for model_name in models_to_try:
        try:
            response = client.models.generate_content(model=model_name, contents=prompt)
            category_name = response.text.strip()
            
            # Якщо ШІ повернув коректну категорію
            if category_name in categories_dict:
                return categories_dict[category_name]
            
        except Exception as e:
            # Якщо помилка ліміту (429), пробуємо наступну модель
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                print(f"⚠️ Модель {model_name} вичерпала ліміт. Перемикаюсь...")
                continue
            else:
                print(f"❌ Помилка моделі {model_name}: {e}")
                break # Якщо помилка не в лімітах, припиняємо

    # 4. РЕЗЕРВНИЙ ВАРІАНТ
    return "Інше 📁"