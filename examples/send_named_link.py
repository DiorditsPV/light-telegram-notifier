import os
from dotenv import load_dotenv
from ltm.notifier import TelegramNotifier
from ltm.utils import make_link


def main() -> None:
    load_dotenv()

    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in .env")
        return

    notifier = TelegramNotifier(token)
    link = make_link("https://google.com", "Google")
    notifier.send_message(chat_id, f"Check this: {link}")


if __name__ == "__main__":
    main()
