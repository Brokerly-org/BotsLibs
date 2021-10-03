from brokerly import Bot


def handler(context, update):
    chat_id = update.message["chat_id"]
    text = update.message["content"]
    print(f"New message from chat {chat_id}: {text}")
    context.send_message(chat_id, text)


def callback_handler(context, callback_data):
    print(callback_data)


bot = Bot(
    token="nn1FpnNpLcUqEufHn-xJ", message_handler=handler, callback_handler=callback_handler, host="yakov.gq",
)
bot.start()
