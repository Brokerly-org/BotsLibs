import requests
import time

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
    def __init__(self, host, port, token, message_handler) -> None:
        self.token = token
        self.server_url = f'http://{host}:{port}'
        self.handler = message_handler
            
    def get_updates(self):
        response = requests.get(f"{self.server_url}/bot/pull", params={"token": self.token})
        return response.json()

    def send_message(self, chat_id, message) -> None:
        requests.post(
            f"{self.server_url}/bot/push",
            params={"token": self.token, "chat_id": chat_id, "message": message}
        )

    def start(self, interval = 5):
        while True:
            update = self.get_updates()
            chats = update['chats']
            for chat in chats:
                for message in chat['messages']:
                    message = Message({ "text": message})
                    message['chat'] = chat['chat']
                    
                    self.handler(self, message)
            time.sleep(interval)            