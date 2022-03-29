# For the client, the old blocking client is enough

import socket
import threading


def main():
    host = "127.0.0.1"
    port = 5000
    s = socket.socket()
    networkHost = (host, port)
    s.bind(networkHost)
    s.listen(10)

    while True:
        conn, addr = s.accept()
        # if there's no response in 5 seconds, close connection
        conn.settimeout(60)
        print(f"Connection from {addr}")
        # create a new thread
        #   target = function/method  that will be called when thread starts
        #   args = arguments to pass to target function
        thread = threading.Thread(target=listenToClient, args=(conn, addr))
        thread.start()


def listenToClient(conn, addr):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            data = data.decode()
            prompt = f"Received from {addr}: ".ljust(40)
            print(f"{prompt}{data}")
            data = data.upper()
            conn.send(data.encode())
        except socket.timeout as e:
            print(f"Socket from {addr} timed out")
            print(e)
            break
        except IOError as e:
            print(f"IOError from socket at {addr}")
            print(e)
            break
    conn.close()


if __name__ == '__main__':
    main()
