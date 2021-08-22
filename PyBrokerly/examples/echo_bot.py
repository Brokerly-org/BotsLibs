from brokerly import Bot


def handler(context, update):
    chat_id = update.message["chat_id"]
    text = update.message["content"]
    print(f'New message from chat {chat_id}: {text}')
    context.send_message(chat_id, text)

bot = Bot(token='nblNTu1zMWTQrte0p5KJ', message_handler=handler, host='127.0.0.1', port=80)
bot.start(interval=1)
