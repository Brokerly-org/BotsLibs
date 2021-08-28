from time import sleep
from threading import Thread

from websocket import create_connection


RETRY_CONNECTION_INTERVAL = 3


class Connection:
    def __init__(self, server_url: str, secure: bool, on_update, token):
        self.on_update = on_update

        self.schema = "wss://" if secure else "ws://"

        self.connection_url = f"{self.schema}{server_url}/bot_connect?token={token}"
        self.ws = self.retry_connection()
        self.listener = Thread(target=self.receiver)

        self._stop = False

    def start(self):
        self.listener.start()
        print(self.connection_url)

    def start_connection(self):
        return create_connection(self.connection_url)

    def retry_connection(self):
        while True:
            try:
                ws = self.start_connection()
                return ws
            except ConnectionError:
                sleep(RETRY_CONNECTION_INTERVAL)

    def send(self, data: str):
        try:
            self.ws.send(data)
        except Exception as EX:
            self.ws = self.retry_connection()

    def receiver(self):
        while not self._stop:
            try:
                data = self.ws.recv()
            except Exception:
                self.ws = self.retry_connection()
                continue
            else:
                if not self._stop:
                    self.on_update(data)

    def stop(self):
        print("Stopping...")
        self._stop = True
        self.ws.close()

