
class block:
    age = 0
    data = 0

    def __init__(self, age: int, data: int) -> None:
        self.age = age
        self.data = data

    def __str__(self) -> str:
        return "[age:"+self.age+", data:"+self.data+"]"


class LRUCache:

    maxKeyNum = 0
    keyNum = 0
    lastAge = 0
    minAge = 1
    map = {}  # map key -> block(age, data)
    ageMap = {}  # map age -> key

    def __init__(self, capacity: int):
        self.maxKeyNum = capacity

    def __str__(self) -> str:
        dict = {}
        for key in self.map:
            dict[key] = self.map[key].data
        return str(dict)

    def get(self, key: int) -> int:
        if key in self.map:
            self.ageMap[self.lastAge] = key
            del self.ageMap[self.map[key].age]
            self.map[key].age = self.lastAge
            self.lastAge += 1
            self.minAge += 1
            return self.map[key].data
        return -1

    def put(self, key: int, value: int) -> None:

        if key not in self.map and self.keyNum < self.maxKeyNum:
            self.map[key] = block(self.lastAge, value)
            self.ageMap[self.lastAge] = key
            self.lastAge += 1
            self.keyNum += 1
        elif key not in self.map and self.keyNum == self.maxKeyNum:
            del self.map[self.ageMap[self.minAge]]
            del self.ageMap[self.minAge]
            self.ageMap[self.lastAge] = key
            self.map[key] = block(self.lastAge, value)
            self.minAge += 1
            self.lastAge += 1
        elif key in self.map:
            self.map[key].data = value
            self.ageMap[self.lastAge] = key
            del self.ageMap[self.map[key].age]
            self.map[key].age = self.lastAge
            self.lastAge += 1


def main():
    testCache = LRUCache(3)
    testCache.put(1, 46)
    testCache.put(7, 28)
    testCache.put(6, 35)
    print(testCache)
    testCache.put(1, 68)
    print(testCache)
    testCache.put(9, 81)
    print(testCache)
    testCache.put(10, 100)
    print(testCache)
    print(testCache.get(1))
    testCache.put(2,20)
    print(testCache)
    testCache.put(3,39)
    print(testCache)
    print(testCache.get(2))

    # There's still bug, but to fix it node or other method might be needed
    # I'll try to fix it if I have time

if __name__ == "__main__":
    main()
