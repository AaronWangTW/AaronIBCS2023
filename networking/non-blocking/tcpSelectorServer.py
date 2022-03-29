import socket
import selectors
from multiprocessing.pool import ThreadPool
from threading import Thread

TIMEOUT = 60
MAX_CONNECTIONS = 10

pool = ThreadPool(5)

def main():
    host = "127.0.0.1"
    port = 5000
    networkHost = (host, port)

    s = socket.socket()
    s.bind(networkHost)
    s.listen(MAX_CONNECTIONS)

    # create a selector, this is the object that listens for new events
    selector = selectors.DefaultSelector()

    # Register some object that can create events
    # Parameters are:
    #   the object that originates the events
    #   the type of event to listen for
    #   the function/method to call when that event is detected
    selector.register(s, selectors.EVENT_READ, accept)

    print("Server started...")

    

    # Create a loop that handles events
    while True:
        for key, mask in selector.select():  # select the latest event, mask is just meta data, doesn't matter
            handler = key.data
            # key is a dict that contains info such as callback func, object of event, etc. key.data is the callback function,
            # which is accept() here
            handler(selector, key.fileobj)


def accept(selector: selectors.BaseSelector, s: socket.socket):
    conn, addr = s.accept()
    conn.setblocking(False)
    conn.settimeout(TIMEOUT)
    print(f"Connection from {addr}")

    selector.register(conn, selectors.EVENT_READ, startThread)


def startThread(selector, conn):
    pool.apply_async(readFromSocket, (selector, conn))


def readFromSocket(selector, conn):
    try:
            data = conn.recv(1024)
            if not data:
                unregister(selector,conn)
            data = data.decode()
            prompt = f"Received: ".ljust(10)
            print(f"{prompt}{data}")
            data = data.upper()
            conn.send(data.encode())
    except socket.timeout as e:
            print(f"Socket timed out")
            print(e)
            unregister(selector,conn)
    except IOError as e:
            print(f"IOError from socket")
            print(e)
            unregister(selector,conn)

def unregister(selector:selectors.BaseSelector, fileObj):
    try:
        selector.unregister(fileObj)
    except KeyError as e:
        print(f"KeyError from connection")
        print(e)
    except ValueError as e:
        print(f"ValueError from connection")
        print(e)
    finally:
        fileObj.close()

if __name__ == "__main__":
    main()