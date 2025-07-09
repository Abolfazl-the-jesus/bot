import asyncio
from aiogram import Bot, dispatcher
from bot.config import get_setting
from bot.handlers import start

async def main():
    setting = get_setting()
    bot = Bot(token=setting.bot_token)
    dp = dispatcher()

    dp.include_router(start.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())    