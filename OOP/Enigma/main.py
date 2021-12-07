from typing import final
import numpy.random as random
import os

import enigma as eg

os.chdir(os.path.dirname(__file__))

def encipherString(seed:any,data:bytearray):
    e = eg.Enigma(seed)
    encodedBuffer = bytearray()

    for b in data:
        encodedByte = e.encipher(b)
        encodedBuffer.append(encodedByte)

    return encodedBuffer


def main():
    s = "hello"
    data = bytearray(s.encode('UTF-8'))
    ciphertext = encipherString(100, data)
    print(ciphertext)

    plaintext = encipherString(100, ciphertext)
    print(plaintext.decode("UTF-8"))

if __name__ == "__main__":
    main()
    