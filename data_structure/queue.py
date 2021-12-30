# queue is FIFO, first in first out
# enqueue -> in, dequeue -> out
class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Node = None


class Queue:
    def __init__(self) -> None:
        self._length = 0
        self._tail: Node = None
        self._head: Node = None
        self._iter: Node = None

    def enqueue(self, data: int) -> None:
        node = Node(data)
        if self._tail is None:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._length += 1

    def dequeue(self) -> int:
        if self._head is None:
            return None
        data = self._head.data
        self._head = self._head.next
        self._length -= 1
        if self._head is None:
            self._tail = None  # if all things dequeued, the tail also need to be dequeued or it crashes
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
    q = Queue()
    for i in range(1, 6):
        q.enqueue(i)

    print("length:", len(q))
    print(q)
    print(f"Queue has 5: {5 in q}")

    for i in range(6):
        print(f"Dequeue: {q.dequeue()}\t Length: {len(q)}")