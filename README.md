# 🧾 Expense Calculator Bot (v2.0)

<p align="left">
  <a href="README.md">🇺🇸 English</a> | 
  <a href="README.uk.md">🇺🇦 Українська</a>
</p>

A professional, AI-powered Telegram bot designed to automate personal finance tracking. The bot helps you monitor expenses, manage subscriptions, and analyze your budget using a powerful backend solution.

## 🚀 What's New in Version 2.0 (Major Update)

* **🐘 Migration to PostgreSQL**: Transitioned from local SQLite to a scalable PostgreSQL database, ensuring stable performance on a remote server.
* **☁️ Cloud Deployment**: Deployed on **Google Cloud Platform (Debian)**, running 24/7 in the background via `screen`.
* **🌑 Dark Mode Analytics**: Enhanced statistical visualization with a dark theme for comfortable report viewing.
* **📂 Automated Migration System**: Implemented scripts for secure data transfer and automated backups (Dumps).

## 🛠 Key Features

* **🤖 AI-Categorization (Smart Fallback)**: Automatic expense categorization powered by the Google Gemini API, featuring cascading model rotation to bypass rate limits.
* **🔄 Subscription Manager**: Automatic tracking of recurring payments with reminders handled by `APScheduler`.
* **📊 Visual Analytics**: Generation of donut charts for budget insights using `Matplotlib`.
* **🎯 Financial Planning**: Monthly limit configuration (10+ categories) and savings goals with dynamic progress bars.
* **🌍 Multi-Currency Monitoring**: Up-to-date exchange rates integrated via the Monobank API.

## 💻 Tech Stack

* **Language**: Python 3.13
* **Framework**: aiogram 3.13
* **Database**: **PostgreSQL** (SQLAlchemy + asyncpg)
* **Infrastructure**: Google Cloud (Linux/Debian)

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/Neplyx/ExpenseCalculator_bot.git](https://github.com/Neplyx/ExpenseCalculator_bot.git)

2. **Set up the environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
3. **Run the bot**:
   ```bash
   python main.py

## 👤 Author
* **Maksym Kudyk** — Python Developer & Automation Enthusiast.

* **Education**: Certified by SoftServe Academy.

