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

def encipherTxt(inFilePath: str, outFilePath: str, seed:any):
    # rb -> read byte, wb -> write byte
    with open(inFilePath, "rb") as infd, open(outFilePath,"wb") as outfd:
        e =eg.Enigma(seed)
        while True:
            # read 64 bytes of data, usually would be larger
            buffer = infd.read(64)
            if buffer:
                encipheredBuffer = bytearray()
                for b in buffer:
                    encipheredBuffer.append(e.encipher(b))
                outfd.write(encipheredBuffer)
            else:
                break


def main():
    s = "hello"
    data = bytearray(s.encode('UTF-8'))
    ciphertext = encipherString(100, data)
    print(ciphertext)

    plaintext = encipherString(100, ciphertext)
    print(plaintext.decode("UTF-8"))

    encipherTxt("plaintext.txt","result.txt",100)
    encipherTxt("result.txt","rebuilt.txt",100)

if __name__ == "__main__":
    main()
    