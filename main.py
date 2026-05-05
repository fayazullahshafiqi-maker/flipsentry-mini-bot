import time
import requests
from scraper import scrape_marketplace
import config


def send_telegram(message):
    url = f"https://api.telegram.org/bot{config.TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": config.CHAT_ID,
        "text": message
    })


def run():
    send_telegram("🚀 Flipsentry Mini Bot Started")

    while True:
        try:
            results = scrape_marketplace("rav4")

            for item in results:
                msg = f"{item['title']}\n{item['url']}"
                send_telegram(msg)

            time.sleep(60)

        except Exception as e:
            send_telegram(f"❌ Error: {str(e)}")
            time.sleep(30)


if __name__ == "__main__":
    run()
