from brokerly import Bot

def handler(context, update):
    chat_id = update.chat
    message = update.text
    print(f'New message from chat {chat_id}: {message}')
    context.send_message(chat_id, message)

bot = Bot('127.0.0.1', 80, 'nblNTu1zMWTQrte0p5KJ', handler)
bot.start(interval = 1)