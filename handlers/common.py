from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from handlers.keyboard import main_menu

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    user_name = message.from_user.first_name
    welcome_text = (
        f"Привіт, <b>{user_name}</b>! 👋\n\n"
        "Я твій інтелектуальний помічник для контролю фінансів. 💸\n"
        "Обери дію в меню нижче або просто введи свою першу витрату!"
    )
    await message.answer(welcome_text, reply_markup=main_menu(), parse_mode="HTML")

@router.message(Command("cancel"))
@router.message(F.text.casefold() == "скасувати")
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Дію скасовано. 🔙", reply_markup=main_menu())