from typing import Callable
from os import linesep


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.right: Node = None
        self.left: Node = None
        self.height: int = 0


class AVLTree:
    def __init__(self) -> None:
        self._root: Node = None
        self._length: int = 0

    def __len__(self):
        return self._length

    def __iter__(self):
        def inOrderGenerator(root: Node) -> int:
            if root.left:
                yield from inOrderGenerator(root.left)
            yield root.data
            if root.right:
                yield from inOrderGenerator(root.right)
        return inOrderGenerator(self._root)

    def __reversed__(self):
        def reversedGenerator(root: Node) -> int:
            if root.right:
                yield from reversedGenerator(root.right)
            yield root.data
            if root.left:
                yield from reversedGenerator(root.left)
        return reversedGenerator(self._root)

    def __contains__(self, data: int) -> bool:
        root = self._root
        while root:
            if data < root.data:
                root = root.left
            elif data > root.data:
                root = root.right
            else:
                return True
        return False

    def max(self) -> int:
        if self._root is None:
            return None
        root = self._root
        while root.right:
            root = root.right
        return root.data

    def min(self) -> int:
        if self._root is None:
            return None
        root = self._root
        while root.left:
            root = root.left
        return root.data

    def height(self) -> int:
        return self._root.height

    def _height(self, root: Node) -> int:
        if root is None:
            return -1
        root.height = max(self._height(root.left), self._height(root.right))+1
        return root.height

    def _getBalance(self, root: Node = None) -> int:
        if root is None:
            return 0
        return self._height(root.left) - self._height(root.right)

    def _rebalance(self, root: Node = None) -> Node:
        if root is None:
            return None
        balance = self._getBalance(root)
        leftBalance = self._getBalance(root.left)
        rightBalance = self._getBalance(root.right)

        if balance > 1:
            if leftBalance >= 0:
                return self._rotateRight(root)
            else:
                root.left = self._rotateLeft(root.left)
                return self._rotateRight(root)
        elif balance < -1:
            if rightBalance > 0:
                root.right = self._rotateRight(root.right)
                return self._rotateLeft(root)
            else:
                return self._rotateLeft(root)

        return root

    def _rotateRight(self, root: Node) -> Node:
        newRoot = root.left
        rightSubtree = newRoot.right
        newRoot.right = root
        root.left = rightSubtree
        self._height(newRoot)
        return newRoot

    def _rotateLeft(self, root: Node) -> Node:
        newRoot = root.right
        leftSubtree = newRoot.left
        newRoot.left = root
        root.right = leftSubtree

        self._height(newRoot)
        return newRoot

    def insert(self, data: int) -> None:
        self._root = self._insert(data, self._root)

    def _insert(self, data: int, root: Node) -> Node:
        if root is None:
            self._length += 1
            return Node(data)
        if data < root.data:
            root.left = self._insert(data, root.left)
        else:
            root.right = self._insert(data, root.right)

        self._height(root)
        return self._rebalance(root)

    def delete(self, data: int) -> None:
        self._delete(data, self._root)

    def _minNode(self, root: Node) -> Node:
        if root.left:
            return self._minNode(root.left)
        return root

    def _delete(self, data: int, root: Node) -> Node:

        if self._root is None:
            return None
        if data < root.data:
            root.left = self._delete(data, root.left)
        elif data > root.data:
            root.right = self._delete(data, root.right)
        else:
            self._length -= 1
            # if there's only a right subtree
            if root.left is None:
                temp = root.right
                root = None
                return temp
            # if only left subtree
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            # if two children, choose smallest in order successor
            temp = self._minNode(root.right)
            root.data = temp.data
            root.right = self._delete(temp.data, root.right)
        return self._rebalance(root)


def treePrinter(root: Node, dataFunc: Callable, width: int = 64):
    elementCount = 2**(root.height + 1) - 1
    elements = [None] * elementCount

    #    0
    #  1   2
    # 3 4 5 6
    # notice how left side is always node x 2 + 1. e.g. 3 = 1x2 +1
    # right side will be node x2 +2
    def flatten(root: Node, idx: int = 0):
        elements[idx] = dataFunc(root)
        if root.left:
            flatten(root.left, idx*2+1)
        if root.right:
            flatten(root.right, idx*2+2)
    flatten(root)

    def valueStr(val: int, width: int):
        if val is None:
            return "_".center(width)
        return f"{val}".center(width)

    level = 0
    end = 0
    levelWidth = width
    result = ""

    for i, val in enumerate(elements):
        result += valueStr(val, levelWidth)
        if i == end:
            result += linesep
            levelWidth = levelWidth // 2
            level += 1
            end += 2**level
    return result


if __name__ == "__main__":
    avl = AVLTree()

    for i in range(6):
        avl.insert(i)
        print(treePrinter(avl._root, lambda x: x.data))
        print("---------------------------------------------------------------")
