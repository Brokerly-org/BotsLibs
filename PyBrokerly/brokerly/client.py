import requests
import time
import json as json_lib
from concurrent.futures.thread import ThreadPoolExecutor


from .widgets import Widget
from .connection_handler import Connection


class Message:
    def __init__(self, json) -> None:
        self.data = json

    def __getattr__(self, name: str):
        return self.data[name]

    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __getitem__(self, key):
        return self.data[key]


class Bot:
    def __init__(self, token: str, message_handler, host: str, port: int = None, workers: int = 4, secure: bool = True) -> None:
        self.token = token
        self.schema = "https://" if secure else "http://"
        if port is not None:
            self.server_url = f'{self.schema}{host}:{port}'
        else:
            self.server_url = f'{self.schema}{host}'
        self.connection = Connection(self.server_url[self.server_url.find("//")+2:], secure, self.pares_update, self.token)
        self.connection.start()
        self.handler = message_handler
        self.executor = ThreadPoolExecutor(max_workers=workers)

    def send_message(self, chat_id, message, widget: Widget = None) -> None:
        empty_widget = {"type": "non", "args": {}}

        response = requests.post(
            f"{self.server_url}/bot/push",
            params={"token": self.token, "chat_id": chat_id},
            json={"text": message, "widget": widget.to_widget() if widget is not None else empty_widget},
        )

    def _run_handler(self, updates):
        try:
            self.handler(self, updates)
        except Exception as EX:
            print(EX)

    def _get_updates(self):
        response = requests.get(f"{self.server_url}/bot/pull", params={"token": self.token})
        return response.json()

    def pares_update(self, update):
        updates = json_lib.loads(update)
        for update in updates:
            self.execute_update(update)

    def execute_update(self, update):
        for message in update['messages']:
            message = Message({"message": message})
            self.executor.submit(self._run_handler, message)

    def start(self, interval=5):
        self.idle()

    def idle(self):
        while True:
            try:
                time.sleep(0.5)
            except KeyboardInterrupt:
                break

