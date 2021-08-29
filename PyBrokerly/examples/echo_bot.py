from brokerly import Bot


def handler(context, update):
    chat_id = update.message["chat_id"]
    text = update.message["content"]
    print(f"New message from chat {chat_id}: {text}")
    context.send_message(chat_id, text)


bot = Bot(
    token="pq-eQv9ECM7gyUXwKDFr", message_handler=handler, host="dashboard.brokerly.tk"
)
bot.start(interval=1)
