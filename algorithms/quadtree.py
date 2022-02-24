from collections import namedtuple
from typing import List


Coord = namedtuple("Coord", ["x", "y"])


class Quad:
    def __init__(self, right: int, bottom: int, maxcap: int):
        self.ne = None
        self.se = None
        self.nw = None
        self.sw = None
        self.right = right
        self.bottom = bottom
        self.children: List[Coord] = []
        self.max_cap = maxcap
        self.divided = False

    def add(self, child:Coord):
        if len(self) < self.max_cap and not self.divided:
            self.children.append(child)
        else:
            if self.ne == None:
                self.children.append(child)
                self.divide()
            else: 
                if child.x < self.right/2:
                    if child.y < self.bottom/2:
                        self.nw.add(child)
                    else:
                        self.sw.add(child)
                else:
                    if child.y < self.bottom/2:
                        self.ne.add(child)
                    else:
                        self.se.add(child)

    def divide(self):
        nwQuad = Quad(self.right/2,self.bottom/2,self.max_cap)
        neQuad = Quad(self.right,self.bottom/2,self.max_cap)
        swQuad = Quad(self.right/2,self.bottom,self.max_cap)
        seQuad = Quad(self.right,self.bottom,self.max_cap)
        for child in self.children:
            if child.x < self.right/2:
                if child.y < self.bottom/2:
                    nwQuad.children.append(child)
                else:
                    swQuad.children.append(child)
            else:
                if child.y < self.bottom/2:
                    neQuad.children.append(child)
                else:
                    seQuad.children.append(child)
        self.children=[]
        self.divided = True
        self.nw = nwQuad
        self.ne = neQuad
        self.sw = swQuad
        self.se = seQuad

    def __len__(self):
        return len(self.children)

    def __str__(self):
        cd = [f"({c.x}, {c.y})" for c in self.children]

        return f"""Quad ({self.right}, {self.bottom}): {len(self.children)}
    {', '.join(cd)}
NW:{self.nw}
NE:{self.ne}
SW:{self.sw}
SE:{self.se}
"""


class QuadTree:
    def __init__(self, right: int, bottom: int, max_cap: int = 5):
        self._max_cap = max_cap
        self._root = Quad(right=right, bottom=bottom, maxcap=self._max_cap)

    def add(self, child: Coord):
        self._root.add(child)

    def __str__(self):
        return str(self._root)


if __name__ == "__main__":
    qt = QuadTree(1024, 1024,5)

    qt.add(Coord(256, 256))
    qt.add(Coord(768, 256))
    qt.add(Coord(256, 768))
    qt.add(Coord(768, 768))
    qt.add(Coord(256, 100))
    qt.add(Coord(256, 200))
    qt.add(Coord(256, 300))
    qt.add(Coord(256, 400))
    qt.add(Coord(100, 400))
    qt.add(Coord(200, 400))
    qt.add(Coord(300, 400))
    qt.add(Coord(400, 400))
    print(qt)
    print("─" * 50)
