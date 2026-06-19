import asyncio
import logging
from datetime import datetime, timedelta

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from bot.bot import bot, dp
from settings import ACCESS_TOKEN, CHAT_ID
from api import get_orders
from service.csv_writer import write_orders
from service.calculate import get_orders_rating

logging.basicConfig(level=logging.INFO, format='[{asctime}] #{levelname:4} {name}:{lineno} - {message}', style='{')
logger = logging.getLogger(__name__)


async def send_daily_message():
    """
    callback-функция для инициализации процесса запроса данных и отправки ежедневоного сообщения
    :return:
    """
    try:
        orders = get_orders(ACCESS_TOKEN)
        write_orders(orders)

        rating = get_orders_rating(orders)
        date = (datetime.today() - timedelta(days=1)).strftime('%d.%m.%Y')

        if not rating:
            text = f'Заказов на {date} зафиксировано не было :('
        else:
            text = (f"Привет! Топ 3 артикула по заказам на {date}:\n"
                    f"1. {rating[0][1]} ({rating[0][0]})\n"
                    f"2. {rating[1][1]} ({rating[1][0]})\n"
                    f"3. {rating[2][1]} ({rating[2][0]})")

        await bot.send_message(chat_id=CHAT_ID, text=text)

    except Exception as err:
        logger.error(exc_info=True)
        await bot.send_message(chat_id=CHAT_ID, text='Непредвиденная ошибка формирования ежедневной статистики :(')


async def on_startup():
    """
    Инициализация ежедневого задания при запуске бота
    :return:
    """
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

    scheduler.add_job(
        send_daily_message,
        trigger="interval",
        seconds=5,
    )
    scheduler.start()


async def main():
    await on_startup()
    await bot.send_message(chat_id=CHAT_ID, text='Я проснулся')
    await dp.start_polling(bot)


asyncio.run(main())
