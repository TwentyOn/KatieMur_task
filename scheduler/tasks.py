import logging
from datetime import datetime, timedelta

from api import get_orders
from bot.bot import bot
from service.calculate import get_orders_rating
from service.csv_writer import write_orders
from settings import ACCESS_TOKEN, CHAT_ID

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
            text = (f"Доброе утро! Топ 3 артикула по заказам на {date}:\n"
                    f"1. {rating[0][1]} ({rating[0][0]})\n"
                    f"2. {rating[1][1]} ({rating[1][0]})\n"
                    f"3. {rating[2][1]} ({rating[2][0]})")

        await bot.send_message(chat_id=CHAT_ID, text=text)

    except Exception as err:
        logger.error(exc_info=True, msg='Ошибка при отправке сообщения')
        await bot.send_message(chat_id=CHAT_ID, text='Непредвиденная ошибка формирования ежедневной статистики :(')
