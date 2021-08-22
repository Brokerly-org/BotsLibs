# BotsLibs
Library's for creating bots

#### Python bot example
```python
from brokerly import Bot


def handler(context, update):
    chat_id = update.message["chat_id"]
    text = update.message["content"]
    print(f'New message from chat {chat_id}: {text}')
    context.send_message(chat_id, text) # Return the text to the sender

bot = Bot(token='<Token>', message_handler=handler, host='127.0.0.1', port=80)
bot.start(interval=1) # Check for updates every one second
```