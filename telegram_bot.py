import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import config
import io

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

token = config.BOT_TOKEN


def read_file(file: str):
    file = io.open(file, 'r', encoding="utf8")
    file_contents = file.read()
    file.close()
    return file_contents


def start(update: Update, _: CallbackContext) -> None:
    message = read_file('strings/start_message.txt')
    update.message.reply_text(message)


def help_command(update: Update, _: CallbackContext) -> None:
    message = read_file('strings/help_message.txt')
    update.message.reply_text(message)


def echo(update: Update, _: CallbackContext) -> None:
    update.message.reply_text(update.message.text)


def main() -> None:
    updater = Updater(token)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
