import socket

BUFF_SIZE = 2048


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.connect_ex(("dpr01", 7001))
    print("Connected")
    while True:
        request = s.recv(BUFF_SIZE).decode()
        if len(request) != 0:
            print(request)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Shutting down")