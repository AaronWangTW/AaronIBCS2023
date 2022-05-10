import asyncio
import json

ENCODING = "utf8"
USERNAME = 'username'
MESSAGE = 'message'


class ChatClientProtocol(asyncio.Protocol):

    def __init__(self, on_conn_lost: asyncio.Future, loop) -> None:
        # We need the loop later so we can execute some extra code on the loop
        self._loop = loop

        # Future that we will use to inform main that we have quit
        self.on_conn_lost = on_conn_lost
        self.is_connected = False
        self._transport = None
        self.on_data_received: callable = None

    def connection_made(self, transport: asyncio.BaseTransport) -> None:
        self._transport = transport
        self.is_connected = True
        peerName = transport.get_extra_info("peername")
        print(f"Connected to {peerName}")

    def connection_lost(self, exc: Exception | None) -> None:
        self.is_connected = False
        print("Connection has been closed")
        self.on_conn_lost.set_result(True)
        return super().connection_lost(exc)

    def data_received(self, data: bytes) -> None:
        message = data.decode(ENCODING)
        #print(f"Message received: {message}")
        if self.on_data_received:
            self.on_data_received(message)

    def send(self, data: str):
        if data:
            self._transport.write(data.encode(ENCODING))

    # async def get_message(self, loop: asyncio.BaseEventLoop):
    #     while self.is_connected:
    #         message = await loop.run_in_executor(None, input, '>>>')
    #         message = message.strip()
    #         if message == 'q':
    #             self.is_connected = False
    #             self._transport.close()
    #         else:
    #             self.send(message)

    def close(self):
        self._transport.close()


class ChatApp:
    def __init__(self) -> None:
        self._userName = None
        self.loop = asyncio.get_running_loop()
        self.on_conn_lost = self.loop.create_future()
        self.echo_client_protocol = ChatClientProtocol(self.on_conn_lost, self.loop)
        self.echo_client_protocol.on_data_received = self.on_data_received

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username: str):
        self._username = username

    async def get_message(self, loop: asyncio.BaseEventLoop):
        while self.echo_client_protocol.is_connected:
            message = await loop.run_in_executor(None, input, '')
            message = message.strip()
            if message == 'q':
                self.echo_client_protocol.is_connected = False
                self.echo_client_protocol.close()
            else:
                json_packet = {
                    USERNAME: self.username,
                    MESSAGE: message
                }
                packet = json.dumps(json_packet)
                self.echo_client_protocol.send(packet)

    def on_data_received(self, message):
        data = json.loads(message)
        uname = f"[{data[USERNAME]}]".ljust(15)
        print(f"{uname} {data[MESSAGE]}")

    async def prompt_username(self):
        self.username = input("Type in a username: ")

    async def run(self, host: str, port:int):

        await self.prompt_username()
        # Create connection
        transport, protocol = await self.loop.create_connection(
            lambda: self.echo_client_protocol,
            host,
            port
        )

        # Start event loop that listens for input messages
        await self.get_message(self.loop)

        # Handle cleanup when client closes
        try:
            await self.on_conn_lost
        finally:
            transport.close()


async def main():
    # Get a reference to the event loop since we are using low-level APIs
    #loop = asyncio.get_running_loop()
    host = '127.0.0.1'
    port = 5001

    app = ChatApp()
    await app.run(host,port)

    # Create a Future to listen to later so we can detect the closing of the client
    # on_conn_lost = loop.create_future()

    # Create an instance of the EchoClientProtocol
    # echo_client_protocol = ChatClientProtocol(on_conn_lost, loop)

    # # Create connection
    # transport, protocol = await loop.create_connection(
    #     lambda: echo_client_protocol,
    #     host,
    #     port
    # )

    # # Start event loop that listens for input messages
    # await echo_client_protocol.get_message(loop)

    # # Handle cleanup when client closes
    # try:
    #     await on_conn_lost
    # finally:
    #     transport.close()


if __name__ == "__main__":
    asyncio.run(main())
