# 🧾 Expense Calculator Bot (v2.0)

<p align="left">
  <a href="README.md">🇺🇸 English</a> | 
  <a href="README.uk.md">🇺🇦 Українська</a>
</p>

Професійний Telegram-бот для автоматизації обліку фінансів, побудований на базі штучного інтелекту. Бот допомагає контролювати витрати, стежити за підписками та аналізувати бюджет за допомогою потужного серверного рішення.

## 🚀 Що нового у версії 2.0 (Major Update)

* **🐘 Міграція на PostgreSQL**: Перехід з локального SQLite на масштабовану базу даних PostgreSQL, що забезпечує стабільну роботу на віддаленому сервері.
* **☁️ Cloud Deployment**: Бот розгорнутий на **Google Cloud Platform (Debian)** та працює 24/7 у фоновому режимі через `screen`.
* **🌑 Dark Mode Analytics**: Покращена візуалізація статистики з темною темою для комфортного перегляду звітів.
* **📂 Automated Migration System**: Реалізовано скрипти для безпечного перенесення даних та автоматичного створення резервних копій (Dumps).

## 🛠 Основні можливості

* **🤖 AI-Категоризація (Smart Fallback)**: Автоматичне визначення категорії витрат за допомогою Google Gemini API. Реалізовано каскадну ротацію моделей для обходу лімітів.
* **🔄 Менеджер підписок**: Автоматичне відстеження регулярних платежів з нагадуваннями через `APScheduler`.
* **📊 Візуальна аналітика**: Генерація кільцевих діаграм (Donut Charts) за допомогою `Matplotlib`.
* **🎯 Фінансове планування**: Встановлення місячних лімітів (10+ категорій) та цілей накопичення з динамічними прогрес-барами.
* **🌍 Мультивалютний моніторинг**: Актуальні курси валют через API Monobank.

## 💻 Технологічний стек

* **Language**: Python 3.13
* **Framework**: aiogram 3.13
* **Database**: **PostgreSQL** (SQLAlchemy + asyncpg)
* **Infrastructure**: Google Cloud (Linux/Debian)

## 📦 Встановлення та запуск

1. **Клонуйте репозиторій**:
   ```bash
   git clone [https://github.com/Neplyx/ExpenseCalculator_bot.git](https://github.com/Neplyx/ExpenseCalculator_bot.git)
2. Налаштуйте оточення:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
3. Запустіть бота:
   ```bash
   python main.py
👤 Автор
Maksym Kudyk — Python Developer & Automation Enthusiast.

Certified by SoftServe Academy.




   
