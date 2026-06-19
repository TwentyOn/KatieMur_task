import random
from datetime import date, timedelta

from models import Order

from faker import Faker


def generate_data() -> list[Order]:
    result = [None] * 1000

    articles = [random.randrange(100000000, 1000000000) for _ in range(100)]

    fake = Faker('ru_RU')
    for i in range(1000):
        order = Order(
            order_date=(date.today() - timedelta(days=1)).strftime("%d-%m-%Y"),
            article=random.choice(articles),
            product_name=fake.text(),
            status=random.choice(['Оформлен', 'В пути', 'Доставлен']),
            price=random.uniform(500, 100000),
        )
        result[i] = order

    return result
