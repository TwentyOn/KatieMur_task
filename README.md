# Тестовое задание

## Структура проекта
- bot - реализация Telegram-бота
- service - вспомогательные модули для работы программы
  - calculate - функции для расчетов
  - csv_writer - функции для записи в csv-файл
- api.py - модуль для запросов к API
- main.py - точка входа в программу 
- models.py - модуль для описания моделей данных
- settings.py - модуль для чтения переменных окружения

## Используемые компоненты
- Aiogram - реализация бота
- APScheduler  - библиотека для планирования выполнения кода

## Требования к переменным окружения
- ACCESS_TOKEN - токен доступа к APi
- BOT_TOKEN - токен доступа к Telegram-боту
- CHAT_ID - идентификатор Telegram-чата в который идет рассылка

## Запуск

1. клонирование репозитория
```commandline
git clone https://github.com/TwentyOn/test_tasks.git -b citadel_task && cd test_tasks
```

2. запуск docker-compose

```commandline
docker compose up -d
```

3. запуск тестов (опционально)
```commandline
docker compose exec -it backend python manage.py test
```
4. Остановка docker-compose
```commandline
docker compose stop
```

После запуска веб-приложения:
 - фронтенд доступен по адресу: http://localhost
 - OpenAPI-схема доступна по адресу:
http://localhost/api/schema/swagger-ui/

К БД можно подключиться с порта 5433, параметры подключения можно найти
в параметрах окружения
[docker-compose.yaml](docker-compose.yaml)

## Запуск настольного приложения
### Способ 1 (только windows)
1. Запустить исполняемый файл [main.exe](desktop%2Fbuild%2Fexe.win-amd64-3.14%2Fmain.exe)
по пути desktop/build/exe.win-amd64-3.14
### Способ 2
1. перейти в директорию приложения
```commandline
cd desktop
```
2. создать и активировать вирутальное окружение
```commandline
python -m venv .venv && .venv\Scripts\activate
```
3. установить зависимости
```commandline
pip install -r requirements.txt
```
4. запустить приложение
```commandline
python main.py
```
5. деативация окружения
```commandline
deativate
```

## Демонстрация работы

### Демо-видео
[2026-05-07 02-04-03.mp4](docs%2F2026-05-07%2002-04-03.mp4)

### Скриншоты

1. Окно регистрации

![register.png](docs%2Fregister.png)
2. Форма входа

![login.png](docs%2Flogin.png)


3. Интерфейс личного кабинета

![profile_view.png](docs%2Fprofile_view.png)


4. главное окно настольного приложения 

![desktop.png](docs%2Fdesktop.png)


5. окно подключения настольного приложения

![desktop_connected.png](docs%2Fdesktop_connected.png)

