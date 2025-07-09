from aiogram import Router
from aiogram.types import message

router = Router()

@Router.message(command=["start"])
async def start(message: message):
    await message.answer("بات ران شد هوراااا")
    