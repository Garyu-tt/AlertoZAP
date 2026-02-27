# AlertoZAP: Yandex Metrica Traffic Alerting

## Описание
Система автоматического мониторинга и алертинга по трафику сайта через Yandex Metrica API с уведомлениями в Telegram и Email.

## Установка
1. Клонируйте репозиторий
2. Создайте виртуальное окружение и активируйте его:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate    # Windows
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Скопируйте .env.example или .env в .env и заполните параметры.

## Конфигурация
- Все параметры (токены, SMTP, ID счетчика) задаются через файл .env.
- Пример файла: см. .env.example

## Логирование и обработка ошибок
- Все события и ошибки пишутся в файл `alerting.log` в корне проекта.
- Скрипт не падает при ошибках API или отправки уведомлений, ошибки логируются.

## Автоматизация запуска
- Для Linux: добавьте задачу в cron, например:
   ```bash
   0 */2 * * * cd /path/to/project && /path/to/venv/bin/python main.py
   ```
- Для Windows: используйте планировщик задач.

## Зависимости
- Все зависимости перечислены в requirements.txt (requests, python-dotenv, aiogram, aiohttp).

## Пример логов
```
2026-02-26 12:00:00 INFO Fetched metric ym:s:visits successfully.
2026-02-26 12:00:01 INFO Alerts sent: ['Взрывной рост трафика: 2000 vs среднее 1000']
```

## Запуск
- Для ручного запуска:
  ```bash
  python main.py
  ```
- Для автоматического запуска настройте cron (Linux) или планировщик задач (Windows).

## Добавление новых счетчиков
- Добавьте новый ID счетчика в .env и запустите скрипт с нужным конфигом.


## Изменение порогов чувствительности
- Пороговые значения задаются в main.py в секции "Настройки алертов".

## Контакты
- По всем вопросам писать в Telegram: [@mirbi_a](https://t.me/mirbi_a)


