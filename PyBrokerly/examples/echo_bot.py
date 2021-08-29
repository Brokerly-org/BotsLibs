from brokerly import Bot


def handler(context, update):
    chat_id = update.message["chat_id"]
    text = update.message["content"]
    print(f'New message from chat {chat_id}: {text}')
    context.send_message(chat_id, text)

bot = Bot(token='UlbP7EQ2rl47SmY7nH3A', message_handler=handler, host='localhost', port=9981, secure=False)
bot.start(interval=1)
