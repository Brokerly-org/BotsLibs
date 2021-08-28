from datetime import datetime, timedelta

from brokerly import Bot
from brokerly.widgets import Slider, Button, Checkbox, Switch, DatePicker, TimePicker


def handler(context, update):
    chat_id = update.message["chat_id"]
    text = update.message["content"]
    print(f'New message from chat {chat_id}: {text}')
    if text == "slider":
        context.send_message(chat_id, "Home temperature °C", widget=Slider(initial_value=22.0, min=16.0, max=30.0, divisions=14))
    elif text == "button":
        context.send_message(chat_id, "Get door camera image", widget=Button(text="Take Picture", data="door_camera"))
    elif text == "checkbox":
        context.send_message(chat_id, "Send me suggestions by email", widget=Checkbox(initial_status=False))
    elif text == "switch":
        context.send_message(chat_id, "Send alert when home door is opened", widget=Switch(initial_status=False))
    elif text == "date picker":
        context.send_message(
            chat_id,
            "When to send the package?",
            widget=DatePicker(
                initial=datetime.now(),
                first=datetime.now() - timedelta(days=1),
                last=datetime.now() + timedelta(days=14),
                format="MM-dd",
            )
        )
    elif text == "time picker":
        context.send_message(
            chat_id,
            "When to backup server?",
            widget=TimePicker(
                initial_hour=12,
                initial_minute=0,
            )
        )
    else:
        help_text = """
        Commands:
        1. button
        2. slider
        3. checkbox
        4. switch
        5. date picker
        6. time picker
        """
        context.send_message(chat_id, help_text)

bot = Bot(token='pq-eQv9ECM7gyUXwKDFr', message_handler=handler, host='dashboard.brokerly.tk')
bot.start(interval=1)
