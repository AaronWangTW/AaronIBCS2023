import socket

def main():
    host = "172.16.12.41"
    port = 5005

    s = socket.socket(type=socket.SOCK_DGRAM)
    networkHost = (host, port)

    data = socket.gethostbyname_ex("brentmparker.com")
    print(data)
    serverHost = data[2][0]

    server = (serverHost, 9001) # 5004 originally

    s.bind(networkHost)
    print("Client started...")
    
    msg = input(">>>")
    while msg != 'q':
        s.sendto(msg.encode(),server)
        data, addr = s.recvfrom(1024)
        data = data.decode()
        print(f"Received from server {addr}: {data}")
        msg = input(">>>")
    s.close()

if __name__ == "__main__":
    main()