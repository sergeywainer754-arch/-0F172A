import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command

import os
TOKEN = os.environ.get("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Главное меню
def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🚀 Открыть VPN",
                web_app=WebAppInfo(
                    url="https://sleep-wallet-experimental-chairs.trycloudflare.com/"
    )
)
        ],
        [
            InlineKeyboardButton(text="📊 Статус", callback_data="status")
        ],
        [
            InlineKeyboardButton(text="⚙ Настройки", callback_data="settings")
        ]
    ])

# Кнопка назад
def back_button():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅ Назад", callback_data="back")]
    ])

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🚀 <b>VPN Панель</b>\n\nВыберите действие:",
        reply_markup=main_menu(),
        parse_mode="HTML"
    )

@dp.callback_query()
async def callbacks(callback):
    if callback.data == "keys":
        await callback.message.edit_text(
            "📲 <b>Ваши ключи</b>\n\n🔑 #AID-41452\n🔴 Статус: Закончился",
            reply_markup=back_button(),
            parse_mode="HTML"
        )

    elif callback.data == "status":
        await callback.message.edit_text(
            "🟢 <b>VPN активен</b>\n\n📍 Сервер: Германия\n📡 IP: 123.123.123.123",
            reply_markup=back_button(),
            parse_mode="HTML"
        )

    elif callback.data == "settings":
        await callback.message.edit_text(
            "⚙ <b>Настройки</b>\n\nТут скоро будет магия 😎",
            reply_markup=back_button(),
            parse_mode="HTML"
        )

    elif callback.data == "back":
        await callback.message.edit_text(
            "🚀 <b>VPN Панель</b>\n\nВыберите действие:",
            reply_markup=main_menu(),
            parse_mode="HTML"
        )

    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":

    asyncio.run(main())
