# main.py
import asyncio
import logging
from loader import dp, bot, scheduler
import database as db
from handlers import common, expenses, stats, goals, limits
from utils.scheduler_tasks import setup_scheduler

async def main():
    logging.basicConfig(level=logging.INFO)
    db.init_db()
    
    # 1. Специфічні команди
    dp.include_router(common.router)
    
    # 2. Модулі з кнопками (мають пріоритет)
    dp.include_router(stats.router)
    dp.include_router(goals.router)
    dp.include_router(limits.router)
    
    # 3. Обробка витрат - ЗАВЖДИ В КІНЦІ
    dp.include_router(expenses.router)
    
    setup_scheduler()
    scheduler.start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())