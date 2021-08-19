from brokerly import Bot

def handler(context, update):
    chat_id = update.message["chat_id"]
    text = update.message["content"]
    print(f'New message from chat {chat_id}: {text}')
    context.send_message(chat_id, text)

bot = Bot('127.0.0.1', 80, 'nblNTu1zMWTQrte0p5KJ', handler)
bot.start(interval = 1)
