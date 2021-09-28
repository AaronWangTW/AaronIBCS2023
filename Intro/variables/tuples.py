# Tuples are like lists but immutable
# slightly more space/time efficient than list cuz can't be changed
import sys
import time

list1 = [1, 2, 3, 4, 5]
tuple1 = (1, 2, 3, 4, 5)

print("list1 size: ", sys.getsizeof(list1))
print("tuple1 size: ", sys.getsizeof(tuple1))

startTime = time.time()
list2 = list(range(1000000))
endTime = time.time()
print(f"Size: {sys.getsizeof(list2)}\nTime: {endTime-startTime}")

startTime = time.time()
tuple2 = tuple(range(1000000))
endTime = time.time()
print(f"Size: {sys.getsizeof(tuple2)}\nTime: {endTime-startTime}")

# slightly more time efficient on average
# but most importantly, protects data

myTuple = (5,) * 10
print(myTuple)

print(f"address: {hex(id(myTuple))}")
myTuple = myTuple + (1, 2, 3)
print(myTuple)
print(f"address: {hex(id(myTuple))}")
#seems like changing tuple, but actually creating a new one
