import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import asyncio
import aiohttp
import logging

load_dotenv()

# Настройка логирования
logging.basicConfig(
    filename='alerting.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
)


YANDEX_METRICA_TOKEN = os.getenv('YANDEX_METRICA_TOKEN')
YANDEX_METRICA_COUNTER_ID = os.getenv('YANDEX_METRICA_COUNTER_ID')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '465'))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER')
def send_email(subject, body):
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = EMAIL_RECEIVER
    try:
        with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as server:
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.sendmail(EMAIL_HOST_USER, [EMAIL_RECEIVER], msg.as_string())
        logging.info('Email sent')
    except Exception as e:
        logging.error(f'Email send error: {e}')


async def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=payload) as resp:
                if resp.status == 200:
                    logging.info('Telegram sent')
                else:
                    logging.error(f'Telegram send error: {resp.status}')
    except Exception as e:
        logging.error(f'Telegram send error: {e}')

API_URL = 'https://api-metrika.yandex.net/stat/v1/data'


def get_dates():
    today = datetime.now().date()
    start_date = today - timedelta(days=7)
    return start_date, today


def fetch_metric(metric_name):
    start_date, end_date = get_dates()
    headers = {'Authorization': f'OAuth {YANDEX_METRICA_TOKEN}'}
    params = {
        'ids': YANDEX_METRICA_COUNTER_ID,
        'metrics': metric_name,
        'date1': start_date.strftime('%Y-%m-%d'),
        'date2': end_date.strftime('%Y-%m-%d'),
        'dimensions': 'ym:s:date',
        'accuracy': 'full',
        'limit': 8
    }
    try:
        response = requests.get(API_URL, headers=headers, params=params, timeout=20)
        response.raise_for_status()
        data = response.json()
        logging.info(f"Fetched metric {metric_name} successfully.")
        return [row['metrics'][0] for row in data['data']]
    except Exception as e:
        logging.error(f"Error fetching metric {metric_name}: {e}")
        return [0]*8


def main():
    try:
        visits = fetch_metric('ym:s:visits')
        search_visits = fetch_metric('ym:s:searchVisits')
        bounce_rate = fetch_metric('ym:s:bounceRate')
        avg_duration = fetch_metric('ym:s:avgVisitDurationSeconds')

        alerts = []
        # Настройки алертов
        TRAFFIC_BOOST_FACTOR = 1.5
        BOUNCE_RATE_DELTA = 20  # процентных пунктов
        ENGAGEMENT_DROP_FACTOR = 0.7

        # Вспомогательные функции
        def avg7(values):
            return sum(values[:-1]) / 7 if len(values) == 8 else None

        # 1. Взрывной рост трафика (visits)
        avg_visits = avg7(visits)
        if avg_visits and visits[-1] > avg_visits * TRAFFIC_BOOST_FACTOR:
            alerts.append(f"Взрывной рост трафика: {visits[-1]:.0f} vs среднее {avg_visits:.0f}")

        # 2. Взрывной рост поискового трафика (searchVisits)
        avg_search = avg7(search_visits)
        if avg_search and search_visits[-1] > avg_search * TRAFFIC_BOOST_FACTOR:
            alerts.append(f"Взрывной рост поискового трафика: {search_visits[-1]:.0f} vs среднее {avg_search:.0f}")

        # 3. Рост показателя отказов (bounceRate)
        avg_bounce = avg7(bounce_rate)
        if avg_bounce and bounce_rate[-1] > avg_bounce + BOUNCE_RATE_DELTA:
            alerts.append(f"Рост отказов: {bounce_rate[-1]:.1f}% vs среднее {avg_bounce:.1f}%")

        # 4. Падение вовлеченности (avgVisitDurationSeconds)
        avg_dur = avg7(avg_duration)
        if avg_dur and avg_duration[-1] < avg_dur * ENGAGEMENT_DROP_FACTOR:
            alerts.append(f"Падение вовлеченности: {avg_duration[-1]:.0f} сек vs среднее {avg_dur:.0f} сек")

        if alerts:
            print("\nALERTS:")
            for alert in alerts:
                print(alert)
            # Формируем текст уведомления
            counter_url = f"https://metrika.yandex.ru/stat/traffic?counterId={YANDEX_METRICA_COUNTER_ID}"
            alert_text = '\n'.join(alerts) + f"\n\nСчетчик: {counter_url}"
            # Email
            send_email("Alert: аномалии в трафике", alert_text)
            # Telegram (асинхронно)
            asyncio.run(send_telegram(alert_text))
            logging.info(f"Alerts sent: {alerts}")
        else:
            print("Нет аномалий по метрикам.")
            logging.info("Нет аномалий по метрикам.")
    except Exception as e:
        logging.critical(f"Critical error in main: {e}")

if __name__ == '__main__':
    main()
