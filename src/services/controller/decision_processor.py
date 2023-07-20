import redis
import json
from datetime import datetime
from threading import Thread
import socket


redis_app = redis.Redis(host="red01", port=6379)


def make_decision(conn):
    sub = redis_app.pubsub()
    sub.subscribe('messages')

    last_time = datetime.now()
    decision = 0
    for message in sub.listen():
        if message is None:
            continue
        data = message["data"]
        if not isinstance(data, int):
            d = json.loads(data.decode().replace("'", '"'))
            decision += d["payload"]
            diff = datetime.now() - last_time
            if diff.seconds * 1000000 + diff.microseconds > 5000000:
                last_time = datetime.now()
                last_call_reply = last_time.strftime("%Y-%m-%dT%H:%M:%S")
                reply = {"datetime": last_call_reply, "status": "up" if decision >= 0 else "down"}
                conn.sendall(str(reply).encode())
                redis_app.set(str(last_time.timestamp()), "up" if decision >= 0 else "down")
                decision = 0
                print(reply)


def socket_conn():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 7001))
    s.listen()
    while True:
        try:
            print("Connecting")
            conn, address = s.accept()
            print(address)
            thread1 = Thread(target=make_decision,
                           args=[conn])
            thread1.start()
        except KeyboardInterrupt:
            try:
                conn.close()
            except:
                pass
            finally:
                s.close()


if __name__ == "__main__":
    socket_conn()