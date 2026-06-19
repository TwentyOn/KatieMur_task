import logging
from models import Order

logger = logging.getLogger(__name__)

def get_orders_rating(orders: list[Order]) -> list[tuple[int, int]]:
    """
    Функция для подсчета рейтинга заказов
    :param orders:
    :return:
    """
    try:
        result = {}

        articles = [d.article for d in orders]
        for art in articles:
            result[articles.count(art)] = art

        result = sorted(result.items(), key=lambda x: x[0], reverse=True)

        return result

    except Exception as err:
        logger.error(exc_info=True, msg='Ошибка при подсчете рейтинга заказов')
        raise err
