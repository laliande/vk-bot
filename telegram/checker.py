import telebot
from time import sleep
from app.comfig import telegram_token

users = {}


def create_bot(token):
    bot = telebot.TeleBot(token)
    return bot


def ban_users(user_id):
    n = users.get(user_id, 1)
    users.update({user_id: n})
    if n > 4:
        pass


def check_links(text, links=['http://', 'https://', '.ru', '.online', '.com']):
    for link in links:
        if link in text:
            return True
    return False


def handler_text_message(bot):
    @bot.message_handler(content_types=['text'])
    def handle_messages(message):
        if check_links:
            bot.reply_to(message, 'Warning! Links are forbidden')
            sleep(7)
            bot.delete_message(message.chat.id, message.message_id)
            bot.delete_message(message.chat.id, message.message_id + 1)
            ban_users(message.from_user.id)


bot = create_bot(telegram_token)
handler_text_message(bot)
bot.polling()
