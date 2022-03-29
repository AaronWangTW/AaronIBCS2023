import socket


def main():
    host = "127.0.0.1"
    port = 5004

    s = socket.socket(type=socket.SOCK_DGRAM)
    networkHost = (host, port)
    s.bind(networkHost)
    print("Server started...")

    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode()
        if data == 'q':
            break
        print(f"Received from {addr}: {data}")
        data = data.upper()
        print(f"Sending ot {addr}: {data}")
        s.sendto(data.encode(), addr)
    s.close()


if __name__ == "__main__":
    main()
