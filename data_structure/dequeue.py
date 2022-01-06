# queue is FIFO, first in first out
# dequeue is both side ok to modify data structure
from typing import Iterator


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Node = None
        self.prev: Node = None


class Dequeue:
    def __init__(self) -> None:
        self._length = 0
        self._tail: Node = None
        self._head: Node = None
        self._iter: Node = None

    def append(self, data: int) -> None:
        node = Node(data)
        if self._tail is None:
            self._head = node
            self._tail = node
        else:
            node.prev = self._tail
            self._tail.next = node
            self._tail = node
        self._length += 1

    def prepend(self, data: int) -> None:
        node = Node(data)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node
        self._length += 1

    def deleteFirst(self) -> int:
        if self._head is None:
            return None
        data = self._head.data
        self._head = self._head.next
        if self._head:  # is not None
            self._head.prev = None
        else:
            self._tail = None  # if all things dequeued, the tail also need to be dequeued or it crashes
        self._length -= 1
        return data

    def deleteLast(self) -> int:
        if self._tail is None:
            return None
        data = self._tail.data
        self._tail = self._tail.prev
        if self._tail:
            self._tail.next = None
        else:
            self._head = None
        self._length -= 1
        return data

    def __iter__(self):
        self._iter = self._head
        return self

    def __next__(self):
        if self._iter is None:
            raise StopIteration
        temp = self._iter.data
        self._iter = self._iter.next
        return temp

    def __reversed__(self) -> Iterator:
        def reverseIterator():
            r_iter = self._tail
            while r_iter:
                yield r_iter.data
                r_iter = r_iter.prev
        return reverseIterator()

    def __contains__(self, data: int) -> bool:
        for d in self:
            if d == data:
                return True
        return False

    def __str__(self) -> str:
        s = "["
        for d in self:
            s += str(d)+", "
        s = s[:-2]
        s += "]"
        return s

    def __len__(self):
        return self._length


if __name__ == "__main__":
    q = Dequeue()
    for i in range(1, 6):
        q.append(i)

    print("length:", len(q))
    print(q)
    print(f"Queue has 5: {5 in q}")

    for i in range(6):
        print(f"delete first: {q.deleteFirst()}\t Length: {len(q)}")

    for i in range(1, 6):
        q.prepend(i)

    print("length:", len(q))
    print(q)
    print(f"Queue has 5: {5 in q}")

    for i in range(6):
        print(f"delete last: {q.deleteLast()}\t Length: {len(q)}")

    for i in range(1, 6):
        q.append(i)
    print("normal",[x for x in q])
    print("reversed",[x for x in reversed(q)])