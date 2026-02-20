from aiogram import Bot, Dispatcher
from google import genai
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import BOT_TOKEN, GEMINI_KEY

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
client = genai.Client(api_key=GEMINI_KEY)
scheduler = AsyncIOScheduler(timezone="Europe/Kyiv")