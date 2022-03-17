import socket


def main():
    host = "127.0.0.1"
    port = 5000

    # create a new socket
    s = socket.socket()

    # create a tuple for host and port
    networkHost = (host, port)

    # tell socket to use host and port
    s.bind(networkHost)

    # start listening for requests
    s.listen()

    # accept incoming connection
    conn, addr = s.accept()
    print(f"Accepted connection from {addr}")

    # We're a server, we never stop listening
    # We're also not providing a graceful way to exit
    while True:
        # receive BINARY data
        data = conn.recv(1024)
        if not data:
            break

        # convert binary data to string
        data = data.decode()
        print(f"From connnection: {data}")

        data = data.upper()
        # return data to client
        print(f"Sending back to client: {data}")
        conn.send(data.encode())
    conn.close()


if __name__ == "__main__":
    main()
