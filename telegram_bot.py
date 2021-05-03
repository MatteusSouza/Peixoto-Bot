import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater, 
    CommandHandler, 
    MessageHandler, 
    Filters, 
    ConversationHandler, 
    CallbackContext
)

from config import BOT_TOKEN
from strings.read_file import read_file
import fortnite_tracker

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

PLATFORM, REGION, USERNAME = range(3)

choices = {'username': '', 'platform': '', 'region': ''}

def start(update: Update, _: CallbackContext) -> None:
    message = read_file('strings/start_message.txt')
    update.message.reply_text(message)


def help_command(update: Update, _: CallbackContext) -> None:
    message = read_file('strings/help_message.txt')
    update.message.reply_text(message)


def search_power_ranking(update, _: CallbackContext)-> int:
    reply_keyboard = [
        ['Console', 'Mobile',],
        ['Pc'],
    ]

    update.message.reply_text(
        'What platform?',
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )

    return PLATFORM


def platform(update: Update, _: CallbackContext) -> int:
    choices['platform'] = update.message.text
    reply_keyboard = [
        ["NA East", "NA West", "Europe"],
        ["Oceania", "Brazil", "Asia", "Middle East"],
    ]

    update.message.reply_text(
        'What region?',
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return REGION


def region(update: Update, _: CallbackContext) -> int:
    user_choice = ["NA East", "NA West", "Europe", "Oceania", "Brazil", "Asia", "Middle East"].index(update.message.text)
    initials = ["NAE", "NAW", "EU", "OCE", "BR", "ASIA", "ME"]
    choices['region'] = initials[user_choice]
    update.message.reply_text(
        'What username?',
        reply_markup = ReplyKeyboardRemove(),
    )
    return USERNAME

def username(update: Update, _: CallbackContext) -> int:
    choices['username'] = update.message.text
    power_ranking = fortnite_tracker.getPower_ranking(
        choices['username'],
        choices['platform'],
        choices['region']
    )
    if power_ranking['status_code'] != 200:
        update.message.reply_text('Power Ranking não encontrado. \nTalvez o jogador não possua power ranking.')
    else:
        pr = power_ranking['response_info']
        update.message.reply_text(
            f"{pr['name']}\n"
            f"Power Ranking: {pr['points']}\n"
            f"Cash Winnings: ${pr['cashPrize']}\n"
            f"Events played: {pr['events']}\n"
            f"Percentile: {pr['percentile']}%"
            )
    return ConversationHandler.END

def cancel(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    updater = Updater(BOT_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('pr', search_power_ranking)],
        states={
            PLATFORM: [
                MessageHandler(
                    Filters.regex('^(Console|Mobile|Pc)$'), platform
                )
            ],
            REGION: [
                MessageHandler(
                Filters.regex('^(NA East|NA West|Europe|Oceania|Brazil|Asia|Middle East)$'), region
                )
            ],
            USERNAME: [
                MessageHandler(Filters.text & ~Filters.command, username)
            ],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
