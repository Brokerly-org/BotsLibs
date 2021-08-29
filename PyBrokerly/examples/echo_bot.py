from brokerly import Bot


def handler(context, update):
    chat_id = update.message["chat_id"]
    text = update.message["content"]
    print(f"New message from chat {chat_id}: {text}")
    context.send_message(chat_id, text)

<<<<<<< HEAD
bot = Bot(token='UlbP7EQ2rl47SmY7nH3A', message_handler=handler, host='localhost', port=9981, secure=False)
=======

bot = Bot(
    token="pq-eQv9ECM7gyUXwKDFr", message_handler=handler, host="dashboard.brokerly.tk"
)
>>>>>>> 4d39976a40f78bf0d86d7cc444dd6d5a28331c64
bot.start(interval=1)
