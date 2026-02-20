# utils/formatter.py

def get_progress_bar(current, limit):
    """Генерує візуальну шкалу прогресу"""
    if limit <= 0:
        return "<code>⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜</code> 0%"
    
    percent = min(int((current / limit) * 100), 100)
    filled_length = int(percent // 10)
    
    # Якщо ліміт перевищено, шкала стає червоною (опціонально)
    char = "🟥" if current >= limit else "🟩"
    bar = char * filled_length + "⬜" * (10 - filled_length)
    
    return f"<code>{bar}</code> {percent}%"