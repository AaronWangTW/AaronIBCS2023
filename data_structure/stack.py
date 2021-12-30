# take off top and put on top only
# FILO data structure, first in last out
# push -> in, pop -> out

class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Node = None


class Stack:
    def __init__(self) -> None:
        self._head: Node = None
        self._length: int = 0
        self._iter: Node = None

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

    def __len__(self) -> int:
        return self._length

    def __str__(self) -> str:
        s = "["
        node = self._head
        while node:
            s += f"{node.data}"
            node = node.next
            if node is not None:  # if node is not None, so not the last element
                s += ", "
        s += "]"
        return s

    def push(self, data: int):
        n = Node(data)  # create node to be put in
        n.next = self._head  # point the node to the last node added
        self._head = n  # point the head to the new node
        self._length += 1

    def pop(self) -> int:
        if self._head == None:
            return None
        data = self._head.data  # get data of last node
        self._head = self._head.next  # move head to remove last node
        self._length -= 1
        return data


if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(3)
    s.push(420)
    s.push(87)
    s.push(68)

    # customized len
    print("length: ", len(s))
    # customized print
    print(s)

    # customized iteration
    for n in s:
        print(n)

    # customized contains detection
    print(5 in s)

    for i in range(6):
        print(s.pop())
