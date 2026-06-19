import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from scheduler.tasks import send_daily_message



async def on_startup():
    """
    Инициализация ежедневого задания при запуске бота
    :return:
    """
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

    # планирование на 10 утра
    # scheduler.add_job(
    #     send_daily_message,
    #     trigger="cron",
    #     hour=10,
    # )

    # тестовое планирование (раз в мин)
    scheduler.add_job(
        send_daily_message,
        trigger="interval",
        minutes=1,
        # seconds=3
    )

    scheduler.start()
