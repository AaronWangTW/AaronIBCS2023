import socket


def main():
    host = "172.16.12.35"
    port = 5000

    s = socket.socket()
    networkHost = (host, port)

    # connect to server
    s.connect(networkHost)

    # get input from user
    msg = input(">>>")
    # while we do not want to quit
    while msg != 'q':
        try:
            if len(msg) > 0:
                # send message to server
                s.send(msg.encode())

                # listen for echo response
                data = s.recv(1024)
                print(f"received from server: {data.decode()}")
                msg = input(">>>")

        except IOError as e:
            print(f"Server closed connection: {e}")
            break
    s.close()


if __name__ == "__main__":
    main()
