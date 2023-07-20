import requests as r
from datetime import datetime
import random


def send_signal(data: dict[str, int]):
    r.post("http://app01:8080/api/sens-messages/", json=data)


def main():
    while True:
        data = {"datetime": datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S"),
                "payload": random.randint(0, 10) - 5}
        send_signal(data)


if __name__ == "__main__":
    main()
