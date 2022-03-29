import asyncio
import time


async def message(message: str, delay: int = 2):
    await asyncio.sleep(delay)
    print(message)


async def noTasks():
    print(f"Started at {time.strftime('%X')}")
    delay = 1
    for i in range(3):
        await message(f"First loop {i}",delay)

    delay = 2
    for i in range(3):
        await message(f"First loop {i}",delay)

    print(f"Finished at {time.strftime('%X')}")

async def tasksList():
    print(f"Started at {time.strftime('%X')}")

    tasks = []

    delay = 1
    for i in range(3):
        tasks.append(message(f"First loop {i}",delay))

    delay = 2
    for i in range(3):
        tasks.append(message(f"First loop {i}",delay))

    for task in tasks:
        await task

    print(f"Finished at {time.strftime('%X')}")

async def tasksGather():
    print(f"Started at {time.strftime('%X')}")

    tasks = []

    delay = 1
    for i in range(3):
        tasks.append(message(f"First loop {i}",delay))

    delay = 2
    for i in range(3):
        tasks.append(message(f"First loop {i}",delay))

    await asyncio.gather(*tasks)

    print(f"Finished at {time.strftime('%X')}")


if __name__ == "__main__":
    #asyncio.run(noTasks())
    #asyncio.run(tasksList())
    asyncio.run(tasksGather())
