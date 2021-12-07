from typing import Any
import numpy.random as random

ENCODING = "UTF-8"
PERMUTATION_SIZE = 256
ROTOR_DIMS = (10,20)

class Enigma:
    def __init__(self, seed: Any) -> None:
        random.seed(seed)
        self._plugboard = Plugboard()
        self._rotors = []
        self._reflector = Reflector()
        num_rotors = random.randint(ROTOR_DIMS[0],ROTOR_DIMS[1])
        for _ in range(0,num_rotors):
            self._rotors.append(Rotor())

    def encipher(self, val: int) -> int:
        # pass one way through
        cipher = self._plugboard.encipherForwards(val)
        for idx, rotor in enumerate(self._rotors):
            # Always rotate first rotor
            if idx == 0:
                rotor.rotate()
            elif self._rotors[idx-1].rotateNext():
                rotor.rotate()
            cipher = rotor.encipherForwards(cipher)
        cipher = self._reflector.encipher(cipher)
        for rotor  in self._rotors[::-1]:
            cipher = rotor.encipherBackwards(cipher)
        
        cipher = self._plugboard.encipherBackwards(cipher)
        return cipher


class Plugboard:
    def __init__(self) -> None:
        self._wires = [i for i in range(PERMUTATION_SIZE)]
        swapped = []
        for idx, val in enumerate(self._wires):
            if idx not in swapped and random.randint(0, PERMUTATION_SIZE+1) <= round(PERMUTATION_SIZE*0.6):
                # each wire 60% chance to be swapped
                # choose random location to swap
                loc = random.randint(0, len(self._wires)-1)
                if loc not in swapped:
                    tmp = self._wires[loc]
                    self._wires[loc] = val
                    self._wires[idx] = tmp
                    swapped.insert(0, idx)
                    swapped.insert(0, loc)

    def encipherForwards(self, val: int) -> int:
        cipher = self._wires[val]
        return cipher

    def encipherBackwards(self, val: int) -> int:
        cipher = self._wires.index(val)
        return cipher

    def __str__(self) -> str:
        s = "Plugboard: \n"
        for idx, val in enumerate(self._wires):
            s = s + f"{idx} - {val}\t"
        return s


class Rotor:
    def __init__(self) -> None:
        self._rotor_pos = 0
        self._rotate_next_pos = random.randint(0, PERMUTATION_SIZE - 1)
        self._wires = [i for i in range(0,PERMUTATION_SIZE)]
        random.shuffle(self._wires)
        self.setPosition(random.randint(0,PERMUTATION_SIZE - 1))

    def setPosition(self, position):
        change = self._wires.index(position) - self._rotor_pos
        self._rotor_pos = position
        self._wires = self._wires[change:] + self._wires[:change] # put the end half to the front

    def rotate(self):
        self._rotor_pos = (self._rotor_pos + 1)% PERMUTATION_SIZE
        self._wires = self._wires[1:] + self._wires[:1]

    def rotateNext(self) -> bool:
        return self._rotor_pos == self._rotate_next_pos

    def encipherForwards(self, val: int) -> int:
        cipher = self._wires[val]
        return cipher

    def encipherBackwards(self, val: int) -> int:
        cipher = self._wires.index(val)
        return cipher
    def __str__(self) -> str:
        s = f"Rotor\n\t{self._wires}\n\tRotor Position: {self._rotor_pos}\n\tRotate Next Position: {self._rotate_next_pos}"
        return s

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
                self._permutations[idx] = rnd
                self._permutations[rnd] = idx
                tempVals.remove(idx)
                tempVals.remove(rnd)

    def encipher(self, val: bytes) -> int:
        return self._permutations[val]


if __name__ == "__main__":
    # test components
    print("Reflector:")
    r = Reflector()
    print(r._permutations)
    print(r.encipher(5))
    p = Plugboard()
    print(p)
    rot = Rotor()
    print(rot)
    # test whole enigma
    e = Enigma(100)
    cipher=e.encipher(5)
    print(cipher)
    e = Enigma(100)
    cipher = e.encipher(cipher)
    print(cipher)
