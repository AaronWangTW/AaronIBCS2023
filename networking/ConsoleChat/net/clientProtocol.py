from abc import ABC, abstractmethod
import asyncio
from typing import Coroutine
from json import loads, dumps

ENCODING = "utf8"


def _async(coro: Coroutine):
    loop = asyncio.get_event_loop()
    return loop.create_task(coro)
    # wrapping normal, non-async method into async method


class AbstractMessageHandler(ABC):
    @abstractmethod
    async def onMessageReceived(self, message: str) -> None:
        raise NotImplementedError

    async def onConnectionLost(self) -> None:
        return None

    async def onClose(self) -> None:
        return None


class AbstractChatClientProtocol(ABC):
    _isConnected: bool = False
    _host: str
    _port: int
    _message_handler: AbstractMessageHandler = None

    def __init__(self, host: str, port: int) -> None:
        self._host = host
        self._port = port

    @property
    def isConnected(self) -> bool:
        return self._isConnected

    @property
    def message_handler(self) -> AbstractMessageHandler:
        return self._message_handler

    @message_handler.setter
    def message_handler(self, handler: AbstractMessageHandler) -> None:
        self._message_handler = handler

    @abstractmethod
    async def connect(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def send(self, data: str) -> None:
        raise NotImplementedError

    @abstractmethod
    async def close(self) -> None:
        raise NotImplementedError


class ChatClientProtocol(AbstractChatClientProtocol, asyncio.Protocol):
    _transport: asyncio.Transport

    async def connect(self) -> None:
        loop = asyncio.get_event_loop()
        await loop.create_connection(lambda: self, self._host, self._port)

    async def send(self, data: str) -> None:
        if data:
            package = data.encode(ENCODING)
            self._transport.write(package)

    async def close(self) -> None:
        self._transport.close()
        self._isConnected = False
        if self.message_handler:
            await self.message_handler.onClose()

    def connection_made(self, transport: asyncio.BaseTransport):
        self._transport = transport
        self._isConnected = True

    def connection_lost(self, exc: Exception | None) -> None:
        self._isConnected = False
        if self.message_handler:
            _async(self.message_handler.onConnectionLost())

    def data_received(self, data: bytes) -> None:
        message = data.decode(ENCODING)
        if self.message_handler:
            _async(self.message_handler.onMessageReceived(message))


class TestProtocol(AbstractChatClientProtocol):
    delay: float = 0.5

    def __init__(self, *, delay: int = 0.5) -> None:
        self.delay = delay

    async def connect(self):
        self._isConnected = True

    async def send(self, data: str):
        await asyncio.sleep(self.delay)
        if data and self._isConnected and self.message_handler:
            await self.message_handler.onMessageReceived(data)

    async def close(self):
        self._isConnected = False
        if self.message_handler:
            await self.message_handler.onClose()
