import os
from ltm.utils.reply_chatid import reply_chatid


def main() -> None:
    if not os.environ.get("TELEGRAM_BOT_TOKEN"):
        raise ValueError("Добавте переменную TELEGRAM_BOT_TOKEN в окружение")

    reply_chatid()


if __name__ == "__main__":
    main()
