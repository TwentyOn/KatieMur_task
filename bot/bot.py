from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from settings import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command('help'))
async def test(message: Message):
    print(message.chat.id)
    await message.answer('da')
