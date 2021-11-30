from typing import Any
import numpy.random as random

ENCODING = "UTF-8"
PERMUTATION_SIZE = 8

class Enigma:
    def __init__(self, seed: Any) -> None:
        random.seed(seed)

    def encipher(self, val: int) -> int:
        pass


class Plugboard:
    def __init__(self) -> None:
        pass

    def encipherForwards(self, val: int) -> int:
        pass

    def encipherBackwards(self, val: int) -> int:
        pass


class Rotor:
    def __init__(self) -> None:
        pass

    def setPosition(self, position):
        pass

    def rotate(self):
        pass

    def rotateNext(self) -> bool:
        pass

    def encipherForwards(self, val: int) -> int:
        pass

    def encipherBackwards(self, val: int) -> int:
        pass


class Reflector:
    def __init__(self) -> None:
        self._permutations = [i for i in range(0, PERMUTATION_SIZE)]
        tempVals = [i for i in range(0, PERMUTATION_SIZE)]
        for idx, val in enumerate(self._permutations):
            if idx == val:
                rnd = idx
                while idx == rnd:
                    # choose random value from tempVals until different
                    rnd = random.choice(tempVals)
                self._permutations[idx]=rnd
                self._permutations[rnd]=idx
                tempVals.remove(idx)
                tempVals.remove(rnd)


    def encipher(self, val: bytes) -> int:
        return self._permutations[val]

if __name__ == "__main__":
    r = Reflector()
    print(r._permutations)
    print(r.encipher(5))