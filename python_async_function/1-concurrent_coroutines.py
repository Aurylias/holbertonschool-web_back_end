#!/usr/bin/env python3
"""Module using multiple times wait_random asynchronously"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list(float):
    """Calls wait_random n times and store results in a list"""
    delays = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    return sorted(delays)

if __name__ == "__main__":
    print("Wait max 5 second")
    delays = asyncio.run(wait_n(3, 5))
    for data in delays:
        print(data)

    print("\nWait max 10 second")
    delays = asyncio.run(wait_n(3, 10))
    for data in delays:
        print(data)

    print("\nWait max 15 second")
    delays = asyncio.run(wait_n(3, 15))
    for data in delays:
        print(data)
