import requests
import time
from concurrent.futures.thread import ThreadPoolExecutor


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
    def __init__(self, token: str, message_handler, host: str, port: int = None, workers: int = 4) -> None:
        self.token = token
        if port is not None:
            self.server_url = f'http://{host}:{port}'
        else:
            self.server_url = f'http://{host}'
        self.handler = message_handler
        self.executor = ThreadPoolExecutor(max_workers=workers)
            
    def get_updates(self):
        response = requests.get(f"{self.server_url}/bot/pull", params={"token": self.token})
        return response.json()

    def send_message(self, chat_id, message) -> None:
        requests.post(
            f"{self.server_url}/bot/push",
            params={"token": self.token, "chat_id": chat_id, "message": message}
        )

    def start(self, interval=5):
        while True:
            update = self.get_updates()
            chats = update['chats']
            for chat in chats:
                for message in chat['messages']:
                    message = Message({"message": message})
                    self.executor.submit(self.handler, (message,))
            time.sleep(interval)            
