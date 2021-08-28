from brokerly import Bot
from brokerly.widgets import Slider


def handler(context, update):
    chat_id = update.message["chat_id"]
    text = update.message["content"]
    print(f'New message from chat {chat_id}: {text}')
    context.send_message(chat_id, "Home temperature", widget=Slider(initial_value=22, min=16, max=30, divisions=14))

bot = Bot(token='pq-eQv9ECM7gyUXwKDFr', message_handler=handler, host='dashboard.brokerly.tk')
bot.start(interval=1)
