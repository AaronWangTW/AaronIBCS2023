from math import pi


class Circle:
    def __init__(self, r: float) -> None:
        # documentation
        """
        Object constructor
        
        Args:
            r: radius of circle
        """
        self._r = r
        # r public, _r protected,__r private
        print(f"Object class Circle instantiated. r:{r}")

    @property
    def r(self):
        return self._r

    @property
    def circumference(self):
        return round(2*self._r*pi, 3)

    @property
    def area(self):
        return round(self._r**2*pi, 3)

    @r.setter
    def r(self, r: float):
        if r <= 0:
            raise ValueError("radius must be >0")
        self._r = r

    def copy(self):
        return Circle(self._r)

    # python version of Java ToString()
    def __str__(self) -> str:
        return f"Class Circle | r: {self._r}\tcircumference: {self.circumference}\tarea: {self.area}"

    # Overriding Comparators

    # greater than
    def __gt__(self, other):
        if type(other) == Circle:
            return self._r > other._r
        if type(other) == float or type(other) == int:
            return self.area > other.area
        # if other object has an area member
        area = getattr(other, "area", None)
        if area is not None:
            return self.area > other.area
        return False

    # less than
    def __lt__(self, other):
        if type(other) == Circle:
            return self._r < other._r
        if type(other) == float or type(other) == int:
            return self.area < other.area
        # if other object has an area member
        area = getattr(other, "area", None)
        if area is not None:
            return self.area < other.area
        return False
    # equal to

    def __eq__(self, other):
        if type(other) == Circle:
            return self._r == other._r
        if type(other) == float or type(other) == int:
            return self.area == other.area
        # if other object has an area member
        area = getattr(other, "area", None)
        if area is not None:
            return self.area == other.area
        return False


class Rectangle:
    def __init__(self, w: float, h: float) -> None:
        self._w = w
        self._h = h
        print(f"Object class Rectangle instantiated. w:{w} h:{h}")

    @property
    def w(self):
        return self._w

    @property
    def h(self):
        return self._h

    @property
    def circumference(self):
        return 2*self._h+2*self._w

    @property
    def area(self):
        return self._w*self._h

    @w.setter
    def w(self, w: float):
        if w <= 0:
            raise ValueError("width must be >0")
        self._w = w

    @h.setter
    def h(self, h: float):
        if h <= 0:
            raise ValueError("height must be >0")
        self._h = h

    def copy(self):
        return Rectangle(self._w, self._h)

    def __str__(self) -> str:
        return f"Class Rectangle | \tw: {self._w} \th: {self._h}\tcircumference: {self.circumference}\tarea: {self.area}"


def main():
    # construct instance
    c1 = Circle(5.0)
    # get property
    print(c1.r)
    # set attribute method 1
    c1.__setattr__("r", 7.0)
    print(c1.r)
    # set attribute method 2
    c1.r = 9.0
    print(c1.r)
    # setter safety check
    try:
        c1.r = -3
    except ValueError as e:
        print(e)
    # property extended 1
    print(f"circumference: {c1.circumference}")
    # property extended 2
    print(f"area: {c1.area}")
    # test __str__
    print(c1)

    # test class rectangle
    r1 = Rectangle(3.0, 5.0)
    print(r1)
    r1.h = 4.0
    r1.w = 12.0
    print(r1)

    #test copy
    c2 = c1.copy()
    print(f"same object? {id(c1) == id(c2)}")

    #test comparator override
    c2.r = 7.0
    print(c1 > c2, c1 < c2)
    c2.r = 9.0
    print(f"same radius? {c1==c2}")
    print(f"same area? {c1==c2.area}")
    # test compare other obj
    print(f"rec and circle same area? {c1==r1}")


if __name__ == "__main__":
    main()
