import asyncio
import logging

from bot.bot import bot, dp
from scheduler.scheduler import on_startup
from settings import CHAT_ID

logging.basicConfig(level=logging.INFO, format='[{asctime}] #{levelname:4} {name}:{lineno} - {message}', style='{')
logger = logging.getLogger(__name__)


async def main():
    await on_startup()
    await bot.send_message(chat_id=CHAT_ID, text='Я проснулся')
    await dp.start_polling(bot)


asyncio.run(main())
